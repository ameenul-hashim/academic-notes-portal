import os
import re

THEME_SELECTOR_HTML = """<select id="theme-selector" class="bg-black/20 text-white backdrop-blur-md border border-white/10 rounded-lg px-2 py-1 text-xs outline-none cursor-pointer hover:bg-white/20 transition-all">
                    <option value="rose">Rose</option>
                    <option value="dark">Navy</option>
                    <option value="light">Light</option>
                    <option value="emerald">Emerald</option>
                </select>"""

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Remove the old fixed bottom theme selector
    content = re.sub(r'<!-- Theme selector -->.*?</div>\s*<script>\s*\(function\(\)\s*{\s*const selector = document\.getElementById\(\'theme-selector\'\).*?}\)\(\);\s*</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<!-- Theme selector -->.*?</div>', '', content, flags=re.DOTALL)

    # 2. Add selector to header
    if f == 'index.html':
        # Modify index.html header to be flex
        new_header = """    <header class="glass-card sticky top-0 z-50 shadow-lg py-4">
        <div class="max-w-7xl mx-auto px-4 flex items-center justify-between">
            <div class="w-10 md:w-24"></div>
            <div class="text-center">
                <p class="text-sm text-orange-200 tracking-widest uppercase mb-1">Welcome</p>
                <h1 class="font-bold text-xl md:text-3xl tracking-wider text-white">BA History Calicut Unofficial Notes</h1>
            </div>
            <div>
                """ + THEME_SELECTOR_HTML + """
            </div>
        </div>
    </header>"""
        content = re.sub(r'<header class="glass-card sticky top-0 z-50 shadow-lg py-4">.*?</header>', new_header, content, flags=re.DOTALL)
    else:
        # For other pages, replace the empty w-20 div with the selector
        content = content.replace('<div class="w-20"></div>', '<div>\n                ' + THEME_SELECTOR_HTML + '\n            </div>')

    # 3. Ensure the bottom script to handle the selector is present (since we might have removed it in step 1)
    # We need a script that finds the selector and adds the listener
    bottom_script = """    <script>
        (function() {
            const selector = document.getElementById('theme-selector');
            const savedTheme = localStorage.getItem('preferred-theme') || 'rose';
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
    
    # Remove any old bottom scripts if they exist
    content = re.sub(r'<script>\s*\(function\(\)\s*{\s*const selector = document\.getElementById\(\'theme-selector\'\).*?}\)\(\);\s*</script>', '', content, flags=re.DOTALL)
    
    if bottom_script not in content:
        content = content.replace('</body>', bottom_script + '\n</body>')

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Moved theme selector to header and added hover effects.")
