# File Hierarchy Generator

File Hierarchy Generator is a versatile tool designed to streamline the process of creating structured file hierarchies for your projects. With support for multiple programming languages, including Python, C#, and C++, this tool allows you to automatically generate a base project structure with just a few clicks. It's an ideal solution for developers looking to kickstart their projects without the hassle of manually creating directories and files.

## Features

- Support for generating file structures for Python, C#, and C++ projects.
- Easy-to-use graphical user interface (GUI) for seamless operation.
- Ability to customize the file hierarchy as per your project needs.
- Simple, yet powerful, validation to ensure correct file and directory names.
- File hierarchies can easily be created with Language-Specific Markup Schemas (LLMS) such as CHATGPT, Claude, Gemini, and many others.

## Getting Started

### Prerequisites

Before running the File Hierarchy Generator, ensure you have the following installed:

- Python 3.x
- PyQt5

### Installation

1. Clone this repository or download the executable from the releases section.
2. If you've cloned the repository, navigate to the directory containing `file_hierarchy_generator.py` and `gui.py`.

### Running the Tool

To run File Hierarchy Generator, simply execute the provided executable. If you're running from source, execute the following command:

```
python gui.py
```

This will launch the graphical user interface of the File Hierarchy Generator.

## Usage

1. **Select the programming language**: Upon launching the tool, select the target programming language for your project structure from the dropdown menu.
2. **Customize the file hierarchy (optional)**: The tool pre-populates a recommended structure based on your selected language. You can customize this structure in the provided text area.
3. **Select the output directory**: Click the "Browse" button to choose the directory where you want to generate the file hierarchy.
4. **Generate the file hierarchy**: Click the "Generate" button to create your project structure. You'll receive a success message once the process is complete.

## Troubleshooting

If you encounter any issues with invalid file names or duplicate directories, please review the error message provided and adjust your file hierarchy accordingly. For other issues, check if your Python and PyQt5 installations are up to date.

## Contributing

Contributions are welcome! If you'd like to improve the File Hierarchy Generator or add support for more languages, please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
