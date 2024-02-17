import os

# Set your GitHub details here
github_username = "thomasthaddeus"
repository_name = "VideoSeries"
branch_name = "main"

# Directory to start from
start_dir = "."  # Assuming the script is run from the root of your project

# Output HTML file to write the links to
output_file = "file_links_dropdown.html"

# List of directories to include
include_dirs = [
    "part-01-intro-to-python",
    "part-02-data-types-and-structures",
    "part-03-control-structures",
    "part-04-functions-and-modules",
    "part-05-advanced-data-structures",
    "part-06-object-oriented-programming",
    "part-07-error-and-exception-handling",
    "part-08-file-handling-and-io",
    "part-09-external-libraries-and-tools",
    "part-10-python-in-practice",
    "part-11-advanced-topics",
    "part-12-final-project",
]


def generate_html_dropdowns(start_dir, output_file):
    dropdown_html = ""
    for part_dir in include_dirs:
        part_path = os.path.join(start_dir, part_dir)
        if not os.path.exists(part_path):
            continue
        dropdown_html += f"<h2>{part_dir}</h2>\n"
        dropdown_html += f'<select onchange="location = this.value;">\n'
        dropdown_html += '<option value="">Select a file...</option>\n'
        for root, dirs, files in os.walk(part_path):
            for name in files:
                rel_path = os.path.relpath(os.path.join(root, name), start_dir)
                github_link = f"https://github.com/{github_username}/{repository_name}/blob/{branch_name}/{rel_path}"
                dropdown_html += (
                    f'    <option value="{github_link}">{rel_path}</option>\n'
                )
        dropdown_html += "</select>\n\n"

    # Add JavaScript for handling selection
    html_content = f"""
<html>
<head>
    <title>File Links</title>
</head>
<body>
    {dropdown_html}
    <script>
        document.querySelectorAll('select').forEach(selectElement => {{
            selectElement.addEventListener('change', function() {{
                const url = this.value;
                if(url) {{
                    window.location.href = url;
                }}
            }});
        }});
    </script>
</body>
</html>
    """

    with open(output_file, "w") as file:
        file.write(html_content)


generate_html_dropdowns(start_dir, output_file)
