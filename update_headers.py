import glob

def run():
    try:
        with open('index.html', 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        content = content.replace('<header class="glass-card sticky top-0 z-50 shadow-lg py-4">', '<header class="glass-card relative md:sticky top-0 z-50 shadow-lg py-4">')
        with open('index.html', 'w', encoding='utf-8', errors='ignore') as f:
            f.write(content)
            
        html_files = glob.glob('*.html')
        if 'index.html' in html_files:
            html_files.remove('index.html')
        if 'chat.html' in html_files:
            html_files.remove('chat.html') # Do not hide Navbar on chat page just to be safe
            
        for fname in html_files:
            with open(fname, 'r', encoding='utf-8', errors='ignore') as f:
                c = f.read()
            c = c.replace('<header class="glass-card sticky top-0 z-50 shadow-lg py-4">', '<header class="hidden md:block glass-card sticky top-0 z-50 shadow-lg py-4">')
            with open(fname, 'w', encoding='utf-8', errors='ignore') as f:
                f.write(c)
                
        print('Header configuration updated successfully.')
    except Exception as e:
        print(f"Error: {e}")

run()
