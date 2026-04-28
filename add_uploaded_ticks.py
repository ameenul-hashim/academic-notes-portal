import os
import re
import glob

html_files = glob.glob('*-en.html') + glob.glob('*-ml.html')

svg_tick = '<svg class="w-6 h-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modals = re.findall(r'id="(modal-ch\d+)"', content)
    
    modified = False
    for modal_id in set(modals):
        parts = content.split(f'id="{modal_id}"')
        if len(parts) < 2:
            continue
            
        modal_content = parts[1][:2000]
        # Check for Google Drive or Google Docs links
        if 'drive.google.com' in modal_content or 'docs.google.com' in modal_content:
            # Flexible onclick regex to handle potential spaces or semicolons
            pattern = re.compile(
                r'(onclick="document\.getElementById\(\'' + modal_id + r'\'\)\.classList\.remove\(\'hidden\'\)[^"]*"[^>]*>.*?<h2[^>]*>)(.*?)(</h2>)',
                re.DOTALL
            )
            
            def replacer(match):
                div_and_h2 = match.group(1)
                text = match.group(2).strip()
                suffix = match.group(3)
                
                idx = div_and_h2.rfind('<h2')
                div_part = div_and_h2[:idx]
                h2_part = div_and_h2[idx:]
                
                if '<svg' in text and 'text-green-400' in text:
                    return match.group(0)
                    
                if 'flex' not in h2_part:
                    h2_part = h2_part.replace('class="', 'class="flex items-center justify-center gap-2 ')
                    
                return f"{div_part}{h2_part}{text} {svg_tick}{suffix}"
            
            new_content = pattern.sub(replacer, content)
            if new_content != content:
                content = new_content
                modified = True
                print(f"Added tick for {modal_id} in {file}")

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Done")
