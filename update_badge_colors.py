import os
import re

BADGE_STYLE = """
        /* Upload Status Badge Overrides */
        /* Red Badges (0 Uploaded) */
        [data-theme="light"] .bg-red-500\/20 { background-color: rgba(239, 68, 68, 0.15) !important; }
        [data-theme="light"] .text-red-300 { color: #b91c1c !important; border-color: rgba(185, 28, 28, 0.2) !important; }
        [data-theme="emerald"] .text-red-300 { color: #fca5a5 !important; }

        /* Yellow Badges (Partial) */
        [data-theme="light"] .bg-yellow-500\/20 { background-color: rgba(245, 158, 11, 0.15) !important; }
        [data-theme="light"] .text-yellow-300 { color: #b45309 !important; border-color: rgba(180, 83, 9, 0.2) !important; }
        [data-theme="rose"] .text-yellow-300 { color: #fde68a !important; }

        /* Green Badges (Complete) */
        [data-theme="light"] .bg-green-500\/20 { background-color: rgba(34, 197, 94, 0.15) !important; }
        [data-theme="light"] .text-green-300 { color: #15803d !important; border-color: rgba(21, 128, 61, 0.2) !important; }
"""

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Inject before </style>
    if BADGE_STYLE not in content:
        content = content.replace('</style>', BADGE_STYLE + '</style>')

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Updated Note Upload Status badge colors for better theme compatibility.")
