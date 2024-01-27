from flask import Flask, render_template
import markdown2
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Get the directory containing the markdown files
    content_dir = os.path.join(os.path.dirname(__file__), 'content')
    markdown_files = os.listdir(content_dir)

    # Load and convert content from all Markdown files
    html_content = ""
    for file in markdown_files:
        if file.endswith('.md'):  # Corrected file extension check
            md_file_path = os.path.join(content_dir, file)
            with open(md_file_path, 'r') as md_file:
                content = md_file.read()

            # Convert Markdown to HTML using markdown2 with extras
            html = markdown2.markdown(content, extras=["fenced-code-blocks"])
            html_content += html + "\n"

    return render_template('index.html', content=html_content)

if __name__ == '__main__':
    app.run(debug=True, port=80)
