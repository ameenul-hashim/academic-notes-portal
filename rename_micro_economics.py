import os
import re

# Rename Micro Economics to Micro Economics Foundations
OLD_NAME = "Micro Economics"
NEW_NAME = "Micro Economics Foundations"

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the name
    content = content.replace(OLD_NAME, NEW_NAME)
    content = content.replace(OLD_NAME.lower(), NEW_NAME.lower())
    
    # Fix Page Titles if they contain the old name
    content = re.sub(OLD_NAME, NEW_NAME, content)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Renamed '{OLD_NAME}' to '{NEW_NAME}' across all files.")
