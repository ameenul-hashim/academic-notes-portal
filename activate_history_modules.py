import re

links_en = {
    "ch3": "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/history%20of%20keralam%20upto%2012th%20century/history%20english/module%203/history%20english%20module%203.pdf",
    "ch2_2": "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/history%20of%20keralam%20upto%2012th%20century/history%20english/module%202%20chapter%202/history%20english%20module%202%20chapter%202.pdf",
    "ch2_3": "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/history%20of%20keralam%20upto%2012th%20century/history%20english/module%202%20chapter%203/history%20module%202%20chapter%203%20english.pdf"
}

links_ml = {
    "ch3": "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/history%20of%20keralam%20upto%2012th%20century/history%20malayalam/module%203/history%20module%203%20malayalam.pdf",
    "ch2_2": "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/history%20of%20keralam%20upto%2012th%20century/history%20malayalam/module%202%20chapter%202/history%20module%202%20chapter%202.pdf",
    "ch2_3": "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/history%20of%20keralam%20upto%2012th%20century/history%20malayalam/module%202%20chapter%203/history%20malayalam%20module%202%20chapter%203.pdf"
}

subtitles = {
    "ch2_2": "ROCK SHELTERS OF KERALAM",
    "ch2_3": "The Megalithic Culture"
}

# The active card HTML
def generate_active_card(ch_id, title, subtitle, link, lang_name):
    # for ch3, title is "Module 3", subtitle is empty
    # for ch2_2 / ch2_3, title is "Module 2, Chapter X", subtitle exists
    
    download_name = f"History_of_Keralam_{title.replace(' ', '_').replace(',', '')}_{lang_name}.pdf"
    
    if subtitle:
        title_html = f'''<h2 class="flex flex-col items-center justify-center text-center gap-1 text-2xl font-bold text-white">
                        <span class="flex items-center gap-2">{title} <svg class="w-6 h-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></span>
                        <span class="text-sm font-medium text-emerald-200/80">{subtitle}</span>
                    </h2>'''
        modal_title_html = f'''<h3 class="text-2xl font-bold text-white mb-6 text-center">{title}<br><span class="text-lg font-medium text-gray-300">{subtitle}</span></h3>'''
    else:
        title_html = f'''<h2 class="flex items-center justify-center gap-2 text-2xl font-bold text-white">{title} <svg class="w-6 h-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></h2>'''
        modal_title_html = f'''<h3 class="text-2xl font-bold text-white mb-6 text-center">{title}</h3>'''

    return f'''            <!-- Chapter Card {ch_id} -->
            <div>
                <div onclick="document.getElementById('modal-{ch_id}').classList.remove('hidden')" class="glass-card h-40 flex items-center justify-center p-6 cursor-pointer rounded-xl text-center transition-all hover:-translate-y-1 bg-emerald-500/10 border-emerald-500/20 text-emerald-100 hover:shadow-[0_0_30px_rgba(16,185,129,0.2)]">
                    {title_html}
                </div>

                <!-- Modal for {ch_id} -->
                <div id="modal-{ch_id}" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4">
                    <div class="glass-card rounded-2xl p-8 max-w-sm w-full relative" onclick="event.stopPropagation()">
                        <button onclick="document.getElementById('modal-{ch_id}').classList.add('hidden')" class="absolute top-4 right-4 text-gray-300 hover:text-white text-2xl">&times;</button>
                        {modal_title_html}
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
    ("economics-en.html", links_en, "English"),
    ("economics-ml.html", links_ml, "Malayalam")
]

for fname, links, lang_name in files:
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace ch2_2
    ch2_2_block = generate_active_card("ch2_2", "Module 2, Chapter 2", subtitles["ch2_2"], links["ch2_2"], lang_name)
    pattern_ch2_2 = re.compile(r'<!-- Chapter Card ch2_2 -->.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*', re.DOTALL)
    content = pattern_ch2_2.sub(ch2_2_block, content, count=1)

    # Replace ch2_3
    ch2_3_block = generate_active_card("ch2_3", "Module 2, Chapter 3", subtitles["ch2_3"], links["ch2_3"], lang_name)
    pattern_ch2_3 = re.compile(r'<!-- Chapter Card ch2_3 -->.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*', re.DOTALL)
    content = pattern_ch2_3.sub(ch2_3_block, content, count=1)

    # Replace ch3 (Module 3)
    # The structure of Chapter Card 3 might be slightly different depending on if it has the extra flex column container
    # I'll just use a regex matching from <!-- Chapter Card 3 --> down to that card's end.
    ch3_block = generate_active_card("ch3", "Module 3", "", links["ch3"], lang_name)
    # Be robust against the exact number of divs by matching up to right before `<!-- Chapter Card 4 -->` or `<!-- Chapter Card 5 -->`
    pattern_ch3 = re.compile(r'<!-- Chapter Card 3 -->.*?<!-- Chapter Card 4 -->\s*', re.DOTALL)
    content = pattern_ch3.sub(ch3_block + "<!-- Chapter Card 4 -->\n", content, count=1)

    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)

print("Updated all module cards with links and titles!")
