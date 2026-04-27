import os
import re

def revert_modals(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for the "Premium" buttons I added
    premium_pattern = r'<div class="flex flex-col gap-4">\s*<a href="([^"]+)"[^>]*>.*?View Notes.*?</a>\s*<a href="([^"]+)"[^>]*>.*?Download PDF.*?</a>\s*</div>'
    
    def reconstruct_old(match):
        view_link = match.group(1)
        # Convert /uc?id=... back to /file/d/.../view for the download link if needed, 
        # but usually the download button uses a specific format.
        
        # Extract ID from view_link or download_link
        id_match = re.search(r'id=([a-zA-Z0-9_-]{25,})', view_link)
        if not id_match:
            id_match = re.search(r'/d/([a-zA-Z0-9_-]{25,})/', view_link)
        
        if id_match:
            drive_id = id_match.group(1)
            # Reconstruct the "Philosophy of AI" style
            return f"""<div class="flex flex-col gap-4">
                            <!-- You can put your custom link here -->
                            <a href="https://drive.google.com/file/d/{drive_id}/view?usp=sharing" target="_blank" class="text-orange-300 hover:text-orange-100 underline text-center font-medium">Google Drive Link</a>
                            <!-- Download PDF Option -->
                            <a href="https://drive.google.com/uc?export=download&id={drive_id}" download class="btn-glass text-center py-3 px-4 rounded-lg font-medium focus:outline-none focus:ring-2 focus:ring-orange-500 bg-white/10 text-white mt-2">
                                Download PDF
                            </a>
                        </div>"""
        return match.group(0)

    new_content = re.sub(premium_pattern, reconstruct_old, content, flags=re.DOTALL)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
updated_count = 0
for html_file in html_files:
    if revert_modals(html_file):
        updated_count += 1
        print(f"Reverted Modals: {html_file}")

print(f"Total files updated: {updated_count}")
