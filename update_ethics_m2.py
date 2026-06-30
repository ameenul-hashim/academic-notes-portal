import re

def update_file(path, link, download_name):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    coming_soon_regex = re.compile(
        r'(<h3 class="text-2xl font-bold text-white mb-6 text-center">Module 2</h3>\s*<div class="flex flex-col gap-4">).*?(</div>\s*</div>)',
        re.DOTALL
    )
    
    replacement_html = f'''\\g<1>
                            <!-- You can put your custom link here -->
                            <a href="{link}" target="_blank" class="text-orange-300 hover:text-orange-100 underline text-center font-medium">View PDF</a>
                            <!-- Download PDF Option -->
                            <a href="{link}?download={download_name}" download="{download_name}" class="btn-glass text-center py-3 px-4 rounded-lg font-medium focus:outline-none focus:ring-2 focus:ring-orange-500 bg-white/10 text-white mt-2">
                                Download PDF
                            </a>
                        \\g<2>'''

    content = coming_soon_regex.sub(replacement_html, content)
    
    h2_current = '<h2 class="text-2xl font-bold text-white">Module 2</h2>'
    h2_new = '<h2 class="flex items-center justify-center gap-2 text-2xl font-bold text-white">Module 2 <svg class="w-6 h-6 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></h2>'
    
    content = content.replace(h2_current, h2_new)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

en_file = r'c:\Users\lenov\OneDrive\Desktop\degree main projects\pdf app\ethics-en.html'
en_link = 'https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/fundamentals%20of%20ethics/fundamentals%20of%20ethics%20english/module%202/ethics%20module%202.pdf'
en_name = 'Fundamentals_of_Ethics_Module_2_English.pdf'
update_file(en_file, en_link, en_name)

ml_file = r'c:\Users\lenov\OneDrive\Desktop\degree main projects\pdf app\ethics-ml.html'
ml_link = 'https://cbxbwvftstjuqrqummyg.supabase.co/storage/v1/object/public/degree-sem1-notes/degree-sem1-notes%20and%20classes/fundamentals%20of%20ethics/fundamentals%20of%20ethics%20malayalam/module%202/malayalam%20module%202%20ethics.pdf'
ml_name = 'Fundamentals_of_Ethics_Module_2_Malayalam.pdf'
update_file(ml_file, ml_link, ml_name)

print("Updated links and icons.")
