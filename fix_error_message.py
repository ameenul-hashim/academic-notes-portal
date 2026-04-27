import os
import re

def update_error_message(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for the "Coming Soon" description
    old_line = "Our team is currently preparing these notes in reddish brown style for you."
    new_line = "Our team is currently preparing these notes."

    if old_line in content:
        new_content = content.replace(old_line, new_line)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
updated_count = 0
for html_file in html_files:
    if update_error_message(html_file):
        updated_count += 1
        print(f"Updated Error Message: {html_file}")

print(f"Total files updated: {updated_count}")
