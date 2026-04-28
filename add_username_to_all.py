import os
import re

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

# Script to move username display UNDER the header and remove sticky behavior
script_inject = """
    <script>
        (function() {
            const name = localStorage.getItem('portal-username');
            const header = document.querySelector('header');
            if (header) {
                // Remove sticky and z-index as requested
                header.classList.remove('sticky', 'top-0', 'z-50');
                
                if (name) {
                    const nameContainer = document.createElement('div');
                    // Separate bar under navbar, hidden on mobile
                    nameContainer.id = 'header-name-display';
                    nameContainer.className = "hidden md:flex justify-end max-w-7xl mx-auto px-4 mt-2 gap-3 items-center";
                    nameContainer.innerHTML = `
                        <div class="flex items-center gap-2 px-3 py-1 bg-white/5 rounded-lg border border-white/10 text-xs md:text-sm font-bold text-orange-400">
                            <svg class="w-4 h-4 text-orange-500" fill="currentColor" viewBox="0 0 20 20"><path d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"></path></svg> 
                            <span>${name}</span>
                        </div>
                        <button onclick="if(confirm('Change name?')){localStorage.removeItem('portal-username'); localStorage.removeItem('portal-userkey'); location.reload();}" class="text-[10px] text-gray-500 hover:text-white underline uppercase tracking-tighter transition-colors">Change Name</button>
                    `;
                    header.after(nameContainer);
                }
            }
        })();
    </script>
</body>"""

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove any previous versions of the script
        content = re.sub(r'<script>\s*\(function\(\) \{\s*const name = localStorage\.getItem\(\'portal-username\'\);[\s\S]*?<\/script>', '', content)

        # Inject new script
        if 'portal-username' not in content:
            new_content = content.replace('</body>', script_inject)
            
            if new_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Moved username under header and removed sticky for {filename}")

print("Done")
