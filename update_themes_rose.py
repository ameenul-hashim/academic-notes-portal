import os
import re

# Reddish Brown Theme (Rose)
ROSE_CSS_VARS = """            --bg-rose: linear-gradient(to bottom right, #450a0a, #881337, #7f1d1d);
            --text-rose: #f8f9fa;
            --card-bg-rose: rgba(255,255,255,0.1);
            --card-border-rose: rgba(255,255,255,0.2);"""

ROSE_CSS_RULES = """        html[data-theme="rose"], body[data-theme="rose"] {
            background: var(--bg-rose) !important;
            color: var(--text-rose) !important;
        }
        [data-theme="rose"] .glass-card { background: var(--card-bg-rose) !important; border-color: var(--card-border-rose) !important; }"""

CSS_CONTENT = """    <style>
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
            --bg-light: linear-gradient(to bottom right, #f0f5ff, #e0eaff);
            --bg-dark: linear-gradient(to bottom right, #1a1a2e, #16213e);
            --bg-rose: linear-gradient(to bottom right, #450a0a, #881337, #7f1d1d);
            --bg-emerald: linear-gradient(to bottom right, #e0f7e9, #c2efd9);
            --text-light: #212529;
            --text-dark: #f8f9fa;
            --text-rose: #f8f9fa;
            --text-emerald: #0a3b1c;
            --card-bg-light: rgba(255,255,255,0.6);
            --card-bg-dark: rgba(0,0,0,0.3);
            --card-bg-rose: rgba(255,255,255,0.1);
            --card-bg-emerald: rgba(255,255,255,0.5);
            --card-border-light: rgba(0,0,0,0.1);
            --card-border-dark: rgba(255,255,255,0.1);
            --card-border-rose: rgba(255,255,255,0.2);
            --card-border-emerald: rgba(6,78,59,0.2);
        }

        /* Theme rules applying to html and body */
        html[data-theme="light"], body[data-theme="light"] { background: var(--bg-light) !important; color: var(--text-light) !important; }
        html[data-theme="dark"], body[data-theme="dark"] { background: var(--bg-dark) !important; color: var(--text-dark) !important; }
        html[data-theme="rose"], body[data-theme="rose"] { background: var(--bg-rose) !important; color: var(--text-rose) !important; }
        html[data-theme="emerald"], body[data-theme="emerald"] { background: var(--bg-emerald) !important; color: var(--text-emerald) !important; }
        
        [data-theme="light"] .glass-card { background: var(--card-bg-light) !important; border-color: var(--card-border-light) !important; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05) !important; }
        [data-theme="dark"] .glass-card { background: var(--card-bg-dark) !important; border-color: var(--card-border-dark) !important; }
        [data-theme="rose"] .glass-card { background: var(--card-bg-rose) !important; border-color: var(--card-border-rose) !important; }
        [data-theme="emerald"] .glass-card { background: var(--card-bg-emerald) !important; border-color: var(--card-border-emerald) !important; box-shadow: 0 4px 6px -1px rgba(6, 78, 59, 0.05) !important; }

        /* Text Color Overrides for Tailwind classes */
        [data-theme="light"] .text-white, [data-theme="light"] .text-gray-100, [data-theme="light"] .text-gray-200, [data-theme="light"] .text-gray-300 { color: var(--text-light) !important; }
        [data-theme="emerald"] .text-white, [data-theme="emerald"] .text-gray-100, [data-theme="emerald"] .text-gray-200, [data-theme="emerald"] .text-gray-300 { color: var(--text-emerald) !important; }
        
        /* Accent colors to adapt to themes */
        [data-theme="light"] .text-orange-200, [data-theme="light"] .text-pink-200, [data-theme="light"] .text-orange-300, [data-theme="light"] .text-pink-300 { color: #b45309 !important; }
        [data-theme="emerald"] .text-orange-200, [data-theme="emerald"] .text-pink-200, [data-theme="emerald"] .text-orange-300, [data-theme="emerald"] .text-pink-300 { color: #047857 !important; }

        /* Specific background overrides like bg-white/5 */
        [data-theme="light"] .bg-white\/5, [data-theme="light"] .bg-white\/10 { background-color: rgba(0,0,0,0.05) !important; }
        [data-theme="emerald"] .bg-white\/5, [data-theme="emerald"] .bg-white\/10 { background-color: rgba(6,78,59,0.05) !important; }

        /* Border overrides */
        [data-theme="light"] .border-white\/20, [data-theme="light"] .border-white\/10 { border-color: rgba(0,0,0,0.1) !important; }
        [data-theme="emerald"] .border-white\/20, [data-theme="emerald"] .border-white\/10 { border-color: rgba(6,78,59,0.1) !important; }

        /* Hover effects */
        [data-theme="light"] .hover\:text-white:hover { color: #000 !important; }
        [data-theme="emerald"] .hover\:text-white:hover { color: #022c22 !important; }

        /* Link colors */
        [data-theme="light"] a.text-orange-300 { color: #2563eb !important; }
        [data-theme="emerald"] a.text-orange-300 { color: #047857 !important; }
    </style>"""

HEAD_SCRIPT = """    <script>
        (function() {
            const savedTheme = localStorage.getItem('preferred-theme') || 'rose';
            document.documentElement.setAttribute('data-theme', savedTheme);
        })();
    </script>"""

THEME_JS_WITH_DROPDOWN = """    <!-- Theme selector -->
    <div class="fixed bottom-4 right-4 z-50">
        <select id="theme-selector" class="bg-black/60 text-white backdrop-blur-md border border-white/20 rounded-lg px-3 py-2 outline-none cursor-pointer hover:bg-black/80 transition-colors shadow-lg">
            <option value="rose">Reddish Brown (Default)</option>
            <option value="dark">Dark Navy</option>
            <option value="light">Light Theme</option>
            <option value="emerald">Emerald Theme</option>
        </select>
    </div>

    <script>
        (function() {
            const selector = document.getElementById('theme-selector');
            const savedTheme = localStorage.getItem('preferred-theme') || 'rose';
            document.documentElement.setAttribute('data-theme', savedTheme);
            if (selector) {
                selector.value = savedTheme;
                selector.addEventListener('change', (e) => {
                    const theme = e.target.value;
                    document.documentElement.setAttribute('data-theme', theme);
                    localStorage.setItem('preferred-theme', theme);
                });
            }
        })();
    </script>"""

THEME_JS_NO_DROPDOWN = """    <script>
        (function() {
            const savedTheme = localStorage.getItem('preferred-theme') || 'rose';
            document.documentElement.setAttribute('data-theme', savedTheme);
        })();
    </script>"""

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove any existing style/script/dropdown blocks from my previous actions
    content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*\(function\(\)\s*{\s*const savedTheme = localStorage\.getItem\(\'preferred-theme\'\).*?}\)\(\);\s*</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- Theme selector -->.*?localStorage\.setItem\(\'preferred-theme\', theme\);.*?}\)\(\);\s*</script>', '', content, flags=re.DOTALL)
    
    # Add new CSS and Head Script
    content = content.replace('</head>', CSS_CONTENT + '\n' + HEAD_SCRIPT + '</head>')
    
    # Add Bottom JS
    if f == 'index.html':
        content = content.replace('</body>', THEME_JS_WITH_DROPDOWN + '</body>')
    else:
        content = content.replace('</body>', THEME_JS_NO_DROPDOWN + '</body>')

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Updated themes to include Reddish Brown (Rose) as default.")
