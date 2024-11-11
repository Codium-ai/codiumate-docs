#! /usr/bin/env python3

from pathlib import Path
import os
import re

CONTEXT_FILE_NAME = ".llm_context.txt"
DOCS_DIRECTORY = "docs"


def get_markdown_content(directory):
    """
    Recursively find and concatenate all markdown files in a directory.
    Uses some ad-hoc logic to remove different elemnts:
     - Images
     - Examples.
     - UI tags.
    
    Args:
        directory (str): Path to the directory to search
        
    Returns:
        str: Concatenated content of all markdown files
    """
    markdown_content = ""
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.markdown')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        # Remove all html tags
                        # Stop reading once you encounter a line that starts with a !!!
                        for line in f:
                            if line.startswith("!!!"):
                                break
                            line_content = re.sub(r'<[^>]*>', '', line)
                            line_content = re.sub(r'\{.*?\}', '', line_content)
                            markdown_content += line_content

                except Exception as e:
                    print(f"Error reading {file_path}: {str(e)}")
                    
    # Remove all more than 1 newlines
    markdown_content = re.sub(r'\n{3,}', '\n', markdown_content)
    return markdown_content

if __name__ == "__main__":
    docs_path = Path(__file__).parent.parent / DOCS_DIRECTORY
    markdown_content = get_markdown_content(docs_path)
    with open(CONTEXT_FILE_NAME, "w") as f:
        f.write(markdown_content)
