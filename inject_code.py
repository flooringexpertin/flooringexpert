import os

# 1. Yahan apne project folder ka path dalein (Jahan saari HTML files rakhi hain)
# Agar python file project folder ke andar hi hai toh current directory '.' use karein.
PROJECT_DIRECTORY = "."

# 2. Wo code/snippet jo aapko sabhi HTML pages me add karna hai
SNIPPET_TO_ADD = """
<!-- Form Inline Handler Start -->
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
    if (hostname.includes("flooringexpert.in")) {
      window.location.href = "/thank-you.html";
    } else if (hostname.includes("github.io")) {
      window.location.href = "/flooringexpert/thank-you.html";
    } else {
      const pathSegments = window.location.pathname.split('/').filter(Boolean);
      const depth = pathSegments.length > 1 ? pathSegments.length - 1 : 0;
      const prefix = depth > 0 ? "../".repeat(depth) : "./";
      window.location.href = prefix + "thank-you.html";
    }
  }, 200);
}
</script>
<!-- Form Inline Handler End -->
"""

def inject_code_to_html():
    updated_count = 0
    skipped_count = 0

    # Directory ke saare folders aur files ko scan karna
    for root, dirs, files in os.walk(PROJECT_DIRECTORY):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()

                    # Check karein ki snippet pehle se file me mojud hai ya nahi
                    if "Form Inline Handler Start" in content:
                        print(f"Skipped (Already exists): {file_path}")
                        skipped_count += 1
                        continue

                    # </body> tag se theek pehle snippet inject karna
                    if "</body>" in content:
                        new_content = content.replace("</body>", f"\n{SNIPPET_TO_ADD}\n</body>")
                        
                        with open(file_path, "w", encoding="utf-8") as f:
                            f.write(new_content)
                            
                        print(f"Successfully Added: {file_path}")
                        updated_count += 1
                    else:
                        print(f"Warning: </body> tag not found in {file_path}")

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    print("\n--- Summary ---")
    print(f"Total Files Updated: {updated_count}")
    print(f"Total Files Skipped: {skipped_count}")

if __name__ == "__main__":
    inject_code_to_html()