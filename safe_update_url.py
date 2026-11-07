import os

# --- CONFIGURATION ---
TARGET_DIR = "."

# Purana Google Sheet Script URL
OLD_URL = "https://script.google.com/macros/s/AKfycbw_JA84a_GnEr5JwRac1H4FaMqb3Qm8Dcc4DsbDk5VC2dkAuZP3KeIrKt_Z7iS3arDF/exec"

# Naya Google Sheet Script URL
NEW_URL = "https://script.google.com/macros/s/AKfycbz4jfjZMR4E2oNUhfHwpJoa1HdM482qTAhmLypsadyafQHIDbiIRUdrSLCcIMl5XnCY/exec"

def update_script_url():
    updated_files = 0
    skipped_files = 0

    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Sirf URL string ko check aur replace karna
                if OLD_URL in content:
                    new_content = content.replace(OLD_URL, NEW_URL)
                    
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                        
                    print(f"[SUCCESS] Updated URL in: {file_path}")
                    updated_files += 1
                else:
                    skipped_files += 1

    print(f"\n--- Summary ---")
    print(f"Updated Files: {updated_files}")
    print(f"Skipped / Already Updated: {skipped_files}")

if __name__ == "__main__":
    update_script_url()