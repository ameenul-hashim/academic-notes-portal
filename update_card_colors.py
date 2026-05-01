import os
import re

# Color mappings (Light transparent colors)
COLORS = {
    'supabase': 'bg-emerald-500/10 border-emerald-500/20 text-emerald-100 hover:shadow-[0_0_30px_rgba(16,185,129,0.2)]',
    'drive': 'bg-amber-500/10 border-amber-500/20 text-amber-100 hover:shadow-[0_0_30px_rgba(245,158,11,0.2)]',
    'none': 'bg-rose-500/10 border-rose-500/20 text-rose-100 hover:shadow-[0_0_30px_rgba(244,63,94,0.1)]'
}

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all chapter card containers
    # Structure: <div onclick="document.getElementById('modal-ch[N]').classList.remove('hidden')" class="glass-card ..."> ... </div>
    # And then the modal: <div id="modal-ch[N]" ...> ... </div>

    # Step 1: Identify the status of each modal
    modals = re.findall(r'id="(modal-ch\d+)".*?\u003c/div\u003e', content, re.DOTALL)
    
    # We'll use a more robust way: find modal IDs and their content
    modal_matches = list(re.finditer(r'id="(modal-ch\d+)".*?(?=\u003c!-- Chapter Card|\u003c/main\u003e|\u003c!-- Footer|\u003cdiv onclick=|$)', content, re.DOTALL))
    
    status_map = {}
    for match in modal_matches:
        modal_id = match.group(1)
        modal_content = match.group(0)
        
        if 'supabase.co' in modal_content:
            status_map[modal_id] = 'supabase'
        elif 'drive.google.com' in modal_content:
            status_map[modal_id] = 'drive'
        else:
            status_map[modal_id] = 'none'

    # Step 2: Update the onclick div classes
    def replace_card(match):
        modal_id = match.group(1)
        old_classes = match.group(2)
        inner_content = match.group(3)
        
        status = status_map.get(modal_id, 'none')
        new_color_classes = COLORS[status]
        
        # Remove old background/border classes if any, and keep standard ones
        # Standard: glass-card h-40 flex items-center justify-center p-6 cursor-pointer rounded-xl text-center transition-all hover:-translate-y-1
        base_classes = "glass-card h-40 flex items-center justify-center p-6 cursor-pointer rounded-xl text-center transition-all hover:-translate-y-1"
        
        updated_div = f'\u003cdiv onclick="document.getElementById(\'{modal_id}\').classList.remove(\'hidden\')" class="{base_classes} {new_color_classes}"\u003e{inner_content}\u003c/div\u003e'
        return updated_div

    # Pattern for the card trigger div
    pattern = r'\u003cdiv onclick="document\.getElementById\(\'(modal-ch\d+)\'\)\.classList\.remove\(\'hidden\'\)" class="(.*?)"\u003e(.*?)\u003c/div\u003e'
    
    new_content = re.sub(pattern, replace_card, content, flags=re.DOTALL)
    
    # Step 3: Cleanup icons inside h2 (optional but good for consistency)
    # If it's Supabase, we might want a green tick. If Coming Soon, no tick.
    # The user didn't explicitly ask to change icons, but "light green" card implies "success".
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

for filename in os.listdir('.'):
    if filename.endswith('.html') and filename != 'index.html':
        if update_file(filename):
            print(f"Updated card colors in: {filename}")
