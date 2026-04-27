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

link = "https://drive.google.com/file/d/1ObVqXadd-IVY1ztRI3njqNldicI5peck/view?usp=sharing"

new_grid = f'''        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            
            <!-- Chapter Card 1 -->
            <div>
                <div onclick="document.getElementById('modal-ch1').classList.remove('hidden')" class="glass-card cursor-pointer rounded-xl p-10 h-full flex items-center justify-center text-center transition-all hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(236,72,153,0.3)]">
                    <h2 class="text-2xl font-bold text-white">Chapter 1</h2>
                </div>

                <!-- Modal for Chapter 1 -->
                <div id="modal-ch1" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4">
                    <div class="glass-card rounded-2xl p-8 max-w-sm w-full relative" onclick="event.stopPropagation()">
                        <button onclick="document.getElementById('modal-ch1').classList.add('hidden')" class="absolute top-4 right-4 text-gray-300 hover:text-white text-2xl">&times;</button>
                        <h3 class="text-2xl font-bold text-white mb-6 text-center">Chapter 1</h3>
                        <div class="flex flex-col gap-4">
                            <!-- You can put your custom link here -->
                            <a href="{link}" target="_blank" class="text-pink-300 hover:text-pink-100 underline text-center font-medium">Google Drive Link</a>
                            <!-- Download PDF Option -->
                            <a href="{link}" download class="btn-glass text-center py-3 px-4 rounded-lg font-medium focus:outline-none focus:ring-2 focus:ring-pink-500 bg-white/10 text-white mt-2">
                                Download PDF
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Chapter Card 2 -->
            <div>
                <div onclick="document.getElementById('modal-ch2').classList.remove('hidden')" class="glass-card cursor-pointer rounded-xl p-10 h-full flex items-center justify-center text-center transition-all hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(236,72,153,0.3)]">
                    <h2 class="text-2xl font-bold text-white">Chapter 2</h2>
                </div>

                <!-- Modal for Chapter 2 -->
                <div id="modal-ch2" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4">
                    <div class="glass-card rounded-2xl p-8 max-w-sm w-full relative" onclick="event.stopPropagation()">
                        <button onclick="document.getElementById('modal-ch2').classList.add('hidden')" class="absolute top-4 right-4 text-gray-300 hover:text-white text-2xl">&times;</button>
                        <h3 class="text-2xl font-bold text-white mb-6 text-center">Chapter 2</h3>
                        <div class="flex flex-col gap-4">
                            <!-- You can put your custom link here -->
                            <a href="{link}" target="_blank" class="text-pink-300 hover:text-pink-100 underline text-center font-medium">Google Drive Link</a>
                            <!-- Download PDF Option -->
                            <a href="{link}" download class="btn-glass text-center py-3 px-4 rounded-lg font-medium focus:outline-none focus:ring-2 focus:ring-pink-500 bg-white/10 text-white mt-2">
                                Download PDF
                            </a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Chapter Card 3 -->
            <div>
                <div onclick="document.getElementById('modal-ch3').classList.remove('hidden')" class="glass-card cursor-pointer rounded-xl p-10 h-full flex items-center justify-center text-center transition-all hover:-translate-y-1 hover:shadow-[0_0_20px_rgba(236,72,153,0.3)]">
                    <h2 class="text-2xl font-bold text-white">Chapter 3</h2>
                </div>

                <!-- Modal for Chapter 3 -->
                <div id="modal-ch3" class="hidden fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm px-4">
                    <div class="glass-card rounded-2xl p-8 max-w-sm w-full relative" onclick="event.stopPropagation()">
                        <button onclick="document.getElementById('modal-ch3').classList.add('hidden')" class="absolute top-4 right-4 text-gray-300 hover:text-white text-2xl">&times;</button>
                        <h3 class="text-2xl font-bold text-white mb-6 text-center">Chapter 3</h3>
                        <div class="flex flex-col gap-4">
                            <!-- You can put your custom link here -->
                            <a href="{link}" target="_blank" class="text-pink-300 hover:text-pink-100 underline text-center font-medium">Google Drive Link</a>
                            <!-- Download PDF Option -->
                            <a href="{link}" download class="btn-glass text-center py-3 px-4 rounded-lg font-medium focus:outline-none focus:ring-2 focus:ring-pink-500 bg-white/10 text-white mt-2">
                                Download PDF
                            </a>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </main>'''

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Regex to replace everything from the grid div up to </main>
        pattern = re.compile(r'<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">.*?</main>', re.DOTALL)
        
        if pattern.search(content):
            new_content = pattern.sub(new_grid, content)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"Pattern not found in {f}")
    else:
        print(f"File {f} not found")

print("Done")
