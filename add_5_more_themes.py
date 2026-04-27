import os
import re

# Define the 5 new themes
# 1. Midnight (Purple)
# 2. Ocean (Teal)
# 3. Golden (Amber)
# 4. Coffee (Brown)
# 5. Sky (Light Blue - Light Theme)

NEW_THEMES_CSS_VARS = """            --bg-midnight: linear-gradient(to bottom right, #2e1065, #4c1d95);
            --bg-ocean: linear-gradient(to bottom right, #083344, #155e75);
            --bg-golden: linear-gradient(to bottom right, #451a03, #78350f);
            --bg-coffee: linear-gradient(to bottom right, #1c1917, #44403c);
            --bg-sky: linear-gradient(to bottom right, #f0f9ff, #e0f2fe);
            
            --text-midnight: #f5f3ff;
            --text-ocean: #ecfeff;
            --text-golden: #fffbeb;
            --text-coffee: #fafaf9;
            --text-sky: #0c4a6e;

            --accent-midnight: #ddd6fe;
            --accent-ocean: #a5f3fc;
            --accent-golden: #fde68a;
            --accent-coffee: #e7e5e4;
            --accent-sky: #0369a1;"""

NEW_THEMES_RULES = """        html[data-theme="midnight"], body[data-theme="midnight"] { background: var(--bg-midnight) !important; color: var(--text-midnight) !important; }
        html[data-theme="ocean"], body[data-theme="ocean"] { background: var(--bg-ocean) !important; color: var(--text-ocean) !important; }
        html[data-theme="golden"], body[data-theme="golden"] { background: var(--bg-golden) !important; color: var(--text-golden) !important; }
        html[data-theme="coffee"], body[data-theme="coffee"] { background: var(--bg-coffee) !important; color: var(--text-coffee) !important; }
        html[data-theme="sky"], body[data-theme="sky"] { background: var(--bg-sky) !important; color: var(--text-sky) !important; }

        [data-theme="midnight"] .glass-card { background: rgba(255,255,255,0.05) !important; border-color: rgba(255,255,255,0.1) !important; }
        [data-theme="ocean"] .glass-card { background: rgba(255,255,255,0.05) !important; border-color: rgba(255,255,255,0.1) !important; }
        [data-theme="golden"] .glass-card { background: rgba(255,255,255,0.05) !important; border-color: rgba(255,255,255,0.1) !important; }
        [data-theme="coffee"] .glass-card { background: rgba(255,255,255,0.05) !important; border-color: rgba(255,255,255,0.1) !important; }
        [data-theme="sky"] .glass-card { background: rgba(255,255,255,0.7) !important; border-color: rgba(0,0,0,0.1) !important; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1) !important; }

        [data-theme="midnight"] .text-orange-200 { color: var(--accent-midnight) !important; }
        [data-theme="ocean"] .text-orange-200 { color: var(--accent-ocean) !important; }
        [data-theme="golden"] .text-orange-200 { color: var(--accent-golden) !important; }
        [data-theme="coffee"] .text-orange-200 { color: var(--accent-coffee) !important; }
        [data-theme="sky"] .text-orange-200 { color: var(--accent-sky) !important; }
"""

NEW_OPTIONS = """<option value="rose">Reddish Brown</option>
                    <option value="midnight">Midnight Purple</option>
                    <option value="ocean">Ocean Blue</option>
                    <option value="golden">Golden Amber</option>
                    <option value="coffee">Warm Coffee</option>
                    <option value="emerald">Emerald Green</option>
                    <option value="dark">Navy Blue</option>
                    <option value="light">Classic Light</option>
                    <option value="sky">Sky Blue (Light)</option>"""

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Add CSS Variables
    if '--bg-midnight' not in content:
        content = content.replace('--bg-emerald: linear-gradient(to bottom right, #064e3b, #065f46);', '--bg-emerald: linear-gradient(to bottom right, #064e3b, #065f46);\n' + NEW_THEMES_CSS_VARS)
    
    # 2. Add Theme Rules
    if 'data-theme="midnight"' not in content:
        content = content.replace('html[data-theme="emerald"], body[data-theme="emerald"] { background: var(--bg-emerald) !important; color: var(--text-emerald) !important; }', 'html[data-theme="emerald"], body[data-theme="emerald"] { background: var(--bg-emerald) !important; color: var(--text-emerald) !important; }\n' + NEW_THEMES_RULES)

    # 3. Update Dropdown Options (only on pages that have it)
    if '<select id="theme-selector"' in content:
        content = re.sub(r'<option value="rose">.*?</select>', NEW_OPTIONS + '\n                </select>', content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Added 5 more theme options across all pages.")
