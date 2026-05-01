import os
import glob
import re

def fix_links():
    html_files = glob.glob("*.html")
    changes_made = 0
    
    for filepath in html_files:
        content = ""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            try:
                with open(filepath, 'r', encoding='utf-16') as f:
                    content = f.read()
            except Exception as e:
                print(f"Skipping {filepath} due to encoding error: {e}")
                continue
            
        # Replace /edit?usp=sharing with /preview for docs.google.com links
        new_content = re.sub(
            r'(href="https://docs\.google\.com/document/d/[a-zA-Z0-9_-]+)/edit\?usp=sharing"',
            r'\1/preview"',
            content
        )
        
        new_content = re.sub(
            r'(href="https://docs\.google\.com/document/d/[a-zA-Z0-9_-]+)/edit"',
            r'\1/preview"',
            new_content
        )
        
        if content != new_content:
            try:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed links in {filepath}")
                changes_made += 1
            except Exception as e:
                print(f"Error saving {filepath}: {e}")
            
    print(f"Total files updated: {changes_made}")

if __name__ == "__main__":
    fix_links()
