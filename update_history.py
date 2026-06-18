import re

files = ["economics-en.html", "economics-ml.html"]

placeholder_template = """            <!-- Chapter Card {id} -->
            <div>
                <div onclick="document.getElementById('modal-{id}').classList.remove('hidden')" class="glass-card h-40 flex items-center justify-center p-6 cursor-pointer rounded-xl text-center transition-all hover:-translate-y-1 bg-rose-500/10 border-rose-500/20 text-rose-100 hover:shadow-[0_0_30px_rgba(244,63,94,0.1)]">
                    <h2 class="flex flex-col items-center justify-center text-center gap-1 text-2xl font-bold text-white">
                        <span class="flex items-center gap-2">{title}</span>
                        <span class="text-sm font-medium text-rose-200/80">{subtitle}</span>
                    </h2>
                </div>

                <!-- Modal for {id} -->
                <div id="modal-{id}" class="hidden fixed inset-0 z-50 flex flex-col items-center justify-center bg-black/60 backdrop-blur-sm px-4">
                    <div class="glass-card rounded-2xl p-8 max-w-sm w-full relative" onclick="event.stopPropagation()">
                        <button onclick="document.getElementById('modal-{id}').classList.add('hidden')" class="absolute top-4 right-4 text-gray-300 hover:text-white text-2xl">&times;</button>
                        <h3 class="text-2xl font-bold text-white mb-6 text-center">{title}<br><span class="text-lg font-medium text-gray-300">{subtitle}</span></h3>
                        <div class="flex flex-col gap-4">
                            <div class="text-center p-8 rounded-2xl bg-gradient-to-br from-rose-900/40 to-red-950/40 backdrop-blur-lg border border-rose-500/30 shadow-2xl relative overflow-hidden group">
                                <div class="absolute inset-0 bg-gradient-to-r from-transparent via-white/5 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000"></div>
                                <svg class="w-16 h-16 mx-auto mb-4 text-rose-300 animate-pulse" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
                                </svg>
                                <h4 class="text-xl font-bold text-rose-100 mb-2">Content Coming Soon</h4>
                                <p class="text-rose-200/80 leading-relaxed text-sm">Our team is currently preparing these notes.</p>
                                <div class="mt-4 inline-flex items-center gap-2 px-3 py-1 rounded-full bg-rose-500/10 border border-rose-500/20 text-xs font-medium text-rose-300">
                                    <span class="relative flex h-2 w-2">
                                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-rose-400 opacity-75"></span>
                                        <span class="relative inline-flex rounded-full h-2 w-2 bg-rose-500"></span>
                                    </span>
                                    Processing Upload
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>            
"""

for fname in files:
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Update Module 2 to "Module 2 Chapter 1" + Prehistoric Settlements
    
    # Identify the block for modal-ch2
    ch2_card_pattern = r'(<div onclick="document\.getElementById\(\'modal-ch2\'\)\.classList\.remove\(\'hidden\'\)" class="[^"]*">)\s*(<h2 class="[^"]*">)(.*?)(</h2>)'
    def replace_ch2_card(match):
        open_div = match.group(1)
        h2_open = match.group(2)
        # We need to change the h2 block to include the subtitle
        # Ensure it has flex-col for subtitle layout
        # Currently h2 might be: <h2 class="flex items-center justify-center gap-2 text-2xl font-bold text-white">
        new_h2_open = '<h2 class="flex flex-col items-center justify-center text-center gap-1 text-2xl font-bold text-white">'
        inner = '<span class="flex items-center gap-2">Module 2, Chapter 1 <svg class="w-6 h-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></span>\n                        <span class="text-sm font-medium text-emerald-200/80">Prehistoric Settlements</span>'
        return open_div + '\n                    ' + new_h2_open + '\n                        ' + inner + '\n                    </h2>'
        
    content = re.sub(ch2_card_pattern, replace_ch2_card, content, count=1)
    
    # Update modal-ch2 title
    modal_ch2_title_pattern = r'(<div id="modal-ch2" .*?<h3 class="[^"]*">).*?(</h3>)'
    def replace_ch2_modal_title(match):
        pre = match.group(1)
        post = match.group(2)
        return pre + 'Module 2, Chapter 1<br><span class="text-lg font-medium text-gray-300">Prehistoric Settlements</span>' + post
    
    content = re.sub(modal_ch2_title_pattern, replace_ch2_modal_title, content, count=1)
    
    # 2. Add placeholder cards for Module 2 Chapter 2 and Module 2 Chapter 3
    # We will append them right after the modal-ch2 block
    # A modal block ends with:
    #                         </div>
    #                     </div>
    #                 </div>
    #             </div>            
    
    # Let's find where modal-ch2 block ends. It ends before `<!-- Chapter Card 3 -->` or similar.
    # It's easiest to split at `<!-- Chapter Card 3 -->` and insert there.
    
    if "<!-- Chapter Card 3 -->" in content and "modal-ch2_2" not in content:
        parts = content.split("<!-- Chapter Card 3 -->", 1)
        
        new_cards = ""
        new_cards += placeholder_template.format(id="ch2_2", title="Module 2, Chapter 2", subtitle="Pending")
        new_cards += placeholder_template.format(id="ch2_3", title="Module 2, Chapter 3", subtitle="Pending")
        
        content = parts[0] + new_cards + "<!-- Chapter Card 3 -->" + parts[1]
    
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)

# Update sync_index_status.py to count these new modals
with open('sync_index_status.py', 'r', encoding='utf-8') as f:
    sync = f.read()

# Change `modals = re.findall(r'id="(modal-ch\d+|modal-discussion)"', content)` to support underscores
sync = sync.replace(r'id="(modal-ch\d+|modal-discussion)"', r'id="(modal-ch[\d_]+|modal-discussion)"')

with open('sync_index_status.py', 'w', encoding='utf-8') as f:
    f.write(sync)

print("Updated History of Keralam and sync tool.")
