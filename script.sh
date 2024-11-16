tree -L 1 -f | while read line; do
    if [[ -f "$line" ]]; then
        cloc "$line"
    fi
done