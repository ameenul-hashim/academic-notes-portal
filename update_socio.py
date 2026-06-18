import sys
import re

links_en = {
    "Chapter 2": "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/sociology/sociology%20english/module%202/sociology%20module%202.pdf",
    "Chapter 3": "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/sociology/sociology%20english/module%203/sociology%20module%203.pdf"
}

links_ml = {
    "Chapter 2": "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/sociology/sociology%20malayalam/module%202/sociology%20module%202%20malayalam%20.pdf",
    "Chapter 3": "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/sociology/sociology%20malayalam/module%203/sociology%20module%203%20malayalam.pdf"
}

def create_card(ch_num, link, lang_name):
    download_name = f"Sociology_Module_{ch_num}_{lang_name}.pdf"
    
    return f'''            <!-- Chapter Card {ch_num} -->
            <div>
                <div onclick="document.getElementById('modal-ch{ch_num}').classList.remove('hidden')" class="glass-card h-40 flex items-center justify-center p-6 cursor-pointer rounded-xl text-center transition-all hover:-translate-y-1 bg-amber-500/10 border-amber-500/20 text-amber-100 hover:shadow-[0_0_30px_rgba(245,158,11,0.2)]">
                    <h2 class="flex items-center justify-center gap-2 text-2xl font-bold text-white">Module {ch_num} <svg class="w-6 h-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></h2>
                </div>

                <!-- Modal for Chapter {ch_num} -->
                <div id="modal-ch{ch_num}" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4">
                    <div class="glass-card rounded-2xl p-8 max-w-sm w-full relative" onclick="event.stopPropagation()">
                        <button onclick="document.getElementById('modal-ch{ch_num}').classList.add('hidden')" class="absolute top-4 right-4 text-gray-300 hover:text-white text-2xl">&times;</button>
                        <h3 class="text-2xl font-bold text-white mb-6 text-center">Module {ch_num}</h3>
                        <div class="flex flex-col gap-4">
                            <!-- View PDF -->
                            <a href="{link}" target="_blank" class="text-orange-300 hover:text-orange-100 underline text-center font-medium">View PDF</a>
                            <!-- Download PDF Option -->
                            <a href="{link}?download={download_name}" download="{download_name}" class="btn-glass text-center py-3 px-4 rounded-lg font-medium focus:outline-none focus:ring-2 focus:ring-orange-500 bg-white/10 text-white mt-2">
                                Download PDF
                            </a>
                        </div>
                    </div>
                </div>
            </div>            
'''

files = [
    ("sociology-en.html", links_en, "English"),
    ("sociology-ml.html", links_ml, "Malayalam")
]

for fname, links, lang_name in files:
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    # Rename existing "Chapter 1" to "Module 1"
    content = content.replace("Chapter 1", "Module 1")
    
    # Also change the first module's color from emerald to amber if we want consistency with AI modules, but let's just make it amber in the replacement directly if it's emerald. 
    # Actually, Emerald means completed in some of his subjects, but AI used amber.
    content = content.replace('bg-emerald-500/10', 'bg-amber-500/10').replace('border-emerald-500/20', 'border-amber-500/20').replace('text-emerald-100', 'text-amber-100').replace('hover:shadow-[0_0_30px_rgba(16,185,129,0.2)]', 'hover:shadow-[0_0_30px_rgba(245,158,11,0.2)]')
    content = content.replace('text-red-400', 'text-green-400') # Checkmark is usually green

    # Find the closing tag of the grid where the cards are appended
    grid_end_idx = content.find('</main>')
    grid_close_idx = content.rfind('</div>', 0, grid_end_idx)

    new_cards = ""
    if "modal-ch2" not in content:
        new_cards += create_card(2, links["Chapter 2"], lang_name)
    if "modal-ch3" not in content:
        new_cards += create_card(3, links["Chapter 3"], lang_name)
    
    if new_cards:
        content = content[:grid_close_idx] + new_cards + content[grid_close_idx:]
    
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)

print("Sociology modules added successfully.")
