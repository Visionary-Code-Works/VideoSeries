import os

# Set your GitHub details here
GITHUB_UNAME = "vcwtech"
REPO_NAME = "VideoSeries"
GIT_BRANCH = "main"

START_DIR = "."
OUT_FILE = "github_links.md"
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


def generate_html_links(start_dir, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('<div class="accordion" id="accordionExample">\n')
        part_id = 0
        for part_dir in include_dirs:
            part_id += 1
            file.write(f'  <div class="accordion-item">\n')
            file.write(f'    <h2 class="accordion-header" id="heading{part_id}">\n')
            file.write(f'      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse{part_id}" aria-expanded="true" aria-controls="collapse{part_id}">\n')
            file.write(f'        {part_dir}\n')
            file.write(f'      </button>\n')
            file.write(f'    </h2>\n')
            file.write(f'    <div id="collapse{part_id}" class="accordion-collapse collapse" aria-labelledby="heading{part_id}" data-bs-parent="#accordionExample">\n')
            file.write(f'      <div class="accordion-body">\n')
            file.write(f'        <ul>\n')
            for root, dirs, files in os.walk(os.path.join(start_dir, part_dir)):
                for name in files:
                    rel_path = os.path.relpath(os.path.join(root, name), start_dir)
                    github_link = f"https://github.com/{GITHUB_UNAME}/{REPO_NAME}/blob/{GIT_BRANCH}/{rel_path}"
                    file.write(f'          <li><a href="{github_link}" target="_blank">{name}</a></li>\n')
            file.write(f'        </ul>\n')
            file.write(f'      </div>\n')
            file.write(f'    </div>\n')
            file.write(f'  </div>\n')
        file.write('</div>\n')

generate_html_links(START_DIR, OUT_FILE)



# def generate_github_links(start_dir, output_file):
#     with open(output_file, "w", encoding="utf-8") as file:
#         for part in include_dirs:
#             # Write the header for each part
#             readable_part_name = part.replace("-", " ").title()
#             file.write(f"## {readable_part_name}\n\n")
#             part_dir = os.path.join(start_dir, part)
#             for root, dirs, files in os.walk(part_dir):
#                 for name in files:
#                     # Construct the relative path
#                     rel_path = os.path.relpath(os.path.join(root, name), start_dir)
#                     # Construct the GitHub link
#                     github_link = f"https://github.com/{GITHUB_UNAME}/{REPO_NAME}/blob/{GIT_BRANCH}/{rel_path}"
#                     # Write the link to the output file, organized by subdirectories
#                     indent_level = "    " * (rel_path.count("/") - 1)
#                     file.write(f"{indent_level}- [{name}]({github_link})\n")
#             file.write("\n")  # Add a newline for spacing between parts


# generate_github_links(START_DIR, OUT_FILE)



#         for root, dirs, files in os.walk(start_dir):
#             # Skip directories not in include_dirs
#             if not any(dir_name in root for dir_name in include_dirs):
#                 continue
#             for name in files:
#                 # Construct the relative path
#                 rel_path = os.path.relpath(os.path.join(root, name), start_dir)
#                 # Construct the GitHub link
#                 github_link = f"\
#                     https://github.com/{GITHUB_UNAME}/{REPO_NAME}/blob/{GIT_BRANCH}/{rel_path}"
#                 # Write the link to the output file
#                 file.write(f"- [{rel_path}]({github_link})\n")


# generate_github_links(START_DIR, OUT_FILE)
