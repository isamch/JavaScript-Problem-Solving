import os
import re

# Utility to convert titles to camelCase for function names
def to_camel_case(text):
    parts = text.strip().split()
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])

# Readme path and output folder
readme_path = "Intermediate to Advanced.md"
output_folder = "Intermediate to Advanced"
os.makedirs(output_folder, exist_ok=True)

# Read README.md
with open(readme_path, "r", encoding="utf-8") as file:
    content = file.read()

# Match exercises
pattern = re.compile(
    r"## 🔹 (\d+)\. (.+?)\n\n\*\*Task:\*\* (.+?)\s+"
    r"\*\*Input:\*\* (.+?)\s+"
    r"\*\*Expected Output:\*\* (.+?)(?=\n## 🔹|\Z)",
    re.DOTALL
)

# Generate files
for match in pattern.finditer(content):
    num, title, task, input_text, output_text = match.groups()
    file_number = f"{int(num):02d}"
    file_name = f"{file_number}_{title.strip().replace(' ', '_')}.js"
    file_path = os.path.join(output_folder, file_name)

    function_name = to_camel_case(title)

    file_content = f"""// ## 🔹 {num}. {title.strip()}

// **Task:** {task.strip()}
// **Input:** {input_text.strip()}
// **Expected Output:** {output_text.strip()}

function {function_name}(input) {{
    // TODO: Implement this function
}}

// You can test it like this:
// console.log({function_name}({input_text.strip()}));
"""

    with open(file_path, "w", encoding="utf-8") as js_file:
        js_file.write(file_content)

print("✅ JS files with function skeletons created from README.md.")
