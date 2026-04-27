import os
import re

# Correct Subject Names and Pluralization
NAME_UPDATES = {
    "Fundamental of Ethics": "Fundamentals of Ethics",
    "fundamental of ethics": "fundamentals of ethics",
}

# Mapping of file to intended name (based on previous edits and typical academic portal structure)
# We will pluralize Ethics and ensure names are correct in index.html and individual pages.

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Pluralize Fundamental(s) of Ethics
    content = content.replace('Fundamental of Ethics', 'Fundamentals of Ethics')
    content = content.replace('fundamental of ethics', 'fundamentals of ethics')
    
    # 2. Fix Page Titles if they contain "Fundamental"
    content = re.sub(r'Fundamental of Ethics', 'Fundamentals of Ethics', content)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Pluralized 'Fundamentals of Ethics' across all files.")
