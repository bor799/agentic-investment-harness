#!/usr/bin/env python3
"""desk_twitter_pipeline 的确定性测试：全合成数据（不含真实账号或原文），无网络。"""
import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

PIPELINE = pathlib.Path(__file__).resolve().parents[1] / 'desk_twitter_pipeline.py'
REF_DAY = '20261119'  # 窗口 20261113 ~ 20261119


def run_cli(*argv):
    proc = subprocess.run([sys.executable, str(PIPELINE), *argv], capture_output=True, text=True, timeout=60)
    try:
        payload = json.loads(proc.stdout.strip().splitlines()[-1]) if proc.stdout.strip() else {}
    except json.JSONDecodeError:
        payload = {'raw': proc.stdout}
    return proc.returncode, payload


def make_post(pid, screen, text, iso, retweet=False):
    return {'id': pid, 'text': text, 'createdAtISO': iso, 'createdAt': 'Wed Nov 18 10:00:00 +0000 2026',
            'isRetweet': retweet, 'lang': 'en', 'author': {'id': '1', 'name': 'n', 'screenName': screen}}


def write_batch(root, day, accounts, posts_map, done=True, manifest_extra=None):
    d = pathlib.Path(root) / day
    (d / 'posts').mkdir(parents=True, exist_ok=True)
    manifest = {'finished_at': f'{day[:4]}-{day[4:6]}-{day[6:]}T01:00:00+00:00', 'status': 'complete', 'accounts': accounts}
    if manifest_extra:
        manifest.update(manifest_extra)
    (d / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False), encoding='utf-8')
    if done:
        (d / 'DONE.json').write_text(json.dumps({'status': 'complete'}), encoding='utf-8')
    for handle, posts in posts_map.items():
        (d / 'posts' / f'{handle}.json').write_text(
            json.dumps({'ok': True, 'schema_version': 1, 'data': posts}, ensure_ascii=False), encoding='utf-8')
    return d


def std_root(tmp):
    """三天完成批次（含旧式 YYMMDD 命名）+ 一个无 DONE 目录。"""
    root = pathlib.Path(tmp) / 'weekly'
    write_batch(root, '20261115',
                [{'handle': 'alpha_test', 'status': 'fetched'}, {'handle': 'beta_test', 'status': 'rate_limited'}],
                {'alpha_test': [
                    make_post('9001', 'alpha_test', '旧版本推文', '2026-11-14T08:00:00+00:00'),
                    make_post('9002', 'alpha_test', '窗口外旧帖', '2026-11-01T08:00:00+00:00'),
                    make_post('9003', 'other_guy', '账号错配帖', '2026-11-15T08:00:00+00:00'),
                    make_post('9004', 'alpha_test', '转推内容', '2026-11-15T09:00:00+00:00', retweet=True)]})
    write_batch(root, '20261117',
                [{'handle': 'alpha_test', 'status': 'fetched'}, {'handle': 'beta_test', 'status': 'fetched'}],
                {'alpha_test': [make_post('9001', 'alpha_test', '新版本推文', '2026-11-14T08:00:00+00:00')],
                 'beta_test': [make_post('9101', 'beta_test', 'beta 看多 AI 资本开支', '2026-11-16T08:00:00+00:00'),
                               make_post('9102', 'beta_test', 'beta 后来看空估值', '2026-11-16T07:00:00+00:00')]})
    write_batch(root, '20261118',
                [{'handle': 'alpha_test', 'status': 'fetched'}, {'handle': 'beta_test', 'status': 'error'}],
                {'alpha_test': [make_post('9201', 'alpha_test', 'alpha 看空估值', '2026-11-17T08:00:00+00:00')]})
    write_batch(root, '261115', [{'handle': 'ghost_test', 'status': 'fetched'}],  # 旧命名但无 DONE → 跳过
                {'ghost_test': [make_post('9999', 'ghost_test', '孤儿', '2026-11-14T08:00:00+00:00')]}, done=False)
    return root


