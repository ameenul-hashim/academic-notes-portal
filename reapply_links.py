import os
import re

def set_chapter_links(filename, chapter_num, view_link, download_link):
    if not os.path.exists(filename):
        return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We find the modal for the specific chapter
    # And replace the links inside it
    modal_pattern = rf'(<!-- Modal for Chapter {chapter_num} -->[\s\S]*?<div class="flex flex-col gap-4">[\s\S]*?<a href=").*?(" target="_blank"[\s\S]*?<a href=").*?(" download)'
    
    replacement = rf'\1{view_link}\2{download_link}\3'
    
    new_content = re.sub(modal_pattern, replacement, content)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename} Chapter {chapter_num}")

# AI English
set_chapter_links('world-en.html', 1, 'https://drive.google.com/file/d/1mc9bGtuGkK96IUXwN2rxysmYSBMSgI4Y/view', 'https://drive.google.com/uc?export=download&id=1mc9bGtuGkK96IUXwN2rxysmYSBMSgI4Y')
set_chapter_links('world-en.html', 2, 'https://drive.google.com/file/d/15arXegvd1KZsamD-5N7aH2Rq6Cbfii8_/view', 'https://drive.google.com/uc?export=download&id=15arXegvd1KZsamD-5N7aH2Rq6Cbfii8_')
set_chapter_links('world-en.html', 3, 'https://drive.google.com/file/d/1mc9bGtuGkK96IUXwN2rxysmYSBMSgI4Y/view', 'https://drive.google.com/uc?export=download&id=1mc9bGtuGkK96IUXwN2rxysmYSBMSgI4Y')

# AI Malayalam
set_chapter_links('world-ml.html', 1, 'https://docs.google.com/document/d/1KbTb4iYc1MfeTSZxMz7rj9WR7x78VlPd_dkuAWAQT7g/preview', 'https://docs.google.com/document/d/1KbTb4iYc1MfeTSZxMz7rj9WR7x78VlPd_dkuAWAQT7g/export?format=pdf')
set_chapter_links('world-ml.html', 2, 'https://docs.google.com/document/d/1Luku3tnY45i953s3cAeN056f6GUjuTDgxa-_kTpVf_w/preview', 'https://docs.google.com/document/d/1Luku3tnY45i953s3cAeN056f6GUjuTDgxa-_kTpVf_w/export?format=pdf')
set_chapter_links('world-ml.html', 3, 'https://docs.google.com/document/d/1dpfOxxh4s9E7yACFZIjplzsThXXXYuE40VSGIKiIEtI/preview', 'https://docs.google.com/document/d/1dpfOxxh4s9E7yACFZIjplzsThXXXYuE40VSGIKiIEtI/export?format=pdf')

print("Done")
