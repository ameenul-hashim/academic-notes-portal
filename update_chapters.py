import os
import re

files_21 = ['world-en.html', 'world-ml.html']
files_5 = [
    'history-en.html', 'history-ml.html',
    'kerala-en.html', 'kerala-ml.html',
    'politics-en.html', 'politics-ml.html',
    'economics-en.html', 'economics-ml.html',
    'philosophy-en.html', 'philosophy-ml.html'
]

link = "https://drive.google.com/file/d/1ObVqXadd-IVY1ztRI3njqNldicI5peck/view?usp=sharing"

def generate_grid(num_chapters):
    html = '        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">\n'
    for i in range(1, num_chapters + 1):
        placeholder_id = "1ObVqXadd-IVY1ztRI3njqNldicI5peck"
        view_link = f"https://drive.google.com/file/d/{placeholder_id}/view"
        download_link = f"https://drive.google.com/uc?export=download&id={placeholder_id}"
        
        card = f'''            
            <!-- Chapter Card {i} -->
            <div>
                <div onclick="document.getElementById('modal-ch{i}').classList.remove('hidden')" class="glass-card cursor-pointer rounded-xl p-10 h-full flex items-center justify-center text-center transition-all hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(236,72,153,0.3)]">
                    <h2 class="text-2xl font-bold text-white">Chapter {i}</h2>
                </div>

                <!-- Modal for Chapter {i} -->
                <div id="modal-ch{i}" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4">
                    <div class="glass-card rounded-2xl p-8 max-w-sm w-full relative" onclick="event.stopPropagation()">
                        <button onclick="document.getElementById('modal-ch{i}').classList.add('hidden')" class="absolute top-4 right-4 text-gray-300 hover:text-white text-2xl">&times;</button>
                        <h3 class="text-2xl font-bold text-white mb-6 text-center">Chapter {i}</h3>
                        <div class="flex flex-col gap-4">
                            <!-- You can put your custom link here -->
                            <a href="{view_link}" target="_blank" class="text-pink-300 hover:text-pink-100 underline text-center font-medium">Google Drive Link</a>
                            <!-- Download PDF Option -->
                            <a href="{download_link}" download class="btn-glass text-center py-3 px-4 rounded-lg font-medium focus:outline-none focus:ring-2 focus:ring-pink-500 bg-white/10 text-white mt-2">
                                Download PDF
                            </a>
                        </div>
                    </div>
                </div>
            </div>'''
        html += card
    html += '\n        </div>\n    </main>'
    return html

def update_file(filename, num_chapters):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        pattern = re.compile(r'<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">.*?</main>', re.DOTALL)
        
        if pattern.search(content):
            new_grid = generate_grid(num_chapters)
            new_content = pattern.sub(new_grid, content)
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename} with {num_chapters} chapters")
        else:
            print(f"Pattern not found in {filename}")
    else:
        print(f"File {filename} not found")

for f in files_21:
    update_file(f, 21)

for f in files_5:
    update_file(f, 5)

print("Done")
