import os
import re

files_to_restore = [
    'history-en.html', 'history-ml.html',
    'world-en.html', 'world-ml.html',
    'kerala-en.html', 'kerala-ml.html',
    'politics-en.html', 'politics-ml.html',
    'economics-en.html', 'economics-ml.html',
    'philosophy-en.html', 'philosophy-ml.html'
]

placeholder_id = "1ObVqXadd-IVY1ztRI3njqNldicI5peck"
message_html_pattern = r'<div class="flex flex-col gap-4">[\s\S]*?This is not translated and uploaded yet[\s\S]*?</div>'

original_html = f"""                        <div class="flex flex-col gap-4">
                            <!-- You can put your custom link here -->
                            <a href="https://drive.google.com/file/d/{placeholder_id}/view" target="_blank" class="text-pink-300 hover:text-pink-100 underline text-center font-medium">Google Drive Link</a>
                            <!-- Download PDF Option -->
                            <a href="https://drive.google.com/uc?export=download&id={placeholder_id}" download class="btn-glass text-center py-3 px-4 rounded-lg font-medium focus:outline-none focus:ring-2 focus:ring-pink-500 bg-white/10 text-white mt-2">
                                Download PDF
                            </a>
                        </div>"""

for filename in files_to_restore:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = re.sub(message_html_pattern, original_html, content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Restored placeholder links in {filename}")

print("Done")
