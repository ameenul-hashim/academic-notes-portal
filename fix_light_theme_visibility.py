import os
import re

# Replacing Sky/Emerald Light with "Desert Gold" (Light Theme)
# And fixing visibility for all light themes
REFINED_LIGHT_THEMES = """
        /* Light Theme Visibility Fixes */
        [data-theme="light"] {
            --text-light: #0f172a !important;
            --accent-light: #1d4ed8 !important;
        }
        [data-theme="sky"] {
            --bg-sky: linear-gradient(to bottom right, #fffbeb, #fef3c7) !important;
            --text-sky: #451a03 !important;
            --accent-sky: #92400e !important;
        }

        /* Force dark text for all light-mode classes */
        [data-theme="light"] .text-white, [data-theme="light"] .text-gray-100, [data-theme="light"] .text-gray-200, [data-theme="light"] .text-orange-200, [data-theme="light"] .text-pink-200 { 
            color: #0f172a !important; 
        }
        [data-theme="sky"] .text-white, [data-theme="sky"] .text-gray-100, [data-theme="sky"] .text-gray-200, [data-theme="sky"] .text-orange-200, [data-theme="sky"] .text-pink-200 { 
            color: #451a03 !important; 
        }
        
        /* Dropdown options for light themes */
        [data-theme="light"] #theme-selector option, [data-theme="sky"] #theme-selector option {
            background-color: white !important;
            color: black !important;
        }
"""

NEW_OPTIONS = """<option value="rose">Reddish Brown</option>
                    <option value="midnight">Midnight Purple</option>
                    <option value="ocean">Ocean Blue</option>
                    <option value="golden">Golden Amber</option>
                    <option value="coffee">Warm Coffee</option>
                    <option value="sunset">Sunset Glow</option>
                    <option value="indigo">Deep Indigo</option>
                    <option value="forest">Forest Deep</option>
                    <option value="chocolate">Chocolate Dark</option>
                    <option value="slate">Slate Minimal</option>
                    <option value="emerald">Emerald Green</option>
                    <option value="dark">Navy Blue</option>
                    <option value="light">Classic Light</option>
                    <option value="sky">Desert Gold (Light)</option>"""

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update dropdown
    if '<select id="theme-selector"' in content:
        content = re.sub(r'<option value="rose">.*?</select>', NEW_OPTIONS + '\n                </select>', content, flags=re.DOTALL)

    # 2. Inject visibility fixes before </style>
    if REFINED_LIGHT_THEMES not in content:
        content = content.replace('</style>', REFINED_LIGHT_THEMES + '</style>')

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Replaced Sky with Desert Gold and fixed light theme visibility.")
