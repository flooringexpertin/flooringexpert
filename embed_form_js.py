import os
import re

# Folder path (Current Directory)
DIRECTORY = "."

# Aapka JS Code inline embed karne ke liye
INLINE_JS_SNIPPET = """<!-- Form Inline Handler Start -->
<script>
const SCRIPT_URL = "https://script.google.com/macros/s/AKfycbw_JA84a_GnEr5JwRac1H4FaMqb3Qm8Dcc4DsbDk5VC2dkAuZP3KeIrKt_Z7iS3arDF/exec"; 

document.addEventListener("DOMContentLoaded", function() {
  const enquiryForm = document.getElementById("enquiryForm");
  const submitBtn = document.getElementById("submitBtn");

  if (enquiryForm) {
    enquiryForm.addEventListener("submit", function(e) {
      e.preventDefault();

      if (submitBtn) {
        submitBtn.innerText = "Submitting...";
        submitBtn.disabled = true;
      }

      // Meta Pixel Lead event
      if (typeof fbq === 'function') {
        fbq('track', 'Lead');
      }

      const formData = new FormData(enquiryForm);

      fetch(SCRIPT_URL, {
        method: "POST",
        body: formData
      })
      .then(response => {
        redirectToThankYou();
      })
      .catch(error => {
        console.error("Error submitting form:", error);
        redirectToThankYou();
      });
    });
  }
});

function redirectToThankYou() {
  setTimeout(() => {
    const hostname = window.location.hostname;
    
    // 1. Agar Custom Domain (flooringexpert.in) par hai
    if (hostname.includes("flooringexpert.in")) {
      window.location.href = "/thank-you.html";
    } 
    // 2. Agar GitHub Pages (username.github.io/flooringexpert) par hai
    else if (hostname.includes("github.io")) {
      window.location.href = "/flooringexpert/thank-you.html";
    } 
    // 3. Local Machine ya normal relative structure ke liye
    else {
      const pathSegments = window.location.pathname.split('/').filter(Boolean);
      // Agar kisi subfolder ke andar hain toh ../ lagakar root par bhejega
      const depth = pathSegments.length > 1 ? pathSegments.length - 1 : 0;
      const prefix = depth > 0 ? "../".repeat(depth) : "./";
      window.location.href = prefix + "thank-you.html";
    }
  }, 200);
}
</script>
<!-- Form Inline Handler End -->"""

# External form-handler.js tag remove karne ke liye Regex
EXTERNAL_SCRIPT_REGEX = re.compile(
    r'\s*<script\b[^>]*src=["\'][^"\']*form-handler\.js["\'][^>]*>\s*</script>',
    re.IGNORECASE
)

BODY_REGEX = re.compile(r'</body>', re.IGNORECASE)

updated_count = 0

for root, dirs, files in os.walk(DIRECTORY):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                original_content = content

                # 1. Purane external form-handler.js script tags hataayein
                content = EXTERNAL_SCRIPT_REGEX.sub('', content)

                # 2. Agar code pehle se added nahi hai toh embed karein
                if "<!-- Form Inline Handler Start -->" not in content:
                    if BODY_REGEX.search(content):
                        content = BODY_REGEX.sub(f"{INLINE_JS_SNIPPET}\n</body>", content, count=1)
                    else:
                        content += f"\n{INLINE_JS_SNIPPET}"

                # Save file if modified
                if content != original_content:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"✅ Updated: {filepath}")
                    updated_count += 1

            except Exception as e:
                print(f"❌ Error in {filepath}: {e}")

print(f"\n🎉 Total {updated_count} HTML files automatically updated with inline JS code!")