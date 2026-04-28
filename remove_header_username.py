import os
import re

files = [
    'history.html', 'history-en.html', 'history-ml.html',
    'world.html', 'world-en.html', 'world-ml.html',
    'kerala.html', 'kerala-en.html', 'kerala-ml.html',
    'politics.html', 'politics-en.html', 'politics-ml.html',
    'economics.html', 'economics-en.html', 'economics-ml.html',
    'philosophy.html', 'philosophy-en.html', 'philosophy-ml.html',
    'ethics.html', 'ethics-en.html', 'ethics-ml.html',
    'sociology.html', 'sociology-en.html', 'sociology-ml.html',
    'micro-economics.html', 'micro-economics-en.html', 'micro-economics-ml.html'
]

# Script to REMOVE the header/sub-header username display
for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove any version of the username display script
        new_content = re.sub(r'<script>\s*\(function\(\) \{\s*const name = localStorage\.getItem\(\'portal-username\'\);[\s\S]*?<\/script>', '', content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Removed header username display from {filename}")

print("Done")
