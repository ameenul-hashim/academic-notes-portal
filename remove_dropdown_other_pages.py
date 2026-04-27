import os
import re

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html') and f != 'index.html']

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove the dropdown HTML from non-index pages, but KEEP the script that applies the theme
    content = re.sub(
        r'<div class="fixed bottom-4 right-4 z-50">\s*<select id="theme-selector".*?</select>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Removed dropdown UI from other pages, kept it only on index.html.")
