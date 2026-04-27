import os
import re

# New Attractive "Not Uploaded" Message Style
# Using a glassy, deep amber/orange gradient that feels premium
NEW_MESSAGE_HTML = """<div class="text-center p-8 rounded-2xl bg-gradient-to-br from-amber-500/20 to-orange-600/20 backdrop-blur-lg border border-amber-500/30 shadow-2xl relative overflow-hidden group">
                                <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000"></div>
                                <svg class="w-16 h-16 mx-auto mb-4 text-amber-400 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
                                </svg>
                                <h4 class="text-xl font-bold text-amber-200 mb-2">Content Coming Soon</h4>
                                <p class="text-amber-100/80 leading-relaxed text-sm">Our team is currently translating and preparing these notes for you.</p>
                                <div class="mt-4 inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 border border-amber-500/20 text-xs font-medium text-amber-300">
                                    <span class="relative flex h-2 w-2">
                                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-amber-400 opacity-75"></span>
                                        <span class="relative inline-flex rounded-full h-2 w-2 bg-amber-500"></span>
                                    </span>
                                    Processing Upload
                                </div>
                            </div>"""

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Target the old rose/red gradient message block
    # We use a loose regex to catch the structure
    content = re.sub(r'<div class="text-center p-6 rounded-xl bg-gradient-to-br from-rose-600 to-red-700.*?</div>\s*</div>', NEW_MESSAGE_HTML + '\n                        </div>', content, flags=re.DOTALL)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Upgraded 'Not Uploaded' messages to a premium, attractive design.")
