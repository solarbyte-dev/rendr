import markdown
import sys
import webbrowser
import os

def render_markdown(file_path):
    # Read the Markdown file
    try:
        with open(file_path, 'r', encoding='utf-8') as markdown_file:
            markdown_content = markdown_file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return
    except Exception as e:
        print(f"Error reading the file: {e}")
        return

    # Convert Markdown to HTML with relevant extensions
    extensions = [
        'tables',           # Enables table support
        'fenced_code',      # Supports fenced code blocks
        'codehilite',       # Syntax highlighting for code
        'footnotes',        # Supports footnotes
        'meta',             # Metadata support
        'sane_lists',       # Makes bullet lists safer
        'toc'               # Table of contents
    ]

    html_content = markdown.markdown(markdown_content, extensions=extensions)

    # Create an HTML output file
    output_file = file_path.rsplit('.', 1)[0] + '.html'
    try:
        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)
        print(f"Rendered HTML is saved as '{output_file}'")
        
        # Open the rendered HTML in the default web browser
        webbrowser.open(f'file://{os.path.abspath(output_file)}')
    except Exception as e:
        print(f"Error writing to the file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python render_markdown.py <path_to_markdown_file>")
    else:
        render_markdown(sys.argv[1])
