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

# Mapping for specific links
# Key is the current placeholder link or specific link to find
# Value is a tuple of (New View Link, New Download Link)

specific_updates = {
    # Placeholder link
    'https://drive.google.com/file/d/1ObVqXadd-IVY1ztRI3njqNldicI5peck/view?usp=sharing': 
    ('https://drive.google.com/file/d/1ObVqXadd-IVY1ztRI3njqNldicI5peck/view', 
     'https://drive.google.com/uc?export=download&id=1ObVqXadd-IVY1ztRI3njqNldicI5peck'),
    
    # AI English Ch 1
    'https://drive.google.com/file/d/1mc9bGtuGkK96IUXwN2rxysmYSBMSgI4Y/view?usp=sharing':
    ('https://drive.google.com/file/d/1mc9bGtuGkK96IUXwN2rxysmYSBMSgI4Y/view',
     'https://drive.google.com/uc?export=download&id=1mc9bGtuGkK96IUXwN2rxysmYSBMSgI4Y'),
     
    # AI English Ch 2
    'https://drive.google.com/file/d/15arXegvd1KZsamD-5N7aH2Rq6Cbfii8_/view?usp=sharing':
    ('https://drive.google.com/file/d/15arXegvd1KZsamD-5N7aH2Rq6Cbfii8_/view',
     'https://drive.google.com/uc?export=download&id=15arXegvd1KZsamD-5N7aH2Rq6Cbfii8_'),
     
    # AI Malayalam Ch 1
    'https://docs.google.com/document/d/1KbTb4iYc1MfeTSZxMz7rj9WR7x78VlPd_dkuAWAQT7g/edit?usp=drive_link':
    ('https://docs.google.com/document/d/1KbTb4iYc1MfeTSZxMz7rj9WR7x78VlPd_dkuAWAQT7g/preview',
     'https://docs.google.com/document/d/1KbTb4iYc1MfeTSZxMz7rj9WR7x78VlPd_dkuAWAQT7g/export?format=pdf'),
     
    # AI Malayalam Ch 2
    'https://docs.google.com/document/d/1Luku3tnY45i953s3cAeN056f6GUjuTDgxa-_kTpVf_w/edit?usp=drive_link':
    ('https://docs.google.com/document/d/1Luku3tnY45i953s3cAeN056f6GUjuTDgxa-_kTpVf_w/preview',
     'https://docs.google.com/document/d/1Luku3tnY45i953s3cAeN056f6GUjuTDgxa-_kTpVf_w/export?format=pdf')
}

for filename in files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changed = False
        for old_link, (new_view, new_download) in specific_updates.items():
            if old_link in content:
                # We need to be careful to replace the right attribute
                # The "Google Drive Link" uses href="...target="_blank"
                # The "Download PDF" link uses href="..." download
                
                # Replace Google Drive Link (View)
                view_pattern = f'href="{old_link}" target="_blank"'
                new_view_attr = f'href="{new_view}" target="_blank"'
                if view_pattern in content:
                    content = content.replace(view_pattern, new_view_attr)
                    changed = True
                
                # Replace Download PDF Link
                download_pattern = f'href="{old_link}" download'
                new_download_attr = f'href="{new_download}" download'
                if download_pattern in content:
                    content = content.replace(download_pattern, new_download_attr)
                    changed = True
        
        if changed:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated constraints in {filename}")

print("Done")
