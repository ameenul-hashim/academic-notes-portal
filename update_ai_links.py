import re
import sys

# Links mapped as [EN_LINK, ML_LINK]
links = {
    1: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%201/ai%20chapter%201.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%201/philosoply%20of%20ai%20chapter%201.pdf"
    ],
    2: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%202/ai%20english%20chapter%202.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%202/ai%20malayalam%20chapter%202.pdf"
    ],
    3: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%203/ai%20english%20chapter%203.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%203/ai%20malayalam%20chapter%203.pdf"
    ],
    4: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%204/ai%20english%20chapter%204.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%204/ai%20malayalam%20chapter%204.pdf"
    ],
    5: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%205/ai%20english%20chapter%205.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%205/ai%20malayalam%20chapter%205.pdf"
    ],
    6: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%206/ai%20english%20chapter%206.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter6/ai%20malayalam%20chapter%206.pdf"
    ],
    7: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%207/ai%20english%20chapter%207.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%207/ai%20malayalam%20chapter%207.pdf"
    ],
    8: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%20%208/ai%20english%20chapter%208.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%208/ai%20malayalam%20chapter%208.pdf"
    ],
    9: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%209/ai%20english%20chapter%209.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%209/ai%20malayalam%20chapter%209.pdf"
    ],
    10: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%2010/ai%20english%20chapter%2010.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%2010/ai%20malayalam%20chapter%2010.pdf"
    ],
    11: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%2011/ai%20english%20chapter%2011.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%2011/ai%20malayalam%20chapter%2011.pdf"
    ],
    12: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%2012/ai%20english%20chapter%2012.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%2012/ai%20malayalam%20chapter%2012.pdf"
    ],
    13: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%20%2013/ai%20english%20chapte%2013.pdf", # user's exact string
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%2013/ai%20malayalam%20chapter%2013.pdf"
    ],
    14: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%2014/ai%20english%20chapter%2014.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%2014/ai%20malayalam%20chapter%2014.pdf"
    ],
    15: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%2015/ai%20english%20chapter%2015.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%2015/ai%20malayalam%20chapter%2015.pdf"
    ],
    16: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%2016/ai%20enlish%20chapter%2016.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%2016/ai%20malayalam%20chapter%2016.pdf"
    ],
    17: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%2017/ai%20english%20chapter%2017.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%2017/ai%20malayalam%20chapter%2017.pdf"
    ],
    18: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%2018/ai%20english%20chapter%2018.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%2018/ai%20malayalam%20chapter%2018.pdf"
    ],
    19: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%2019/ai%20english%20chapter%2019.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%2019/ai%20malayalam%20chapter%2019.pdf"
    ],
    20: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%2020/ai%20english%20chapter%2020.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%2020/ai%20malayalam%20chapter%2020.pdf"
    ],
    21: [
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%2021/ai%20english%20chapter%2021.pdf",
        "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/chapter%2021/ai%20malayalam%20chapter%2021.pdf"
    ]
}

discussion_links = [
    "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20english/chapter%20discussion/ai%20chapter%205.pdf",
    "https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/philosophy%20of%20artificial%20intelligence/philosophy%20of%20ai%20malayalam/discussion%20last%20module/ai%20discussion%20module%205%20malayalam.pdf"
]

files = [
    ("world-en.html", 0, "English"),
    ("world-ml.html", 1, "Malayalam")
]

import os

