import os
import re

DROPDOWN_FIX_CSS = """
        /* Dropdown visibility fix */
        #theme-selector {
            color: white !important;
            background-color: rgba(0,0,0,0.5) !important;
        }
        #theme-selector option {
            background-color: #1a1a2e !important;
            color: white !important;
        }
        [data-theme="light"] #theme-selector {
            color: #212529 !important;
            background-color: rgba(255,255,255,0.8) !important;
            border-color: rgba(0,0,0,0.2) !important;
        }
        [data-theme="light"] #theme-selector option {
            background-color: white !important;
            color: #212529 !important;
        }
"""

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Inject fix before </style>
    if DROPDOWN_FIX_CSS not in content:
        content = content.replace('</style>', DROPDOWN_FIX_CSS + '</style>')

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Fixed dropdown text visibility across all themes.")
