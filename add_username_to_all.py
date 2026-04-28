import os

files = [
    'history.html', 'history-en.html', 'history-ml.html',
    'world.html', 'world-en.html', 'world-ml.html',
    'kerala.html', 'kerala-en.html', 'kerala-ml.html',
    'politics.html', 'politics-en.html', 'politics-ml.html',
    'economics.html', 'economics-en.html', 'economics-ml.html',
    'philosophy.html', 'philosophy-en.html', 'philosophy-ml.html',
    'ethics.html', 'ethics-en.html', 'ethics-ml.html',
    'sociology.html', 'sociology-en.html', 'sociology-ml.html',
    'micro-economics.html', 'micro-economics-en.html', 'micro-economics-ml.html'
]

# Updated script to inject username display WITH a change option in header (cleaning both keys)
script_inject = """
    <script>
        (function() {
            const name = localStorage.getItem('portal-username');
            if (name) {
                const headerDiv = document.querySelector('header div.flex');
                if (headerDiv) {
                    const nameContainer = document.createElement('div');
                    nameContainer.className = "flex items-center gap-2 px-3 py-1 bg-white/5 rounded-lg border border-white/10 text-[10px] md:text-xs font-bold text-orange-400";
                    nameContainer.innerHTML = `
                        <div class="flex items-center gap-1">
                            <svg class="w-3 h-3" fill="currentColor" viewBox="0 0 20 20"><path d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"></path></svg> 
                            <span>${name}</span>
                        </div>
                        <button onclick="localStorage.removeItem('portal-username'); localStorage.removeItem('portal-userkey'); location.reload();" class="ml-1 text-[8px] text-gray-400 hover:text-white underline uppercase tracking-tighter">Change</button>
                    `;
                    // Insert before the theme selector
                    headerDiv.insertBefore(nameContainer, headerDiv.lastElementChild);
                }
            }
        })();
    </script>
</body>"""

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove old header script if exists (various versions)
        content = content.replace('<script>\n        (function() {\n            const name = localStorage.getItem(\'portal-username\');\n            if (name) {\n                const headerDiv = document.querySelector(\'header div.flex\');\n                if (headerDiv) {\n                    const nameSpan = document.createElement(\'div\');\n                    nameSpan.className = \"hidden md:flex items-center gap-2 px-3 py-1 bg-white/5 rounded-lg border border-white/10 text-xs font-bold text-orange-400\";\n                    nameSpan.innerHTML = `<svg class=\"w-3 h-3\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path d=\"M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z\"></path></svg> ${name}`;\n                    // Insert before the theme selector (which is the last child of headerDiv)\n                    headerDiv.insertBefore(nameSpan, headerDiv.lastElementChild);\n                }\n            }\n        })();\n    </script>', '')
        content = content.replace('<script>\n        (function() {\n            const name = localStorage.getItem(\'portal-username\');\n            if (name) {\n                const headerDiv = document.querySelector(\'header div.flex\');\n                if (headerDiv) {\n                    const nameSpan = document.createElement(\'div\');\n                    nameSpan.className = \"flex items-center gap-2 px-3 py-1 bg-white/5 rounded-lg border border-white/10 text-[10px] md:text-xs font-bold text-orange-400\";\n                    nameSpan.innerHTML = `<svg class=\"w-3 h-3\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path d=\"M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z\"></path></svg> ${name}`;\n                    // Insert before the theme selector (which is the last child of headerDiv)\n                    headerDiv.insertBefore(nameSpan, headerDiv.lastElementChild);\n                }\n            }\n        })();\n    </script>', '')
        # Remove the version without portal-userkey removal
        content = content.replace('<script>\n        (function() {\n            const name = localStorage.getItem(\'portal-username\');\n            if (name) {\n                const headerDiv = document.querySelector(\'header div.flex\');\n                if (headerDiv) {\n                    const nameContainer = document.createElement(\'div\');\n                    nameContainer.className = \"flex items-center gap-2 px-3 py-1 bg-white/5 rounded-lg border border-white/10 text-[10px] md:text-xs font-bold text-orange-400\";\n                    nameContainer.innerHTML = `\n                        <div class=\"flex items-center gap-1\">\n                            <svg class=\"w-3 h-3\" fill=\"currentColor\" viewBox=\"0 0 20 20\"><path d=\"M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z\"></path></svg> \n                            <span>${name}</span>\n                        </div>\n                        <button onclick=\"localStorage.removeItem(\'portal-username\'); location.reload();\" class=\"ml-1 text-[8px] text-gray-400 hover:text-white underline uppercase tracking-tighter\">Change</button>\n                    `;\n                    // Insert before the theme selector\n                    headerDiv.insertBefore(nameContainer, headerDiv.lastElementChild);\n                }\n            }\n        })();\n    </script>', '')

        # Inject new script
        if 'portal-username' not in content:
            new_content = content.replace('</body>', script_inject)
            
            if new_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed change option in header for {filename}")

print("Done")
