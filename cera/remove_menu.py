import os
import re
from bs4 import BeautifulSoup

# Project ka directory path ('.' ka matlab current folder)
PROJECT_DIR = "."

def clean_html_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    modified = False

    # 1. Desktop Menu: "Architectural Surfaces" dropdown container ko remove karein
    for span in soup.find_all("span"):
        if "Architectural Surfaces" in span.get_text():
            # Parent container dhoondo jo dropdown ko wrap kar raha hai
            parent = span.find_parent("div", class_=lambda c: c and "relative" in c and "group" in c)
            if parent:
                parent.decompose()
                modified = True
                break

    # 2. Mobile Menu: "Architectural Surfaces" accordion (<details>) ko remove karein
    for summary in soup.find_all("summary"):
        if "Architectural Surfaces" in summary.get_text():
            details_tag = summary.find_parent("details")
            if details_tag:
                details_tag.decompose()
                modified = True
                break

    # Agar file me match mila aur remove hua, toh save karein
    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"[REMOVED] -> {file_path}")
    else:
        print(f"[SKIPPED / NOT FOUND] -> {file_path}")

def process_all_files():
    count = 0
    for root, dirs, files in os.walk(PROJECT_DIR):
        for file in files:
            if file.endswith(".html"):
                full_path = os.path.join(root, file)
                clean_html_file(full_path)
                count += 1
    print(f"\nDone! Total {count} HTML files check ki gayi.")

if __name__ == "__main__":
    process_all_files()