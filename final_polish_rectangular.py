import os
import re

def polish_rectangular_and_modals(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Enforce Rectangular shape for Chapter Cards (h-40 instead of h-48)
    if re.search(r'Level 3', content):
        pattern_ch = r'class="glass-card h-48 flex items-center justify-center p-6'
        replacement_ch = r'class="glass-card h-40 flex items-center justify-center p-6'
        new_content = re.sub(pattern_ch, replacement_ch, content)
    else:
        new_content = content

    # 2. Upgrade Modals to Premium Gradient Buttons for ALL subjects
    # Search for the old underline link structure and replace with Premium Buttons
    modal_pattern = r'<div class="flex flex-col gap-4">\s*(?:<!--.*?-->\s*)?<a href="([^"]+)"[^>]*>.*?</a>\s*(?:<!--.*?-->\s*)?<a href="([^"]+)"[^>]*>.*?Download PDF.*?</a>'
    
    def upgrade_modal(match):
        view_link = match.group(1)
        download_link = match.group(2)
        
        return f"""<div class="flex flex-col gap-4">
                            <a href="{view_link}" target="_blank" class="w-full py-4 bg-gradient-to-r from-rose-600 to-red-700 hover:from-rose-500 hover:to-red-600 text-white font-bold rounded-xl shadow-xl transition-all hover:-translate-y-1 active:scale-95 flex items-center justify-center gap-3">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                                View Notes
                            </a>
                            <a href="{download_link}" download target="_blank" class="w-full py-4 bg-white/10 hover:bg-white/20 text-white font-bold rounded-xl border border-white/20 transition-all flex items-center justify-center gap-3">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                                Download PDF
                            </a>
                        </div>"""

    new_content = re.sub(modal_pattern, upgrade_modal, new_content, flags=re.DOTALL)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
updated_count = 0
for html_file in html_files:
    if polish_rectangular_and_modals(html_file):
        updated_count += 1
        print(f"Polished: {html_file}")

print(f"Total files updated: {updated_count}")
