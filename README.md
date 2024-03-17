# File Hierarchy Generator

File Hierarchy Generator is a versatile tool designed to streamline the process of creating structured file hierarchies for your projects. With support for multiple programming languages, including Python, C#, and C++, this tool allows you to automatically generate a base project structure with just a few commands. It's an ideal solution for developers looking to kickstart their projects without the hassle of manually creating directories and files.

Hint: File hierarchies can easily be created with Language-Specific Markup Schemas (LLMS) such as CHATGPT, Claude, Gemini, and many others, which you can then paste into this tool, which creates the given file hierarchy.

## Features

- [x] Support for generating file structures for Python, C#, and C++ projects.
- [x] Command-line interface (CLI) for easy integration into automated workflows or build systems.
- [x] Ability to ustomize the file hierarchy as per your project needs.
- [x] Simple, yet powerful, validation to ensure correct file and directory names.

## Getting Started

### Prerequisites

Before running the File Hierarchy Generator, ensure you have the following installed:

    Python 3.x

### Installation

    Clone this repository or download the source code from the releases section.
    Navigate to the directory containing file_hierarchy_generator.py.

## Usage

### GUI

1. Run gui.exe.
2. Select programming language from dropdown.
3. Customize file hierarchy in text area (optional).
4. Click "Browse" to choose output directory.
5. Click "Generate" to create file hierarchy.

Here is the template for python projects, which can be selected in the GUI (for understanding purposes):
```
MyProject/
    src/
        __init__.py
        main.py
    tests/
        __init__.py
        test_main.py
    requirements.txt
    README.md
```
6. Success or error message will be displayed.
7. Close the application when done.

### CLI

To use the File Hierarchy Generator, you can run the file_hierarchy_generator.py script with the following CLI commands:

Generate a file hierarchy for a specific programming language:

```python file_hierarchy_generator.py -l <language> -o <output_directory>```

Replace <language> with one of the supported programming languages: python, csharp, or cpp. Specify the desired output directory with <output_directory>.

Example:
```python file_hierarchy_generator.py -l python -o my_project```

Generate a custom file hierarchy:

```python file_hierarchy_generator.py -o <output_directory> "<file_hierarchy_structure>"```

Provide the desired file hierarchy structure as a string, using newlines to separate directories and files. Specify the desired output directory with <output_directory>.

Example:
```
python file_hierarchy_generator.py -o my_project "src/
main.py
README.md"
```

Note: Make sure to enclose the file hierarchy structure string in quotes to preserve the newlines.

Get help and view available options:

```python file_hierarchy_generator.py -h```

This command displays the available options and their descriptions.

## Troubleshooting

If you encounter any issues with invalid file names or duplicate directories, please review the error message provided and adjust your file hierarchy accordingly. For other issues, check if your Python installation is up to date.

## Contributing

Contributions are welcome! If you'd like to improve the File Hierarchy Generator or add support for more languages, please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
