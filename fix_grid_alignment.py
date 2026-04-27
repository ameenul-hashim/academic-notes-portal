import os
import re

def fix_grid_break_and_align(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix the extra </div> in "Content Coming Soon" blocks
    # The block ends with 6 closing tags in some cases, or 5 when it should be 4 before the chapter div ends.
    # Looking at the code, it has:
    # </div> (closes text-center)
    # </div> (closes flex flex-col)
    # </div> (closes glass-card modal body)
    # </div> (closes modal-chX)
    # </div> (closes chapter wrapper)
    # </div> (EXTRA - CLOSES GRID)
    
    # We need to find the block and ensure it doesn't close the grid.
    # The pattern is:
    # </div>\n                        </div>\n                        </div>\n                    </div>\n                </div>\n            </div>
    # That's 6 divs. Let's see if we can find it.
    
    # Actually, a more robust way is to count the tags in the "Content Coming Soon" section.
    pattern = r'(<div class="text-center p-8 rounded-2xl bg-gradient-to-br from-rose-900/40 to-red-950/40.*?)</div>\s*</div>\s*</div>\s*</div>\s*</div>\s*</div>'
    
    # We want to replace it with 5 divs instead of 6.
    # 1: text-center, 2: flex-col, 3: glass-card (modal), 4: modal-chX, 5: chapter wrapper
    replacement = r'\1</div>\n                        </div>\n                        </div>\n                    </div>\n                </div>'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    # 2. Force same height and width for ALL chapter cards
    # Search for the clickable glass-card and set a fixed height
    # Pattern: class="glass-card ... cursor-pointer ..."
    # We'll set h-48 and flex items-center justify-center
    
    pattern_card = r'class="glass-card ([^"]*?cursor-pointer[^"]*?)"'
    def fix_card_size(match):
        classes = match.group(1)
        # Remove any existing min-h, h-, p- classes to start fresh
        classes = re.sub(r'min-h-\[?\d+px\]?', '', classes)
        classes = re.sub(r'h-\d+', '', classes)
        classes = re.sub(r'p-\d+', '', classes)
        # Add fixed height and padding
        return f'class="glass-card h-48 flex items-center justify-center p-6 {classes.strip()}"'

    new_content = re.sub(pattern_card, fix_card_size, new_content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

# List all html files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

updated_count = 0
for html_file in html_files:
    if fix_grid_break_and_align(html_file):
        updated_count += 1
        print(f"Fixed & Aligned: {html_file}")

print(f"Total files updated: {updated_count}")
