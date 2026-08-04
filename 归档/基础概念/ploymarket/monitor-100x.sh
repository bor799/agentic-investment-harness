#!/bin/bash
SOURCE_DIR="/Users/murphy/Documents/Obsidian Vault/信息源"
WORK_DIR="/Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/基础概念/ploymarket"
OUTPUT_FILE="$WORK_DIR/100X 萃取内容看板.md"

last_count=0

update_dashboard() {
    (
        echo "# 100X 萃取内容看板"
        echo ""
        echo "> 自动更新于: $(date '+%Y-%m-%d %H:%M:%S')"
        echo ""
        echo "## 统计"
        echo "- 源目录: \`信息源\`"
        echo "- 总文章数: $(find "$SOURCE_DIR" -path "*/2026-03-W*/*.md" -type f 2>/dev/null | wc -l | tr -d ' ') 篇"
        echo ""
        echo "## 最新文章 (Top 100)"
        echo ""
        
        # 扫描所有文章
        find "$SOURCE_DIR" -path "*/2026-03-W*/*.md" -type f 2>/dev/null | while read -r file; do
            stat -f "%m %N" "$file" 2>/dev/null
        done | sort -rn | head -100 | cut -d' ' -f2- | while read -r file; do
            title=$(grep -m1 "^title:" "$file" 2>/dev/null | sed 's/title: //' | sed 's/^"//;s/"$//')
            [ -z "$title" ] && title=$(basename "$file" .md)
            
            summary=$(grep -A1 "一句话归纳" "$file" 2>/dev/null | tail -1 | sed 's/^\*\*//;s/\*\*$//' | sed 's/^- //' | xargs)
            [ -z "$summary" ] && summary="-"
            
            score=$(grep -m1 "^score:" "$file" 2>/dev/null | sed 's/score: //' | xargs)
            [ -n "$score" ] && score=" [$score分]" || score=""
            
            rel_path="${file#$HOME/}"
            echo "- [$title](<$rel_path>)$score $summary"
        done
    ) > "$OUTPUT_FILE"
}

echo "[$(date '+%H:%M:%S')] 监控启动..." >&2

while true; do
    current_count=$(find "$SOURCE_DIR" -path "*/2026-03-W*/*.md" -type f 2>/dev/null | wc -l | tr -d ' ')
    
    if [ "$current_count" -ne "$last_count" ]; then
        echo "[$(date '+%H:%M:%S')] 检测到变化: $last_count → $current_count 篇" >&2
        update_dashboard
        echo "[$(date '+%H:%M:%S')] 看板已更新" >&2
        last_count=$current_count
    fi
    
    sleep 30
done
