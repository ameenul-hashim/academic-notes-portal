import os
import re

def align_chapters_4col(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Only process Level 3 (Chapter) pages
    if not re.search(r'Level 3', content):
        return False

    # 1. Update grid to 4 columns
    new_content = re.sub(
        r'grid-cols-1 sm:grid-cols-2 lg:grid-cols-3',
        'grid-cols-1 sm:grid-cols-2 lg:grid-cols-4',
        content
    )

    # 2. Ensure all chapter cards have the same height and width (Rectangular)
    # We already have h-40 from the previous step. Let's make sure it's consistent.
    # Pattern: glass-card h-40 ... cursor-pointer
    
    # We'll re-apply h-40 to all cursor-pointer cards on these pages.
    pattern_card = r'class="glass-card ([^"]*?cursor-pointer[^"]*?)"'
    def fix_ch_card(match):
        cls = match.group(1)
        cls = re.sub(r'h-\d+', '', cls)
        cls = re.sub(r'min-h-\[?\d+px\]?', '', cls)
        return f'class="glass-card h-40 flex items-center justify-center p-6 {cls.strip()}"'

    new_content = re.sub(pattern_card, fix_ch_card, new_content)

    # 3. Cleanup redundant flex classes
    pattern_clean = r'class="glass-card ([^"]*)"'
    def clean_classes(match):
        classes = match.group(1).split()
        seen = set()
        cleaned = []
        for c in classes:
            if c not in seen:
                cleaned.append(c)
                seen.add(c)
        return f'class="glass-card {" ".join(cleaned)}"'
    
    new_content = re.sub(pattern_clean, clean_classes, new_content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
updated_count = 0
for html_file in html_files:
    if align_chapters_4col(html_file):
        updated_count += 1
        print(f"Aligned Chapter Page: {html_file}")

print(f"Total files updated: {updated_count}")
