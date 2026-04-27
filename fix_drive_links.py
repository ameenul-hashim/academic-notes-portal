import os
import re

def fix_drive_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the modal link blocks
    # Pattern to find the two links and extract the ID
    # We look for /file/d/ID/view or /uc?export=download&id=ID or /uc?id=ID
    
    # regex for drive ID: [a-zA-Z0-9_-]{25,}
    
    def replace_links(match):
        full_block = match.group(0)
        # Extract the first ID found in the block
        id_match = re.search(r'id=([a-zA-Z0-9_-]{25,})', full_block)
        if not id_match:
            id_match = re.search(r'/d/([a-zA-Z0-9_-]{25,})/', full_block)
        
        if id_match:
            drive_id = id_match.group(1)
            # Create the standardized button block
            return f"""<div class="flex flex-col gap-4">
                            <a href="https://drive.google.com/file/d/{drive_id}/view?usp=sharing" target="_blank" class="w-full py-4 bg-gradient-to-r from-rose-600 to-red-700 hover:from-rose-500 hover:to-red-600 text-white font-bold rounded-xl shadow-xl transition-all hover:-translate-y-1 active:scale-95 flex items-center justify-center gap-3">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
                                View Notes
                            </a>
                            <a href="https://drive.google.com/uc?id={drive_id}&export=download" target="_blank" class="w-full py-4 bg-white/10 hover:bg-white/20 text-white font-bold rounded-xl border border-white/20 transition-all flex items-center justify-center gap-3">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                                Download PDF
                            </a>
                        </div>"""
        return full_block

    # Replace modal link blocks (look for the flex-col gap-4 container)
    pattern = r'<div class="flex flex-col gap-4">.*?</div>\s*</div>'
    new_content = re.sub(pattern, replace_links, content, flags=re.DOTALL)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
updated_count = 0
for html_file in html_files:
    if fix_drive_links(html_file):
        updated_count += 1
        print(f"Fixed Links: {html_file}")

print(f"Total files updated: {updated_count}")
