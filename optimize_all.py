import os
import re

def update_files():
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update heartbeat
                new_content = re.sub(r'3000 /\* 3s heartbeat \*/', '15000 /* 15s heartbeat optimized */', content)
                
                # Add SEO Meta Tags if missing
                if '<meta name="description"' not in new_content:
                    meta_tags = (
                        '\n    <meta name="description" content="Official Unofficial Academic Notes Portal for BA Calicut University. Access study materials, community chat, and real-time updates.">'
                        '\n    <meta name="keywords" content="Calicut University, BA Notes, Academic Portal, Study Materials">'
                        '\n    <meta name="theme-color" content="#881337">'
                    )
                    new_content = re.sub(r'<title>(.*?)</title>', r'<title>\1</title>' + meta_tags, new_content)
                
                if new_content != content:
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filename}")
            except Exception as e:
                print(f"Error updating {filename}: {e}")

if __name__ == "__main__":
    update_files()
