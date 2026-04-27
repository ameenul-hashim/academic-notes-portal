import os
import re

def fix_drive_ids_and_downloads(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Standardize the download link format and REMOVE all whitespace from IDs
    # Pattern to find Drive links
    drive_pattern = r'href="(https://drive\.google\.com/[^"]+)"'
    
    def clean_drive_link(match):
        url = match.group(1)
        # Extract ID
        id_match = re.search(r'id=([a-zA-Z0-9_\-\s]+)(?:&|$)', url)
        if not id_match:
            id_match = re.search(r'/d/([a-zA-Z0-9_\-\s]+)/', url)
        
        if id_match:
            raw_id = id_match.group(1)
            # Remove ALL whitespace from the ID
            clean_id = "".join(raw_id.split())
            
            if 'export=download' in url or 'uc?' in url:
                # Standardize to the most robust download format
                return f'href="https://drive.google.com/u/0/uc?id={clean_id}&export=download"'
            else:
                # Standardize View format
                return f'href="https://drive.google.com/file/d/{clean_id}/view?usp=sharing"'
        return match.group(0)

    new_content = re.sub(drive_pattern, clean_drive_link, content)

    # 2. Re-apply the modal buttons style if the user wants them (they said popup is ok)
    # Actually, they said "popup is ok and view is ok ... downloading time this error is coming"
    # and "change this popup entire to before one".
    # I already reverted to the "before one" (underlined link + glass button).
    # I'll keep that style but ensure it's clean.

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
updated_count = 0
for html_file in html_files:
    if fix_drive_ids_and_downloads(html_file):
        updated_count += 1
        print(f"Fixed Drive IDs: {html_file}")

print(f"Total files updated: {updated_count}")
