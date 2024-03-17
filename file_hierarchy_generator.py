import os
import re

def is_valid_name(name):
    return re.match(r'^[a-zA-Z0-9_\-\.]+$', name) is not None

def validate_structure(structure):
    directories = set()
    for item in structure.split("\n"):
        item = item.strip()
        if not item:
            continue

        if not is_valid_name(item):
            raise ValueError(f"Invalid name: {item}")

        if item.endswith("/"):
            if item[:-1] in directories:
                raise ValueError(f"Duplicate directory: {item}")
            directories.add(item[:-1])

def get_python_project_structure():
    return """src/
    __init__.py
    main.py
tests/
    __init__.py
    test_main.py
requirements.txt
README.md
"""

def get_csharp_project_structure():
    return """src/
    Program.cs
    MyApp.csproj
tests/
    MyAppTests.cs
    MyAppTests.csproj
README.md
"""

def get_cpp_project_structure():
    return """src/
    main.cpp
    Makefile
include/
    myapp.h
tests/
    test_main.cpp
README.md
"""

def create_file_hierarchy(directory, structure):
    validate_structure(structure)

    for item in structure.split("\n"):
        item = item.strip()
        if not item:
            continue

        path = os.path.join(directory, item)
        if item.endswith("/"):
            os.makedirs(path, exist_ok=True)
        else:
            open(path, "w").close()