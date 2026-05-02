import os
import re
import glob

def fix_downloads():
    html_files = glob.glob("*.html")
    updated_files = 0

    # Pattern for the JS fix block
    old_js_pattern = r'<script>\s+// Global download fix for cross-origin PDF links.*?</script>'
    
    # Advanced JS fix for iOS and cross-origin
    new_js = """<script>
        // Advanced global download handler for iPhone/Mobile and Cross-Origin
        document.addEventListener('click', async (e) => {
            const a = e.target.closest('a[download]');
            if (a && a.href.includes('supabase.co')) {
                // If it's already a blob, let it proceed
                if (a.href.startsWith('blob:')) return;
                
                e.preventDefault();
                const originalContent = a.innerHTML;
                const downloadName = a.getAttribute('download') || 'file.pdf';
                
                try {
                    // Visual feedback
                    a.style.pointerEvents = 'none';
                    a.innerHTML = '<span class="flex items-center justify-center gap-2"><svg class="animate-spin h-4 w-4" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" fill="none"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg> Downloading...</span>';
                    
                    const response = await fetch(a.href, { mode: 'cors' });
                    if (!response.ok) throw new Error('Network response was not ok');
                    
                    const blob = await response.blob();
                    const blobUrl = window.URL.createObjectURL(blob);
                    
                    const tempA = document.createElement('a');
                    tempA.href = blobUrl;
                    tempA.setAttribute('download', downloadName);
                    document.body.appendChild(tempA);
                    tempA.click();
                    document.body.removeChild(tempA);
                    
                    // Cleanup
                    setTimeout(() => {
                        window.URL.revokeObjectURL(blobUrl);
                        a.style.pointerEvents = 'auto';
                        a.innerHTML = originalContent;
                    }, 1000);
                    
                } catch (err) {
                    console.error('Advanced download failed, falling back to server-side:', err);
                    // Fallback to direct redirect with download parameter
                    const url = new URL(a.href);
                    url.searchParams.set('download', downloadName);
                    window.location.href = url.toString();
                    
                    // Reset UI after a delay (since we redirected, this might not even be seen)
                    setTimeout(() => {
                        a.style.pointerEvents = 'auto';
                        a.innerHTML = originalContent;
                    }, 2000);
                }
            }
        });
    </script>"""

    for filepath in html_files:
        if filepath in ['fix_downloads.py', 'revert_ticks.py']: continue
        
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()

        original_content = content

        # 1. Update/Inject the JS block
        if re.search(old_js_pattern, content, flags=re.DOTALL):
            content = re.sub(old_js_pattern, new_js, content, flags=re.DOTALL)
        else:
            if '</body>' in content:
                 # Check if it's a subject page
                 if '-' in filepath or filepath in ['ethics.html', 'kerala.html', 'world.html', 'history.html', 'economics.html', 'sociology.html', 'philosophy.html', 'micro-economics.html']:
                    content = content.replace('</body>', f'{new_js}\n</body>')

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filepath}")
            updated_files += 1

    print(f"\nDone! Updated {updated_files} files.")

if __name__ == "__main__":
    fix_downloads()
