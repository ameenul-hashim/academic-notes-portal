import os
import re

MASTER_STYLE = """    <style>
        /* Modern Glassmorphism System */
        .glass-card {
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        /* Theme Definitions */
        :root {
            --bg-rose: linear-gradient(135deg, #450a0a 0%, #881337 50%, #7f1d1d 100%);
            --bg-midnight: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #2e1065 100%);
            --bg-ocean: linear-gradient(135deg, #083344 0%, #155e75 50%, #164e63 100%);
            --bg-golden: linear-gradient(135deg, #451a03 0%, #78350f 50%, #92400e 100%);
            --bg-coffee: linear-gradient(135deg, #1c1917 0%, #44403c 50%, #292524 100%);
            --bg-sunset: linear-gradient(135deg, #7c2d12 0%, #9d174d 50%, #be123c 100%);
            --bg-indigo: linear-gradient(135deg, #1e1b4b 0%, #312e81 50%, #3730a3 100%);
            --bg-forest: linear-gradient(135deg, #064e3b 0%, #14532d 50%, #065f46 100%);
            --bg-chocolate: linear-gradient(135deg, #1c1917 0%, #3b2b07 50%, #451a03 100%);
            --bg-slate: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
            --bg-emerald: linear-gradient(135deg, #064e3b 0%, #065f46 50%, #047857 100%);
            --bg-dark: linear-gradient(135deg, #020617 0%, #0f172a 50%, #1e293b 100%);
            --bg-light: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 50%, #e2e8f0 100%);
            --bg-desert: linear-gradient(135deg, #fffbeb 0%, #fef3c7 50%, #fde68a 100%);
        }

        /* Global Theme Application */
        html, body {
            min-height: 100vh !important;
            margin: 0 !important;
            padding: 0 !important;
            background-attachment: fixed !important;
        }

        [data-theme="rose"] { background: var(--bg-rose) !important; color: #fff1f2 !important; }
        [data-theme="midnight"] { background: var(--bg-midnight) !important; color: #f5f3ff !important; }
        [data-theme="ocean"] { background: var(--bg-ocean) !important; color: #ecfeff !important; }
        [data-theme="golden"] { background: var(--bg-golden) !important; color: #fffbeb !important; }
        [data-theme="coffee"] { background: var(--bg-coffee) !important; color: #fafaf9 !important; }
        [data-theme="sunset"] { background: var(--bg-sunset) !important; color: #fff7ed !important; }
        [data-theme="indigo"] { background: var(--bg-indigo) !important; color: #e0e7ff !important; }
        [data-theme="forest"] { background: var(--bg-forest) !important; color: #f0fdf4 !important; }
        [data-theme="chocolate"] { background: var(--bg-chocolate) !important; color: #fffbeb !important; }
        [data-theme="slate"] { background: var(--bg-slate) !important; color: #f1f5f9 !important; }
        [data-theme="emerald"] { background: var(--bg-emerald) !important; color: #ecfdf5 !important; }
        [data-theme="dark"] { background: var(--bg-dark) !important; color: #f8fafc !important; }
        [data-theme="light"] { background: var(--bg-light) !important; color: #0f172a !important; }
        [data-theme="sky"] { background: var(--bg-desert) !important; color: #451a03 !important; }

        /* Card Visibility Fix */
        .glass-card {
            background: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
        }
        [data-theme="light"] .glass-card, [data-theme="sky"] .glass-card {
            background: rgba(255, 255, 255, 0.7) !important;
            border: 1px solid rgba(0, 0, 0, 0.1) !important;
            box-shadow: 0 8px 32px rgba(0,0,0,0.1) !important;
        }

        /* Text Overrides */
        [data-theme="light"] .text-white, [data-theme="light"] .text-gray-100, [data-theme="light"] .text-orange-200 { color: #0f172a !important; }
        [data-theme="sky"] .text-white, [data-theme="sky"] .text-gray-100, [data-theme="sky"] .text-orange-200 { color: #451a03 !important; }

        /* Header Dropdown Fix */
        #theme-selector {
            background: rgba(0,0,0,0.5) !important;
            color: white !important;
            border: 1px solid rgba(255,255,255,0.2) !important;
        }
        #theme-selector option {
            background: #1e293b !important;
            color: white !important;
        }
        [data-theme="light"] #theme-selector, [data-theme="sky"] #theme-selector {
            background: rgba(255,255,255,0.8) !important;
            color: #0f172a !important;
            border: 1px solid rgba(0,0,0,0.1) !important;
        }
        [data-theme="light"] #theme-selector option, [data-theme="sky"] #theme-selector option {
            background: white !important;
            color: #0f172a !important;
        }
    </style>"""

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Complete style block replacement
    content = re.sub(r'<style>.*?</style>', MASTER_STYLE, content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Applied Master Theme Fix across all pages.")
