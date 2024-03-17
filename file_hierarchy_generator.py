import os
import re
import argparse

def is_valid_name(name):
    """
    Check if a given name (file or directory) is valid.
    It should only contain alphanumeric characters, underscores, hyphens, dots, and forward slashes.
    """
    return re.match(r'^[a-zA-Z0-9_\-\.\/]+$', name) is not None

def validate_structure(structure):
    """
    Validate the structure of the file hierarchy.
    Check for invalid names and duplicate directories.
    Raise a ValueError if any issues are found.
    """
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

def create_file_hierarchy(directory, structure):
    """
    Create the file hierarchy based on the provided structure.
    Validate the structure before creating the files and directories.
    """
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

def get_python_project_structure():
    """
    Return the project structure for a Python project.
    """
    return """
src/
    __init__.py
    main.py
tests/
    __init__.py
    test_main.py
requirements.txt
README.md
"""

def get_csharp_project_structure():
    """
    Return the project structure for a C# project.
    """
    return """
src/
    Program.cs
    MyApp.csproj
tests/
    MyAppTests.cs
    MyAppTests.csproj
README.md
"""

def get_cpp_project_structure():
    """
    Return the project structure for a C++ project.
    """
    return """
src/
    main.cpp
    Makefile
include/
    myapp.h
tests/
    test_main.cpp
README.md
"""

def main():
    """
    Main function to handle command-line arguments and generate the file hierarchy.
    """
    parser = argparse.ArgumentParser(description='File Hierarchy Generator')
    parser.add_argument('-l', '--language', choices=['python', 'csharp', 'cpp'], help='Programming language')
    parser.add_argument('-o', '--output', default='.', help='Output directory')
    parser.add_argument('structure', nargs='?', help='File hierarchy structure')

    args = parser.parse_args()

    if args.language:
        if args.language == 'python':
            structure = get_python_project_structure()
        elif args.language == 'csharp':
            structure = get_csharp_project_structure()
        elif args.language == 'cpp':
            structure = get_cpp_project_structure()
    else:
        structure = args.structure

    if structure:
        try:
            create_file_hierarchy(args.output, structure)
            print("File hierarchy generated successfully.")
        except ValueError as e:
            print(f"Error: {str(e)}")
    else:
        print("Please provide a file hierarchy structure or specify a programming language.")

if __name__ == '__main__':
    main()