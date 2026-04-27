import os
import re

def clean_and_align_globally(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Clean up duplicated classes in glass-card
    # e.g. flex items-center justify-center appearing multiple times
    pattern = r'class="glass-card ([^"]*)"'
    def clean_classes(match):
        classes = match.group(1).split()
        seen = set()
        cleaned = []
        for c in classes:
            if c not in seen:
                cleaned.append(c)
                seen.add(c)
        return f'class="glass-card {" ".join(cleaned)}"'
    
    new_content = re.sub(pattern, clean_classes, content)

    # 2. Enforce consistent heights
    # Subject/Language cards: h-64
    # Chapter cards: h-48
    
    # Identify context
    is_chapter_page = re.search(r'Level 3', content)
    is_index_or_lang = 'index.html' in file_path or (re.search(r'Level 2', content) and not is_chapter_page)

    if is_index_or_lang:
        # Subject/Language Selection cards
        pattern_sl = r'class="glass-card ([^"]*rounded-2xl[^"]*)"'
        def fix_sl(match):
            cls = match.group(1)
            cls = re.sub(r'min-h-\[?\d+px\]?', '', cls)
            cls = re.sub(r'h-\d+', '', cls)
            return f'class="glass-card h-64 {cls.strip()}"'
        new_content = re.sub(pattern_sl, fix_sl, new_content)
    
    if is_chapter_page:
        # Chapter cards
        pattern_ch = r'class="glass-card ([^"]*cursor-pointer[^"]*)"'
        def fix_ch(match):
            cls = match.group(1)
            cls = re.sub(r'h-\d+', '', cls)
            return f'class="glass-card h-48 {cls.strip()}"'
        new_content = re.sub(pattern_ch, fix_ch, new_content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
updated_count = 0
for html_file in html_files:
    if clean_and_align_globally(html_file):
        updated_count += 1
        print(f"Cleaned & Aligned: {html_file}")

print(f"Total files updated: {updated_count}")
