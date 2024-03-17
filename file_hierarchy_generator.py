import os

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
    for item in structure.split("\n"):
        item = item.strip()
        if not item:
            continue

        path = os.path.join(directory, item)
        if item.endswith("/"):
            os.makedirs(path, exist_ok=True)
        else:
            open(path, "w").close()