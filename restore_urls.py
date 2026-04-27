import os
import subprocess
import re

def restore_links_from_git():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    for file in html_files:
        if file == 'index.html': continue
        
        # Get the file content from commit db14ea5
        result = subprocess.run(['git', 'show', f'db14ea5:{file}'], capture_output=True, text=True, encoding='utf-8', errors='ignore')
        if result.returncode != 0:
            print(f"Failed to get {file} from git")
            continue
            
        old_content = result.stdout
        
        # Read current content
        with open(file, 'r', encoding='utf-8') as f:
            current_content = f.read()
            
        # Extract all link blocks from old content
        # We look for the gap-4 flex-col inside the modal
        old_blocks = re.findall(r'<div class="flex flex-col gap-4">.*?</div>\s*</div>', old_content, re.DOTALL)
        current_blocks = re.findall(r'<div class="flex flex-col gap-4">.*?</div>\s*</div>', current_content, re.DOTALL)
        
        if len(old_blocks) == len(current_blocks) and len(old_blocks) > 0:
            new_content = current_content
            for i in range(len(old_blocks)):
                # We just want to extract the URLs from old block and update current block
                old_urls = re.findall(r'href="([^"]+)"', old_blocks[i])
                current_urls = re.findall(r'href="([^"]+)"', current_blocks[i])
                
                if len(old_urls) >= 2 and len(current_urls) >= 2:
                    # Replace the first two URLs in the current block
                    updated_block = current_blocks[i]
                    updated_block = updated_block.replace(f'href="{current_urls[0]}"', f'href="{old_urls[0]}"', 1)
                    updated_block = updated_block.replace(f'href="{current_urls[1]}"', f'href="{old_urls[1]}"', 1)
                    
                    new_content = new_content.replace(current_blocks[i], updated_block)
            
            if new_content != current_content:
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Restored links for {file}")
        else:
            print(f"Block count mismatch for {file}")

restore_links_from_git()
