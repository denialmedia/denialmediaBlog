from flask import Flask, render_template
import markdown2
import os
from flask import Blueprint

app = Flask(__name__)

blueprint = Blueprint(
    'md',
    __name__,
    template_folder='templates',
    static_folder='static'
)

def load_markdown_files(directory):
    """
    Load and convert content from all Markdown files in a given directory.
    Args:
    - directory: Path to the directory containing Markdown files.
    Returns:
    - html_content: Concatenated HTML content of all Markdown files.
    """
    markdown_files = os.listdir(directory)
    markdown_files.sort(reverse=True)  # Sort files in reverse order
    html_content = ""
    for file in markdown_files:
        if file.endswith('.md'):  # Check for .md file extension
            md_file_path = os.path.join(directory, file)
            with open(md_file_path, 'r') as md_file:
                content = md_file.read()
            # Convert Markdown to HTML using markdown2 with extras
            html = markdown2.markdown(content, extras=["fenced-code-blocks"])
            html_content += html + "\n"
    return html_content

@app.route('/')
def index():
    # Get the directory containing the markdown files for the index page
    content_dir = os.path.join(os.path.dirname(__file__), 'content')
    html_content = load_markdown_files(content_dir)
    return render_template('index.html', content=html_content)

@app.route('/projects')
def projects():
    # Get the directory containing the markdown files for the projects page
    content_dir = os.path.join(os.path.dirname(__file__), 'projects')
    html_content = load_markdown_files(content_dir)
    return render_template('projects.html', content=html_content)

if __name__ == '__main__':
    # Bind the app to 0.0.0.0 and the specified port for Render
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))