for fname, lang_idx, lang_name in files:
    with open(fname, "r", encoding="utf-8") as f:
        content = f.read()

    # We need to replace the contents of <div class="flex flex-col gap-4"> ... </div> for each chapter modal
    for i in range(1, 22):
        link = links[i][lang_idx]
        download_name = f"Philosophy_of_AI_Chapter_{i}_{lang_name}.pdf"
        
        replacement = f'''<div class="flex flex-col gap-4">
                            <!-- View PDF -->
                            <a href="{link}" target="_blank" class="text-orange-300 hover:text-orange-100 underline text-center font-medium">View PDF</a>
                            <!-- Download PDF Option -->
                            <a href="{link}?download={download_name}" download="{download_name}" class="btn-glass text-center py-3 px-4 rounded-lg font-medium focus:outline-none focus:ring-2 focus:ring-orange-500 bg-white/10 text-white mt-2">
                                Download PDF
                            </a>
                        </div>'''

        # Using regex to match from <h3 ...>Chapter N</h3> to the end of <div class="flex flex-col gap-4">...</div>
        # Actually it's easier to match the div with id="modal-chX" and replace the <div class="flex flex-col gap-4"> ... </div> block entirely
        
        pattern = re.compile(r'(<div id="modal-ch' + str(i) + r'".*?<h3 class="[^"]*">Chapter ' + str(i) + r'</h3>\s*)(<div class="flex flex-col gap-4">.*?</div>\s*</div>)', re.DOTALL)
        content = pattern.sub(r'\g<1>' + replacement + '\n                    </div>', content)
        
        # We also need to add the correct SVG icon on the chapter card if it's currently missing it
        # Actually, adding the checkmark svg indicates it's available.
        # Find the <h2> inside the card for this chapter.
        h2_pattern = re.compile(r'(<h2 class="[^"]*">)(Chapter ' + str(i) + r')(</h2>)', re.DOTALL)
        h2_repl = r'\g<1><span class="flex items-center justify-center gap-2">Chapter ' + str(i) + r' <svg class="w-6 h-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></span>\g<3>'
        
        # Only replace if it doesn't already have the gap-2 and svg. But simple hack is to just replace the whole <h2> content
        h2_generic = re.compile(r'<h2 class="([^"]*)">\s*(?:<span[^>]*>)?Chapter ' + str(i) + r'(?:\s*<svg.*?</svg>\s*)?(?:</span>)?\s*</h2>', re.DOTALL)
        def h2_repl_func(m):
            cls = m.group(1)
            # Add flex styles if missing
            if "flex" not in cls:
                cls += " flex items-center justify-center gap-2"
            return f'<h2 class="{cls}">Chapter {i} <svg class="w-6 h-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></h2>'

        content = h2_generic.sub(h2_repl_func, content)

    # Finally, append the discussion module if it's not already there.
    if "modal-discussion" not in content:
        # Find the end of the grid: it's before </main>
        grid_end_idx = content.find('</main>')
        if grid_end_idx != -1:
            # We must insert it before the closing </div> of the grid, which is just before </main>
            # Let's find the closing tag of the grid.
            # Assuming there's a </div> right before </main>
            grid_close_idx = content.rfind('</div>', 0, grid_end_idx)
            
            disc_link = discussion_links[lang_idx]
            disc_name = f"Philosophy_of_AI_Discussion_Module_{lang_name}.pdf"
            
            discussion_html = f'''            <!-- Discussion Module Card -->
            <div>
                <div onclick="document.getElementById('modal-discussion').classList.remove('hidden')" class="glass-card h-40 flex items-center justify-center p-6 cursor-pointer rounded-xl text-center transition-all hover:-translate-y-1 bg-amber-500/10 border-amber-500/20 text-amber-100 hover:shadow-[0_0_30px_rgba(245,158,11,0.2)]">
                    <h2 class="flex items-center justify-center gap-2 text-2xl font-bold text-white">Discussion Module <svg class="w-6 h-6 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></h2>
                </div>

                <!-- Modal for Discussion Module -->
                <div id="modal-discussion" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4">
                    <div class="glass-card rounded-2xl p-8 max-w-sm w-full relative" onclick="event.stopPropagation()">
                        <button onclick="document.getElementById('modal-discussion').classList.add('hidden')" class="absolute top-4 right-4 text-gray-300 hover:text-white text-2xl">&times;</button>
                        <h3 class="text-2xl font-bold text-white mb-6 text-center">Discussion Module</h3>
                        <div class="flex flex-col gap-4">
                            <!-- View PDF -->
                            <a href="{disc_link}" target="_blank" class="text-orange-300 hover:text-orange-100 underline text-center font-medium">View PDF</a>
                            <!-- Download PDF Option -->
                            <a href="{disc_link}?download={disc_name}" download="{disc_name}" class="btn-glass text-center py-3 px-4 rounded-lg font-medium focus:outline-none focus:ring-2 focus:ring-orange-500 bg-white/10 text-white mt-2">
                                Download PDF
                            </a>
                        </div>
                    </div>
                </div>
            </div>
'''
            content = content[:grid_close_idx] + discussion_html + content[grid_close_idx:]
    
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)

print("Done updating chapters.")
