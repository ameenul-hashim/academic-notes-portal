import os

def revert_ticks():
    checkmark_path = 'd="M5 13l4 4L19 7"'
    updated_files = []
    
    for filename in os.listdir('.'):
        if filename.endswith('.html'):
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if 'text-red-400' in content and checkmark_path in content:
                    new_content = content.replace('text-red-400', 'text-green-400')
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    updated_files.append(filename)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                
    print(f"Reverted {len(updated_files)} files to green ticks.")

if __name__ == "__main__":
    revert_ticks()
