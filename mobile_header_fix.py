import os
import re

new_header = """
    <header class="glass-card sticky top-0 z-50 shadow-lg py-4">
        <div class="max-w-screen-2xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-4 md:gap-0">
            <!-- Spacer for desktop symmetry -->
            <div class="hidden md:block w-24"></div>
            
            <div class="text-center">
                <p class="text-[10px] md:text-sm text-orange-200 tracking-[0.2em] uppercase mb-1 font-bold">Welcome</p>
                <h1 class="font-black text-lg md:text-3xl tracking-tighter text-white whitespace-normal md:whitespace-nowrap">BA Calicut University Unofficial Notes And Classes</h1>
            </div>

            <div class="flex flex-col md:flex-row items-center gap-3 w-full md:w-auto">
                <a href="chat.html" class="w-full md:w-auto flex items-center justify-center gap-2 px-6 py-3 bg-gradient-to-r from-blue-600/30 to-indigo-600/30 hover:from-blue-600/50 hover:to-indigo-600/50 border border-blue-400/40 rounded-full text-blue-100 text-xs font-black uppercase tracking-widest transition-all hover:scale-[1.02] active:scale-95 shadow-[0_0_20px_rgba(37,99,235,0.2)] backdrop-blur-md">
                    <span class="relative flex h-2 w-2">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-2 w-2 bg-blue-500"></span>
                    </span>
                    Realtime Chat
                </a>
                <select id="theme-selector" class="w-full md:w-auto bg-white/10 text-white backdrop-blur-md border border-white/20 rounded-full px-6 py-3 text-xs font-black uppercase tracking-widest outline-none cursor-pointer hover:bg-white/20 transition-all appearance-none text-center">
                    <option value="rose">Change Theme</option>
                    <option value="rose">Reddish Brown</option>
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
                    <option value="sky">Desert Gold (Light)</option>
                </select>
            </div>
        </div>
    </header>
"""

def fix_header(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Match the entire <header> tag
    pattern = r'<header class="glass-card sticky top-0 z-50 shadow-lg py-4">.*?</header>'
    
    new_content = re.sub(pattern, new_header, content, flags=re.DOTALL)

    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

for filename in os.listdir('.'):
    if filename.endswith('.html') and filename != 'chat.html':
        if fix_header(filename):
            print(f"Fixed mobile header in: {filename}")
