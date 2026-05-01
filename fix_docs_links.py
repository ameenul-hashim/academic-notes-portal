import os
import glob
import re

def fix_links():
    html_files = glob.glob("*.html")
    changes_made = 0
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace /edit?usp=sharing with /preview for docs.google.com links
        # specifically inside href attributes
        new_content = re.sub(
            r'(href="https://docs\.google\.com/document/d/[a-zA-Z0-9_-]+)/edit\?usp=sharing"',
            r'\1/preview"',
            content
        )
        
        # Also just in case they don't have ?usp=sharing
        new_content = re.sub(
            r'(href="https://docs\.google\.com/document/d/[a-zA-Z0-9_-]+)/edit"',
            r'\1/preview"',
            new_content
        )
        
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed links in {filepath}")
            changes_made += 1
            
    print(f"Total files updated: {changes_made}")

if __name__ == "__main__":
    fix_links()
