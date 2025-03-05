import os
import json
from bs4 import BeautifulSoup

SEARCH_INDEX_FILE = "./search.json"
DOCS_DIR = "./public/"

EXCLUDED_FILE_NAMES = ["genindex.html", "license.html", "search.html", "changelog.html", "py-modindex.html"]

try:
    PACKAGE_DIRS = os.getenv("PACKAGES").split()
except: 
    # Default package directories
    PACKAGE_DIRS= ["iqm-exa-common", "iqm-pulla", "iqm-pulse", "iqm-station-control-client"]


def extract_text_from_html(file_path):
    """Extracts text from <p> elements in an HTML file."""
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
        
        # Extract text from headers and paragraphs
        content = " ".join(
            tag.get_text(" ", strip=True) for tag in soup.find_all(["p"])
        )
        
        title_tag = soup.find("h1")
        title = title_tag.get_text(" ", strip=True) if title_tag else "Untitled"

        return content, title

def build_search_index():
    """Builds a JSON search index from documentation HTML files."""
    search_index = []

    for package in PACKAGE_DIRS:
        package_path = os.path.join(DOCS_DIR, package)

        if not os.path.exists(package_path):
            print(f"⚠️ Warning: Directory {package_path} not found. Skipping...")
            continue
        
        for root, dirs, files in os.walk(package_path):
            
            dirs[:] = [d for d in dirs if not d.startswith(("_", "."))]

            for file in files:
                if file.endswith(".html") and file not in EXCLUDED_FILE_NAMES:
                    file_path = os.path.join(root, file)
                    content, title = extract_text_from_html(file_path)
                    relative_url = os.path.relpath(file_path, DOCS_DIR)

                    search_index.append({
                        "package": package,
                        "title": title,
                        "url": f"/{relative_url}",
                        "description": content[:200] + "...",  
                        "content": content  
                    })
    
    with open(SEARCH_INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(search_index, f, indent=2)
    
    print(f"✅ Search index generated at {SEARCH_INDEX_FILE}")

if __name__ == "__main__":
    build_search_index()
