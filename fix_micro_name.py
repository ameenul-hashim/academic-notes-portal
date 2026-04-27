import os
import re

# Fix "Micro Economic Foundations Foundations" or "Micro Economics Foundations"
# Final target: "Micro Economic Foundations"

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Clean up potential double foundations
    content = content.replace("Foundations Foundations", "Foundations")
    content = content.replace("foundations foundations", "foundations")
    
    # 2. Ensure "Micro Economic Foundations" (singular Economic)
    content = content.replace("Micro Economics Foundations", "Micro Economic Foundations")
    content = content.replace("Micro economics foundations", "Micro economic foundations")
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Fixed Micro Economic Foundations naming.")
