import os
import re

def align_html_cards(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define a consistent min-height for cards
    # For subject/language cards (large)
    large_card_style = 'min-h-[200px] flex items-center justify-center p-8'
    # For chapter cards (medium)
    chapter_card_style = 'min-h-[160px] flex items-center justify-center p-6'

    # Identify if it's index.html or sociology.html (Subject/Language selection)
    if 'index.html' in file_path or (re.search(r'Level 2', content) and not re.search(r'Level 3', content)):
        # Apply larger min-height
        pattern = r'class="glass-card([^"]*)"'
        def replace_large(match):
            classes = match.group(1)
            if 'rounded-2xl' in classes and 'p-' in classes:
                # Replace existing padding and h-full with our consistent style
                new_classes = re.sub(r'p-\d+', '', classes)
                new_classes = re.sub(r'h-full', '', new_classes)
                return f'class="glass-card {large_card_style} {new_classes.strip()}"'
            return match.group(0)
        
        new_content = re.sub(pattern, replace_large, content)
    
    # Identify if it's a chapter page (Level 3)
    elif re.search(r'Level 3', content):
        # Apply chapter min-height
        pattern = r'class="glass-card([^"]*)"'
        def replace_chapter(match):
            classes = match.group(1)
            if 'cursor-pointer' in classes and 'p-' in classes:
                new_classes = re.sub(r'p-\d+', '', classes)
                new_classes = re.sub(r'h-full', '', new_classes)
                return f'class="glass-card {chapter_card_style} {new_classes.strip()}"'
            return match.group(0)
        
        new_content = re.sub(pattern, replace_chapter, content)
    else:
        new_content = content

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# List all html files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

updated_count = 0
for html_file in html_files:
    if align_html_cards(html_file):
        updated_count += 1
        print(f"Updated: {html_file}")

print(f"Total files updated: {updated_count}")
