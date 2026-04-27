import os
import re

# Adding 5 more themes: Sunset, Indigo, Forest, Chocolate, Slate
V2_THEMES_CSS_VARS = """            --bg-sunset: linear-gradient(to bottom right, #7c2d12, #9d174d);
            --bg-indigo: linear-gradient(to bottom right, #312e81, #1e1b4b);
            --bg-forest: linear-gradient(to bottom right, #064e3b, #14532d);
            --bg-chocolate: linear-gradient(to bottom right, #3b2b07, #1c1917);
            --bg-slate: linear-gradient(to bottom right, #334155, #0f172a);
            
            --text-sunset: #fff7ed;
            --text-indigo: #e0e7ff;
            --text-forest: #f0fdf4;
            --text-chocolate: #fffbeb;
            --text-slate: #f1f5f9;

            --accent-sunset: #fdba74;
            --accent-indigo: #818cf8;
            --accent-forest: #4ade80;
            --accent-chocolate: #d97706;
            --accent-slate: #94a3b8;"""

V2_THEMES_RULES = """        html[data-theme="sunset"], body[data-theme="sunset"] { background: var(--bg-sunset) !important; color: var(--text-sunset) !important; }
        html[data-theme="indigo"], body[data-theme="indigo"] { background: var(--bg-indigo) !important; color: var(--text-indigo) !important; }
        html[data-theme="forest"], body[data-theme="forest"] { background: var(--bg-forest) !important; color: var(--text-forest) !important; }
        html[data-theme="chocolate"], body[data-theme="chocolate"] { background: var(--bg-chocolate) !important; color: var(--text-chocolate) !important; }
        html[data-theme="slate"], body[data-theme="slate"] { background: var(--bg-slate) !important; color: var(--text-slate) !important; }

        [data-theme="sunset"] .glass-card { background: rgba(255,255,255,0.05) !important; border-color: rgba(255,255,255,0.1) !important; }
        [data-theme="indigo"] .glass-card { background: rgba(255,255,255,0.05) !important; border-color: rgba(255,255,255,0.1) !important; }
        [data-theme="forest"] .glass-card { background: rgba(255,255,255,0.05) !important; border-color: rgba(255,255,255,0.1) !important; }
        [data-theme="chocolate"] .glass-card { background: rgba(255,255,255,0.05) !important; border-color: rgba(255,255,255,0.1) !important; }
        [data-theme="slate"] .glass-card { background: rgba(255,255,255,0.05) !important; border-color: rgba(255,255,255,0.1) !important; }

        [data-theme="sunset"] .text-orange-200 { color: var(--accent-sunset) !important; }
        [data-theme="indigo"] .text-orange-200 { color: var(--accent-indigo) !important; }
        [data-theme="forest"] .text-orange-200 { color: var(--accent-forest) !important; }
        [data-theme="chocolate"] .text-orange-200 { color: var(--accent-chocolate) !important; }
        [data-theme="slate"] .text-orange-200 { color: var(--accent-slate) !important; }
"""

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
                    <option value="sky">Sky Blue (Light)</option>"""

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Add CSS Variables
    if '--bg-sunset' not in content:
        content = content.replace('--accent-sky: #0369a1;', '--accent-sky: #0369a1;\n' + V2_THEMES_CSS_VARS)
    
    # 2. Add Theme Rules
    if 'data-theme="sunset"' not in content:
        content = content.replace('[data-theme="sky"] .text-orange-200 { color: var(--accent-sky) !important; }', '[data-theme="sky"] .text-orange-200 { color: var(--accent-sky) !important; }\n' + V2_THEMES_RULES)

    # 3. Update Dropdown Options
    if '<select id="theme-selector"' in content:
        content = re.sub(r'<option value="rose">.*?</select>', NEW_OPTIONS + '\n                </select>', content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Added ANOTHER 5 theme options (Total 14 now).")
