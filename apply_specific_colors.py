import os
import re

def update_links_and_colors():
    # Files to make RED for Chapter 1
    red_ch1_files = [
        'sociology-en.html', 'sociology-ml.html',
        'philosophy-en.html', 'philosophy-ml.html',
        'economics-en.html', 'economics-ml.html' # History of Keralam
    ]
    
    # Files to make RED for Chapters 1, 2, 3
    red_ch123_files = [
        'kerala-en.html', 'kerala-ml.html' # English
    ]
    
    # History of Keralam Links (Economics files)
    history_en_link = "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/history%20of%20keralam%20upto%2012th%20century/history%20english/chapter1/history%20of%20keralam%20upto%2012th%20century%20chapter%201.pdf"
    history_ml_link = "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/history%20of%20keralam%20upto%2012th%20century/history%20malayalam/chapter1/history%20of%20kerala%20upto%2012th%20century%20chapter1.pdf"

    # 1. Update History of Keralam links first
    for f_name, link, label in [('economics-en.html', history_en_link, 'English'), ('economics-ml.html', history_ml_link, 'Malayalam')]:
        if os.path.exists(f_name):
            with open(f_name, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update Chapter 1 Modal content
            pattern = r'(<div id="modal-ch1".*?<h3.*?>Chapter 1</h3>\s*<div class="flex flex-col gap-4">)(.*?)(</div>)'
            
            replacement = (
                f'\\1\n'
                f'                            <a href="{link}" target="_blank" class="text-orange-300 hover:text-orange-100 underline text-center font-medium">View PDF</a>\n'
                f'                            <a href="{link}" download="History_of_Keralam_Chapter_1_{label}.pdf" class="btn-glass text-center py-3 px-4 rounded-lg font-medium focus:outline-none focus:ring-2 focus:ring-orange-500 bg-white/10 text-white mt-2">\n'
                f'                                Download PDF\n'
                f'                            </a>\n'
                f'                        \\3'
            )
            
            new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
            with open(f_name, 'w', encoding='utf-8') as f:
                f.write(new_content)

    # 2. Update Colors
    for f_name in red_ch1_files:
        if os.path.exists(f_name):
            with open(f_name, 'r', encoding='utf-8') as f:
                content = f.read()
            # Find Chapter 1 h2 and change tick color
            pattern = r'(<h2 class="flex items-center justify-center gap-2 text-2xl font-bold text-white">Chapter 1 <svg class="w-6 h-6 )text-green-400'
            new_content = re.sub(pattern, r'\1text-red-400', content)
            with open(f_name, 'w', encoding='utf-8') as f:
                f.write(new_content)

    for f_name in red_ch123_files:
        if os.path.exists(f_name):
            with open(f_name, 'r', encoding='utf-8') as f:
                content = f.read()
            # Find Chapter 1, 2, 3 h2 and change tick color
            for ch in ['1', '2', '3']:
                pattern = f'(<h2 class="flex items-center justify-center gap-2 text-2xl font-bold text-white">Chapter {ch} <svg class="w-6 h-6 )text-green-400'
                content = re.sub(pattern, r'\1text-red-400', content)
            with open(f_name, 'w', encoding='utf-8') as f:
                f.write(content)

if __name__ == "__main__":
    update_links_and_colors()