def std_analysis():
    return {'themes': [{
        'id': 'ai-capex', 'label': 'AI资本开支', 'horizon': '中期', 'scope': '同一论题+对象', 'gap': '资本开支是否转化为每股现金流',
        'claims': [
            {'post_id': '9101', 'stance': 'bull', 'summary': 'beta 认为订单周期开启'},
            {'post_id': '9201', 'stance': 'bear', 'summary': 'alpha 认为估值已透支'}],
        'impacts': [{
            'symbol': 'CRWV', 'assessment': '算力订单上升利好营收', 'counterpoint': '折旧与融资可能吞掉现金',
            'next_check': '下一季经营现金流', 'status': 'supported',
            'metrics': [{'name': '资本开支', 'value': 123, 'unit': 'USD', 'period': 'FY26Q3',
                         'baseline_value': 100, 'baseline_period': 'FY26Q2', 'basis': '同口径 capex',
                         'source_url': 'https://example.com/ir', 'source_date': '2026-11-10'}]}]}]}


class TestPrepare(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = std_root(self.tmp.name)
        self.preview = pathlib.Path(self.tmp.name) / 'preview.json'

    def test_happy_path(self):
        code, payload = run_cli('prepare', '--root', str(self.root), '--day', REF_DAY, '--output', str(self.preview))
        self.assertEqual(code, 0, payload)
        data = json.loads(self.preview.read_text(encoding='utf-8'))
        self.assertEqual(data['window']['start'], '2026-11-13T00:00:00+08:00')
        self.assertEqual(data['window']['end'], '2026-11-19T23:59:59+08:00')
        cov = data['coverage']
        self.assertEqual(cov['denominator'], 6)  # 2+2+2
        self.assertEqual(cov['succeeded'], 4)    # 1+2+1
        self.assertEqual(cov['missing'], 1)      # beta rate_limited
        self.assertEqual(cov['errors'], 1)       # beta error
        self.assertEqual(cov['days_completed'], 3)
        self.assertIn('20261116', cov['days_missing'])
        self.assertTrue(any(s['dir'] == '261115' and s['reason'] == 'no_done' for s in cov['skipped_incomplete']))
        ids = {p['id'] for p in data['posts']}
        self.assertEqual(ids, {'9001', '9101', '9102', '9201'})  # 去重+过滤窗口外/错配/转推
        post = next(p for p in data['posts'] if p['id'] == '9001')
        self.assertEqual(post['text'], '新版本推文')     # 后到批次覆盖同 ID
        self.assertEqual(post['url'], 'https://x.com/alpha_test/status/9001')
        self.assertTrue(all(p['url'].startswith('https://x.com/') for p in data['posts']))
        self.assertEqual([p['id'] for p in data['posts']], ['9201', '9101', '9102', '9001'])  # 新→旧

    def test_stale_no_completed_batch(self):
        empty = pathlib.Path(self.tmp.name) / 'weekly2'
        empty.mkdir()
        code, payload = run_cli('prepare', '--root', str(empty), '--day', REF_DAY, '--output', str(self.preview))
        self.assertEqual(code, 1)
        self.assertFalse(payload.get('ok'))
        self.assertTrue(any('不复用旧成果' in e for e in payload['errors']), payload)

    def test_corrupt_manifest_and_missing_posts(self):
        bad = write_batch(self.root, '20261119', [{'handle': 'alpha_test', 'status': 'fetched'}], {})
        (bad / 'manifest.json').write_text('{oops', encoding='utf-8')
        write_batch(self.root, '20261116', [{'handle': 'beta_test', 'status': 'fetched'}],
                    {'alpha_test': [make_post('9301', 'alpha_test', 'x', '2026-11-16T00:00:00+00:00')]})  # 帖子文件缺失
        code, payload = run_cli('prepare', '--root', str(self.root), '--day', REF_DAY, '--output', str(self.preview))
        self.assertEqual(code, 0, payload)
        data = json.loads(self.preview.read_text(encoding='utf-8'))
        cov = data['coverage']
        self.assertTrue(any(s['reason'] == 'manifest_unreadable' for s in cov['skipped_incomplete']))
        self.assertTrue(any(p.get('error') == 'read_failed' for p in cov['read_problems']))
        self.assertNotIn('9301', {p['id'] for p in data['posts']})

    def test_legacy_manifest_batch(self):
        """上一代采集器格式（expected_accounts、无逐账号状态）受控纳入。"""
        root = pathlib.Path(self.tmp.name) / 'weekly3'
        d = pathlib.Path(root) / '20261114'
        (d / 'posts').mkdir(parents=True)
        (d / 'manifest.json').write_text(json.dumps({
            'as_of': '2026-11-13T16:14:48+00:00', 'timezone': 'Asia/Shanghai',
            'expected_accounts': ['leg_a', 'leg_b', 'leg_c'], 'status': 'complete'}, ensure_ascii=False), encoding='utf-8')
        (d / 'DONE.json').write_text('{"status":"complete"}', encoding='utf-8')
        (d / 'posts' / 'leg_a.json').write_text(json.dumps(
            {'ok': True, 'schema_version': 1, 'data': [make_post('7001', 'leg_a', 'legacy 帖', '2026-11-13T10:00:00+00:00')]}), encoding='utf-8')
        (d / 'posts' / 'leg_b.json').write_text('{broken', encoding='utf-8')
        # leg_c 文件缺失
        code, payload = run_cli('prepare', '--root', str(root), '--day', REF_DAY, '--output', str(self.preview))
        self.assertEqual(code, 0, payload)
        data = json.loads(self.preview.read_text(encoding='utf-8'))
        cov = data['coverage']
        self.assertEqual(cov['denominator'], 3)
        self.assertEqual(cov['succeeded'], 1)   # 只有 leg_a 可读
        self.assertEqual(cov['missing'], 2)     # 损坏 + 缺文件记缺口，不猜明细
        entry = cov['batches'][0]
        self.assertTrue(entry['legacy'])
        self.assertEqual(entry['denominator'], 3)
        self.assertEqual(cov['days_completed'], 1)
        self.assertEqual([p['id'] for p in data['posts']], ['7001'])
        self.assertEqual(data['data_cutoff'], '2026-11-13T16:14:48+00:00')
        self.assertTrue(any(p.get('error') == 'read_failed' for p in cov['read_problems']))

    def test_day_history_window(self):
        code, payload = run_cli('prepare', '--root', str(self.root), '--day', '20261117', '--output', str(self.preview))
        self.assertEqual(code, 0, payload)
        data = json.loads(self.preview.read_text(encoding='utf-8'))
        self.assertEqual(data['window']['start'], '2026-11-11T00:00:00+08:00')
        self.assertEqual(data['window']['end'], '2026-11-17T23:59:59+08:00')
        self.assertNotIn('9201', {p['id'] for p in data['posts']})  # 18 日批不在历史窗口


class TestBuild(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = std_root(self.tmp.name)
        self.preview = pathlib.Path(self.tmp.name) / 'preview.json'
        self.analysis = pathlib.Path(self.tmp.name) / 'analysis.json'
        self.out = pathlib.Path(self.tmp.name) / 'batch.json'
        code, payload = run_cli('prepare', '--root', str(self.root), '--day', REF_DAY, '--output', str(self.preview))
        self.assertEqual(code, 0, payload)

    def build(self, analysis):
        self.analysis.write_text(json.dumps(analysis, ensure_ascii=False), encoding='utf-8')
        return run_cli('build', '--input', str(self.preview), '--analysis', str(self.analysis), '--output', str(self.out))

    def test_happy_path(self):
        code, payload = self.build(std_analysis())
        self.assertEqual(code, 0, payload)
        batch = json.loads(self.out.read_text(encoding='utf-8'))['batch']
        self.assertEqual(batch['batch_id'], f'x-consensus-{REF_DAY}')
        self.assertEqual(batch['kind'], 'twitter')
        kinds = [f'{i["kind"]}/{i["category"]}' for i in batch['items']]
        self.assertIn('health/fact', kinds)
        self.assertIn('opinion/ai_explainer', kinds)
        self.assertEqual(kinds.count('opinion/external_opinion'), 2)  # 每主题≤3，此处两位作者
        self.assertIn('report/fact', kinds)
        theme = next(i for i in batch['items'] if i['category'] == 'ai_explainer')
        self.assertEqual(theme['stance'], 'mixed')  # 牛熊并存 → mixed
        self.assertIn('参与：2 位作者', theme['body'])
        self.assertIn('4/6 账号日', theme['coverage_note'])  # 覆盖≠参与，分开表达
        self.assertIn('CRWV', theme['symbols'])
        report = next(i for i in batch['items'] if i['kind'] == 'report')
        self.assertIn('123 USD', report['body'])
        self.assertIn('基线 100', report['body'])
        self.assertIn('https://example.com/ir', report['body'])
        for item in batch['items']:
            if item['category'] == 'external_opinion':
                self.assertTrue(item['url'].startswith('https://x.com/'))

    def test_author_merged_and_same_author_mixed(self):
        analysis = std_analysis()
        # 同一作者 beta 的另一条帖子转空 → 作者归并 mixed，参与仍只计 1 位
        analysis['themes'][0]['claims'].append({'post_id': '9102', 'stance': 'bear', 'summary': 'beta 后来看空估值'})
        code, payload = self.build(analysis)
        self.assertEqual(code, 0, payload)
        theme = next(i for i in json.loads(self.out.read_text(encoding='utf-8'))['batch']['items'] if i['category'] == 'ai_explainer')
        self.assertIn('参与：2 位作者', theme['body'])  # 同作者只计一次
        self.assertEqual(theme['stance'], 'mixed')

    def test_empty_themes_health_only(self):
        code, payload = self.build({'themes': []})
        self.assertEqual(code, 0, payload)
        items = json.loads(self.out.read_text(encoding='utf-8'))['batch']['items']
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['kind'], 'health')

    def _reject(self, analysis, needle):
        code, payload = self.build(analysis)
        self.assertEqual(code, 1, payload)
        self.assertTrue(any(needle in e for e in payload.get('errors', [])), payload)

    def test_reject_unknown_post_id(self):
        a = std_analysis(); a['themes'][0]['claims'][0]['post_id'] = '888888'
        self._reject(a, '不在预览中')

    def test_reject_bad_stance(self):
        a = std_analysis(); a['themes'][0]['claims'][0]['stance'] = 'very-bull'
        self._reject(a, 'stance 非法')

    def test_reject_empty_counterpoint(self):
        a = std_analysis(); a['themes'][0]['impacts'][0]['counterpoint'] = '  '
        self._reject(a, '反证不得为空')

    def test_reject_supported_without_metric(self):
        a = std_analysis(); a['themes'][0]['impacts'][0]['metrics'] = []
        self._reject(a, '没有一条完整可比数值')

    def test_reject_metric_missing_baseline(self):
        a = std_analysis(); del a['themes'][0]['impacts'][0]['metrics'][0]['baseline_value']
        self._reject(a, "缺 ['baseline_value']")

    def test_reject_future_source_date(self):
        a = std_analysis(); a['themes'][0]['impacts'][0]['metrics'][0]['source_date'] = '2031-01-01'
        self._reject(a, '来自未来')

    def test_reject_lowercase_symbol(self):
        a = std_analysis(); a['themes'][0]['impacts'][0]['symbol'] = 'crwv'
        self._reject(a, 'symbol 非法')

    def test_reject_empty_claims(self):
        a = std_analysis(); a['themes'][0]['claims'] = []
        self._reject(a, 'claims 必须是非空数组')

    def test_reject_duplicate_claim(self):
        a = std_analysis(); a['themes'][0]['claims'].append(a['themes'][0]['claims'][0])
        self._reject(a, '重复')

    def test_reject_missing_themes_key(self):
        self._reject({'foo': 1}, 'themes 数组')

    def test_reject_preview_without_posts(self):
        bad = pathlib.Path(self.tmp.name) / 'bad_preview.json'
        bad.write_text('{"window": {}}', encoding='utf-8')
        self.analysis.write_text(json.dumps(std_analysis()), encoding='utf-8')
        code, payload = run_cli('build', '--input', str(bad), '--analysis', str(self.analysis), '--output', str(self.out))
        self.assertEqual(code, 1)
        self.assertTrue(any('请先运行 prepare' in e for e in payload.get('errors', [])))

    def test_output_passes_board_contract(self):
        code, _ = self.build(std_analysis())
        self.assertEqual(code, 0)
        batch = json.loads(self.out.read_text(encoding='utf-8'))['batch']
        import re
        self.assertRegex(batch['batch_id'], r'^[A-Za-z0-9._:-]{4,128}$')
        for item in batch['items']:
            self.assertRegex(item['logical_id'], r'^[A-Za-z0-9._:-]{3,160}$')
            self.assertTrue(item['title'] and len(item['title']) <= 300)
            self.assertLessEqual(len(item.get('body') or ''), 8000)
            self.assertLessEqual(len(item.get('coverage_note') or ''), 500)
            for s in item.get('symbols') or []:
                self.assertRegex(s, r'^[A-Z0-9.^-]{1,12}$')
            if item.get('url'):
                self.assertTrue(item['url'].startswith('https://'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
