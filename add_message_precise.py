import os
import re

files = [
    'history-en.html', 'history-ml.html',
    'world-en.html', 'world-ml.html',
    'kerala-en.html', 'kerala-ml.html',
    'politics-en.html', 'politics-ml.html',
    'economics-en.html', 'economics-ml.html',
    'philosophy-en.html', 'philosophy-ml.html'
]

placeholder_id = "1ObVqXadd-IVY1ztRI3njqNldicI5peck"

message_html = """                        <div class="flex flex-col gap-4">
                            <div class="text-center p-6 rounded-xl bg-gradient-to-br from-pink-600 to-purple-700 text-white font-bold shadow-2xl border border-white/20">
                                <svg class="w-12 h-12 mx-auto mb-4 text-pink-200" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                                <p class="text-lg leading-relaxed">This is not translated and uploaded yet.</p>
                                <p class="text-sm mt-2 text-pink-100 opacity-90">Please contact admin for uploads.</p>
                            </div>
                        </div>"""

# Targeted replacement function to avoid over-matching
def add_message_precisely(filename):
    if not os.path.exists(filename):
        return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We look for each modal definition individually
    # and check if it contains the placeholder ID
    
    modals = re.findall(r'(<!-- Modal for Chapter \d+ -->[\s\S]*?</div>\s*</div>\s*</div>)', content)
    
    new_content = content
    for modal in modals:
        if placeholder_id in modal:
            # Replace the links div with the message
            # We target the specific div class="flex flex-col gap-4"
            modal_with_message = re.sub(r'<div class="flex flex-col gap-4">[\s\S]*?</div>\s*</div>', message_html + '\n                    </div>', modal)
            new_content = new_content.replace(modal, modal_with_message)
            
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added message to placeholder chapters in {filename}")

for f in files:
    add_message_precisely(f)

print("Done")
