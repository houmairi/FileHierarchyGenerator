import os

def create_file_hierarchy(directory, structure):
    for item in structure.split("\n"):
        item = item.strip()
        if not item or item.endswith("..."):
            continue

        path = os.path.join(directory, item)
        if item.endswith("/"):
            os.makedirs(path, exist_ok=True)
        else:
            open(path, "w").close()

# Get the file hierarchy from user input
print("Enter the file hierarchy (use indentation for subdirectories, empty line to finish):")
lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line)

hierarchy = "\n".join(lines)

# Create the file hierarchy
create_file_hierarchy(".", hierarchy)
print("File hierarchy created successfully.")