import os
import re

DIRECTORY = "."
updated_count = 0

# Regex patterns
FORM_REGEX = re.compile(
    r'<form\b[^>]*action=["\']https://formsubmit\.co/[^"\']*["\'][^>]*>',
    re.IGNORECASE
)
NAME_REGEX = re.compile(r'\b(for|id|name)=["\']name["\']', re.IGNORECASE)
MESSAGE_REGEX = re.compile(r'\b(for|id|name)=["\']message["\']', re.IGNORECASE)
SUBMIT_BTN_REGEX = re.compile(r'<button\s+([^>]*type=["\']submit["\'][^>]*)>', re.IGNORECASE)
BODY_REGEX = re.compile(r'</body>', re.IGNORECASE)

SCRIPT_TAG = '    <script src="https://flooringexpert.in/form-handler.js"></script>\n</body>'

for root, dirs, files in os.walk(DIRECTORY):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                original_content = content

                # 1. Purane Form tag ko id="enquiryForm" se replace karein
                content = FORM_REGEX.sub('<form id="enquiryForm">', content)

                # 2. Form fields ko Google Script ke hisab se rename karein
                content = NAME_REGEX.sub(r'\1="fullName"', content)
                content = MESSAGE_REGEX.sub(r'\1="details"', content)

                # 3. Submit Button me id="submitBtn" jodein
                if 'id="submitBtn"' not in content and "id='submitBtn'" not in content:
                    def add_btn_id(match):
                        attrs = match.group(1)
                        if 'id=' not in attrs.lower():
                            return f'<button id="submitBtn" {attrs}>'
                        return match.group(0)
                    
                    content = SUBMIT_BTN_REGEX.sub(add_btn_id, content)

                # 4. </body> se theek pehle form-handler.js Script Tag jodein
                if 'form-handler.js' not in content and BODY_REGEX.search(content):
                    content = BODY_REGEX.sub(SCRIPT_TAG, content, count=1)

                # Save changes if modified
                if content != original_content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"✅ Updated: {filepath}")
                    updated_count += 1

            except Exception as e:
                print(f"❌ Error in {filepath}: {e}")

print(f"\n🎉 Total {updated_count} HTML files automatically updated across all folders!")