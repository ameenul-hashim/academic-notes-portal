import os
import re

REFINED_STYLE = """    <style>
        /* Glassmorphism utility classes */
        .glass-card {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }
        /* Glass button styling */
        .btn-glass {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(5px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }
        .btn-glass:hover {
            background: rgba(255, 255, 255, 0.15);
            border-color: rgba(255, 255, 255, 0.4);
            transform: translateY(-2px);
        }

        /* Theme variables */
        :root {
            --bg-rose: linear-gradient(to bottom right, #450a0a, #881337, #7f1d1d);
            --bg-dark: linear-gradient(to bottom right, #0f172a, #1e293b);
            --bg-light: linear-gradient(to bottom right, #f8fafc, #e2e8f0);
            --bg-emerald: linear-gradient(to bottom right, #064e3b, #065f46);
            
            --text-rose: #fff1f2;
            --text-dark: #f8fafc;
            --text-light: #0f172a;
            --text-emerald: #ecfdf5;

            --accent-rose: #fecdd3;
            --accent-dark: #fde68a;
            --accent-light: #2563eb;
            --accent-emerald: #6ee7b7;

            --card-rose: rgba(255, 255, 255, 0.08);
            --card-dark: rgba(255, 255, 255, 0.05);
            --card-light: rgba(255, 255, 255, 0.7);
            --card-emerald: rgba(255, 255, 255, 0.05);
        }

        /* Base Theme Application */
        html[data-theme="rose"], body[data-theme="rose"] { background: var(--bg-rose) !important; color: var(--text-rose) !important; }
        html[data-theme="dark"], body[data-theme="dark"] { background: var(--bg-dark) !important; color: var(--text-dark) !important; }
        html[data-theme="light"], body[data-theme="light"] { background: var(--bg-light) !important; color: var(--text-light) !important; }
        html[data-theme="emerald"], body[data-theme="emerald"] { background: var(--bg-emerald) !important; color: var(--text-emerald) !important; }

        /* Card Styles */
        [data-theme="rose"] .glass-card { background: var(--card-rose) !important; border-color: rgba(255,255,255,0.2) !important; }
        [data-theme="dark"] .glass-card { background: var(--card-dark) !important; border-color: rgba(255,255,255,0.1) !important; }
        [data-theme="light"] .glass-card { background: var(--card-light) !important; border-color: rgba(0,0,0,0.1) !important; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1) !important; }
        [data-theme="emerald"] .glass-card { background: var(--card-emerald) !important; border-color: rgba(255,255,255,0.1) !important; }

        /* Text Overrides for all themes */
        [data-theme="rose"] .text-white, [data-theme="rose"] .text-gray-100 { color: var(--text-rose) !important; }
        [data-theme="dark"] .text-white, [data-theme="dark"] .text-gray-100 { color: var(--text-dark) !important; }
        [data-theme="light"] .text-white, [data-theme="light"] .text-gray-100, [data-theme="light"] .text-gray-200, [data-theme="light"] .text-gray-300 { color: var(--text-light) !important; }
        [data-theme="emerald"] .text-white, [data-theme="emerald"] .text-gray-100 { color: var(--text-emerald) !important; }

        /* Accent Text (Welcome, Subject, etc.) */
        [data-theme="rose"] .text-orange-200, [data-theme="rose"] .text-pink-200 { color: var(--accent-rose) !important; }
        [data-theme="dark"] .text-orange-200, [data-theme="dark"] .text-pink-200 { color: var(--accent-dark) !important; }
        [data-theme="light"] .text-orange-200, [data-theme="light"] .text-pink-200 { color: var(--accent-light) !important; }
        [data-theme="emerald"] .text-orange-200, [data-theme="emerald"] .text-pink-200 { color: var(--accent-emerald) !important; }

        /* Subtitles and Gray Text */
        [data-theme="rose"] .text-gray-300, [data-theme="rose"] .text-gray-400 { color: #fda4af !important; }
        [data-theme="dark"] .text-gray-300, [data-theme="dark"] .text-gray-400 { color: #94a3b8 !important; }
        [data-theme="light"] .text-gray-300, [data-theme="light"] .text-gray-400, [data-theme="light"] .text-gray-500 { color: #475569 !important; }
        [data-theme="emerald"] .text-gray-300, [data-theme="emerald"] .text-gray-400 { color: #6ee7b7 !important; }

        /* Dropdown visibility fix */
        #theme-selector {
            color: white !important;
            background-color: rgba(0,0,0,0.3) !important;
        }
        #theme-selector option {
            background-color: #1a1a2e !important;
            color: white !important;
        }
        [data-theme="light"] #theme-selector {
            color: #0f172a !important;
            background-color: rgba(255,255,255,0.8) !important;
            border-color: rgba(0,0,0,0.2) !important;
        }
        [data-theme="light"] #theme-selector option {
            background-color: white !important;
            color: #0f172a !important;
        }
    </style>"""

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace existing <style> block
    content = re.sub(r'<style>.*?</style>', REFINED_STYLE, content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Refined theme colors for better readability and style.")
