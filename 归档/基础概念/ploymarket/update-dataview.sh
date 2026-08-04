#!/bin/bash

SOURCE_DIR="$HOME/Documents/Obsidian Vault/信息源/AI进展"
TARGET_DIR="$HOME/Documents/Obsidian Vault/兴趣领域/股票投资/基础概念/ploymarket"
DASHBOARD_FILE="$TARGET_DIR/100X 萃取内容看板.md"

# 生成看板内容
generate_dashboard() {
    echo "---"
    echo "dataview"
    echo "---"
    echo ""
    echo "# 100X 萃取内容看板"
    echo ""
    echo "> 自动更新于: $(date '+%Y-%m-%d %H:%M:%S')"
    echo ""
    echo "## 萃取列表"
    echo ""
    echo "|文件名|一句话概括|操作|"
    echo "|---|---|---|"
    
    count=0
    # 使用递归查找，限制数量
    find "$SOURCE_DIR" -name "*.md" -type f 2>/dev/null | while IFS= read -r file; do
        [ "$count" -ge 100 ] && break
        [ ! -f "$file" ] && continue
        
        filename=$(basename "$file" .md)
        rel_path="${file#$HOME/Documents/Obsidian Vault/}"
        
        # 提取一句话概括
        summary=$(grep -A 1 "## 核心洞察" "$file" 2>/dev/null | tail -1 | head -c 80 | tr '\n' ' ')
        [ -z "$summary" ] && summary="暂无概括"
        
        # 转义表格字符
        summary=$(echo "$summary" | sed 's/|/\\|/g')
        
        echo "|[\`$filename\`]($rel_path)|$summary|[🔗 查看]($rel_path)|"
        count=$((count + 1))
    done
    
    echo ""
    echo "---"
    echo ""
    echo "**统计**: 共 $count 篇萃取文章"
}

generate_dashboard > "$DASHBOARD_FILE"
echo "✅ 看板已更新: $(date '+%H:%M:%S')"
