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