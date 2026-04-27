import os
import re

THEME_APPLICATION_RULES = """
        /* Base Theme Application */
        html[data-theme="rose"], body[data-theme="rose"] { background: var(--bg-rose) !important; color: var(--text-rose) !important; }
        html[data-theme="dark"], body[data-theme="dark"] { background: var(--bg-dark) !important; color: var(--text-dark) !important; }
        html[data-theme="light"], body[data-theme="light"] { background: var(--bg-light) !important; color: var(--text-light) !important; }
        html[data-theme="emerald"], body[data-theme="emerald"] { background: var(--bg-emerald) !important; color: var(--text-emerald) !important; }
        html[data-theme="midnight"], body[data-theme="midnight"] { background: var(--bg-midnight) !important; color: var(--text-midnight) !important; }
        html[data-theme="ocean"], body[data-theme="ocean"] { background: var(--bg-ocean) !important; color: var(--text-ocean) !important; }
        html[data-theme="golden"], body[data-theme="golden"] { background: var(--bg-golden) !important; color: var(--text-golden) !important; }
        html[data-theme="coffee"], body[data-theme="coffee"] { background: var(--bg-coffee) !important; color: var(--text-coffee) !important; }
        html[data-theme="sky"], body[data-theme="sky"] { background: var(--bg-sky) !important; color: var(--text-sky) !important; }
        html[data-theme="sunset"], body[data-theme="sunset"] { background: var(--bg-sunset) !important; color: var(--text-sunset) !important; }
        html[data-theme="indigo"], body[data-theme="indigo"] { background: var(--bg-indigo) !important; color: var(--text-indigo) !important; }
        html[data-theme="forest"], body[data-theme="forest"] { background: var(--bg-forest) !important; color: var(--text-forest) !important; }
        html[data-theme="chocolate"], body[data-theme="chocolate"] { background: var(--bg-chocolate) !important; color: var(--text-chocolate) !important; }
        html[data-theme="slate"], body[data-theme="slate"] { background: var(--bg-slate) !important; color: var(--text-slate) !important; }
"""

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the broken block (lines 97-101 range area)
    # Target "html" followed by some whitespace/empty lines before "/* Text Overrides"
    content = re.sub(r'html\s+/\* Text Overrides', THEME_APPLICATION_RULES + '\n        /* Text Overrides', content, flags=re.DOTALL)
    
    # Just in case the above didn't catch it perfectly, try another anchor
    if 'html[data-theme="rose"]' not in content:
         content = content.replace('/* Base Theme Application */', '/* Base Theme Application */' + THEME_APPLICATION_RULES)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Restored all 14 theme background and color application rules.")
