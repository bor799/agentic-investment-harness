#!/bin/bash
# 100X 监控脚本 - 自动同步萃取内容到看板

SOURCE_DIR="/Users/murphy/Documents/Obsidian Vault/信息源"
TARGET_DIR="/Users/murphy/Documents/Obsidian Vault/兴趣领域/股票投资/基础概念/ploymarket"
INDEX_FILE="$TARGET_DIR/100X 萃取看板.md"
STATE_FILE="$TARGET_DIR/.100x-state"

# 初始化状态文件
init_state() {
    touch "$STATE_FILE"
}

# 获取所有已处理的文件
get_processed_files() {
    if [ -f "$STATE_FILE" ]; then
        cat "$STATE_FILE"
    fi
}

# 检查新文件
check_new_files() {
    local new_files=()
    while IFS= read -r -d '' file; do
        local basename=$(basename "$file")
        if ! grep -qx "$basename" "$STATE_FILE" 2>/dev/null; then
            new_files+=("$file")
        fi
    done < <(find "$SOURCE_DIR" -type f -name "*.md" -print0 2>/dev/null | grep -v "\.DS_Store" | sort -z)

    printf '%s\n' "${new_files[@]}"
}

# 提取 frontmatter 字段
extract_field() {
    local file="$1"
    local field="$2"
    grep -m1 "^$field:" "$file" | sed "s/^$field: *//; s/^\"//; s/\"$//"
}

# 生成一句话概括
generate_summary() {
    local file="$1"
    # 尝试提取第一个段落或高亮
    awk '/^---/{flag++;if(flag==2)exit;next} flag>0{if(NF>0){print;exit}}' "$file" | head -c 150
}

# 更新看板
update_dashboard() {
    local new_files=("$@")

    # 创建看板头部
    cat > "$INDEX_FILE" << 'EOF'
# 100X 知识萃取看板

> 📁 原目录：[[../../../../信息源|信息源]]
>
> 🔄 最后更新：`date +%Y-%m-%d %H:%M:%S`

## 📋 内容索引

| 📄 标题 | 💡 概括 | 🔗 跳转 |
|---------|---------|---------|
EOF

    # 如果有新文件，添加到看板
    for file in "${new_files[@]}"; do
        local basename=$(basename "$file")
        local title=$(extract_field "$file" "title" | head -c 80)
        local summary=$(generate_summary "$file" | tr '\n' ' ' | head -c 100)
        local rel_path="${file#$HOME/Documents/Obsidian Vault/}"
        local week_dir=$(echo "$rel_path" | grep -oE '202[0-9]-[0-9]{2}-W[0-9]')

        if [ -z "$title" ]; then
            title="${basename%.md}"
        fi
        if [ -z "$summary" ]; then
            summary="暂无概括"
        fi

        # 转义特殊字符
        title=$(echo "$title" | sed 's/|/\\|/g')
        summary=$(echo "$summary" | sed 's/|/\\|/g')

        echo "| [$title](${rel_path}) | $summary | 🔗 |" >> "$INDEX_FILE"

        # 记录已处理
        echo "$basename" >> "$STATE_FILE"
    done

    # 添加统计信息
    local total=$(find "$SOURCE_DIR" -type f -name "*.md" 2>/dev/null | grep -v "\.DS_Store" | wc -l | tr -d ' ')
    local processed=$(wc -l < "$STATE_FILE" 2>/dev/null || echo 0)

    cat >> "$INDEX_FILE" << EOF

---

## 📊 统计

| 指标 | 数量 |
|------|------|
| 总文件数 | $total |
| 已索引 | $processed |
| 今日新增 | ${#new_files[@]} |

EOF
}

# 主循环
main() {
    cd "$TARGET_DIR" || exit 1

    init_state

    while true; do
        echo "🔍 $(date '+%Y-%m-%d %H:%M:%S') - 检查新文件..."

        # 使用临时文件存储新文件列表
        local tmp_file=$(mktemp)
        check_new_files > "$tmp_file"
        local count=$(wc -l < "$tmp_file" | tr -d ' ')

        if [ "$count" -gt 0 ]; then
            echo "✅ 发现 $count 个新文件，更新看板..."
            # 将文件作为参数传递给 update_dashboard
            update_dashboard $(cat "$tmp_file")
            echo "📝 看板已更新: $INDEX_FILE"
        else
            echo "⏸️  无新文件"
        fi

        rm -f "$tmp_file"

        # 每30秒检查一次
        sleep 30
    done
}

# 运行
main
