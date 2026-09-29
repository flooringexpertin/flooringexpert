import os
import re

# जिस फोल्डर में फाइल्स हैं (वर्तमान फोल्डर)
DIRECTORY = "."

# कितने पेजों में बदलाव हुआ उसका ट्रैक रखने के लिए
updated_count = 0

for root, dirs, files in os.walk(DIRECTORY):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            original_content = content

            # 1. पुराने Form Tag को हटाकर new ID 'enquiryForm' लगाना
            content = re.sub(
                r'<form\s+action="https://formsubmit\.co/[^"]*"\s+method="POST"',
                '<form id="enquiryForm"',
                content
            )

            # 2. Name और ID Fields को Google Script के हिसाब से अपडेट करना
            # Full Name (name="name" -> name="fullName")
            content = content.replace('for="name"', 'for="fullName"')
            content = content.replace('id="name"', 'id="fullName"')
            content = content.replace('name="name"', 'name="fullName"')

            # Project Details (name="message" -> name="details")
            content = content.replace('for="message"', 'for="details"')
            content = content.replace('id="message"', 'id="details"')
            content = content.replace('name="message"', 'name="details"')

            # 3. Submit Button में id="submitBtn" जोड़ना (अगर पहले से नहीं है)
            if 'id="submitBtn"' not in content:
                content = re.sub(
                    r'<button\s+type="submit"',
                    '<button type="submit" id="submitBtn"',
                    content
                )

            # 4. </body> से ठीक पहले form-handler.js का टैग जोड़ना
            if 'form-handler.js' not in content and '</body>' in content:
                content = content.replace(
                    '</body>',
                    '    <script src="form-handler.js"></script>\n</body>'
                )

            # अगर फाइल में बदलाव हुआ है तो उसे सेव करें
            if content != original_content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"✅ Updated: {filepath}")
                updated_count += 1

print(f"\n🎉 कुल {updated_count} HTML फाइल्स सफलतापूर्वक अपडेट हो गई हैं!")