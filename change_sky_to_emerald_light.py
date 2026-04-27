import os
import re

# Change Sky Blue to Emerald Light
EMERALD_LIGHT_CSS_VARS = """            --bg-sky: linear-gradient(to bottom right, #f0fdf4, #dcfce7);
            --text-sky: #064e3b;
            --accent-sky: #10b981;"""

EMERALD_LIGHT_RULE = """        [data-theme="sky"] .text-orange-200 { color: var(--accent-sky) !important; }"""

NEW_OPTIONS = """<option value="rose">Reddish Brown</option>
                    <option value="midnight">Midnight Purple</option>
                    <option value="ocean">Ocean Blue</option>
                    <option value="golden">Golden Amber</option>
                    <option value="coffee">Warm Coffee</option>
                    <option value="sunset">Sunset Glow</option>
                    <option value="indigo">Deep Indigo</option>
                    <option value="forest">Forest Deep</option>
                    <option value="chocolate">Chocolate Dark</option>
                    <option value="slate">Slate Minimal</option>
                    <option value="emerald">Emerald Green</option>
                    <option value="dark">Navy Blue</option>
                    <option value="light">Classic Light</option>
                    <option value="sky">Emerald Light</option>"""

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update CSS Variables
    content = content.replace('--bg-sky: linear-gradient(to bottom right, #f0f9ff, #e0f2fe);', '--bg-sky: linear-gradient(to bottom right, #f0fdf4, #dcfce7);')
    content = content.replace('--text-sky: #0c4a6e;', '--text-sky: #064e3b;')
    content = content.replace('--accent-sky: #0369a1;', '--accent-sky: #10b981;')

    # 2. Update Dropdown Label
    if '<select id="theme-selector"' in content:
        content = content.replace('<option value="sky">Sky Blue (Light)</option>', '<option value="sky">Emerald Light</option>')

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Changed Sky Blue to Emerald Light across all pages.")
