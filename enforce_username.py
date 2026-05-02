import os

def enforce_username():
    # Protection script that redirects users without a username
    check_script = """
    <script>
        (function() {
            if (!localStorage.getItem('portal-username')) {
                alert("Access Denied: Please set a username in the portal first!");
                window.location.href = 'index.html';
            }
        })();
    </script>
"""
    
    count = 0
    for filename in os.listdir('.'):
        # Apply to all HTML files except the landing page
        if filename.endswith('.html') and filename != 'index.html':
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Skip if already protected
                if 'portal-username' in content and 'window.location.href' in content:
                    continue
                
                # Inject right after the <head> tag for fastest execution
                if '<head>' in content:
                    new_content = content.replace('<head>', f'<head>{check_script}')
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Protected: {filename}")
                    count += 1
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    
    print(f"\nSuccessfully enforced username on {count} pages.")

if __name__ == "__main__":
    enforce_username()
