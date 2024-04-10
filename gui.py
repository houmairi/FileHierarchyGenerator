import sys
import traceback
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QFileDialog, QMessageBox, QComboBox, QTreeView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from file_hierarchy_generator import create_file_hierarchy, get_python_project_structure, get_csharp_project_structure, get_cpp_project_structure

class FileHierarchyGeneratorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.hidden_folders = set()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Language selection
        language_layout = QHBoxLayout()
        language_label = QLabel("Select language:")
        self.language_combo = QComboBox()
        self.language_combo.addItems(["Python", "C#", "C++"])
        self.language_combo.currentTextChanged.connect(self.update_file_hierarchy)
        language_layout.addWidget(language_label)
        language_layout.addWidget(self.language_combo)
        layout.addLayout(language_layout)

        # Input label and text edit
        input_layout = QHBoxLayout()
        input_label = QLabel("File hierarchy:")
        self.input_text = QTextEdit()
        self.input_text.setReadOnly(True)  # Make the input text read-only
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_text)
        layout.addLayout(input_layout)
        
        # File hierarchy tree view
        hierarchy_layout = QHBoxLayout()
        hierarchy_label = QLabel("File hierarchy:")
        self.hierarchy_tree = QTreeView()
        hierarchy_layout.addWidget(hierarchy_label)
        hierarchy_layout.addWidget(self.hierarchy_tree)
        layout.addLayout(hierarchy_layout)

        # Output directory label and button
        output_layout = QHBoxLayout()
        output_label = QLabel("Select output directory:")
        self.output_dir = QLabel("")
        output_button = QPushButton("Browse")
        output_button.clicked.connect(self.browse_output_dir)
        output_layout.addWidget(output_label)
        output_layout.addWidget(self.output_dir)
        output_layout.addWidget(output_button)
        layout.addLayout(output_layout)

        # Copy file hierarchy button
        copy_layout = QHBoxLayout()
        copy_label = QLabel("Copy file hierarchy from:")
        self.copy_dir = QLabel("")
        copy_button = QPushButton("Browse")
        copy_button.clicked.connect(self.browse_copy_dir)
        copy_layout.addWidget(copy_label)
        copy_layout.addWidget(self.copy_dir)
        copy_layout.addWidget(copy_button)
        layout.addLayout(copy_layout)
        
        # Hide folders layout
        hide_folders_layout = QHBoxLayout()
        hide_folders_label = QLabel("Select folders to hide:")
        self.hide_folders_text = QTextEdit()
        hide_folders_layout.addWidget(hide_folders_label)
        hide_folders_layout.addWidget(self.hide_folders_text)
        layout.addLayout(hide_folders_layout)
        
        # Hide selected folders
        self.input_text = QTextEdit()
        self.input_text.setMouseTracking(True)
        self.input_text.mousePressEvent = self.on_input_text_mouse_press

        # Generate button
        generate_button = QPushButton("Generate")
        generate_button.clicked.connect(self.generate_file_hierarchy)
        layout.addWidget(generate_button)

        self.setLayout(layout)
        self.setWindowTitle("File Hierarchy Generator")

    def browse_output_dir(self):
        output_dir = QFileDialog.getExistingDirectory(self, "Select Output Directory")
        if output_dir:
            self.output_dir.setText(output_dir)

    def browse_copy_dir(self):
        copy_dir = QFileDialog.getExistingDirectory(self, "Select Directory to Copy")
        if copy_dir:
            self.copy_dir.setText(copy_dir)
            print(f"Selected directory: {copy_dir}")  # Add this print statement
            self.update_file_hierarchy()
            
    def on_input_text_mouse_press(self, event):
        if event.modifiers() == Qt.ControlModifier:
            cursor = self.input_text.cursorForPosition(event.pos())
            cursor.select(QTextCursor.LineUnderCursor)
            selected_text = cursor.selectedText().strip()
            if selected_text.endswith('/'):
                self.toggle_hidden_folder(selected_text[:-1])
        else:
            QTextEdit.mousePressEvent(self.input_text, event)
            
    def toggle_hidden_folder(self, folder):
        if folder in self.hidden_folders:
            self.hidden_folders.remove(folder)
        else:
            self.hidden_folders.add(folder)
        self.update_hidden_folders_text()
        self.update_file_hierarchy()
        
    def update_hidden_folders_text(self):
        self.hide_folders_text.setPlainText('\n'.join(sorted(self.hidden_folders)))

    def generate_file_hierarchy_string(self, directory):
        hierarchy = []
        hide_folders = self.hide_folders_text.toPlainText().split('\n')
        for root, dirs, files in os.walk(directory):
            level = root.replace(directory, '').count(os.sep)
            indent = ' ' * 4 * level
            folder_name = os.path.basename(root)
            if folder_name not in hide_folders:
                hierarchy.append(f"{indent}{folder_name}/")
                subindent = ' ' * 4 * (level + 1)
                for file in files:
                    hierarchy.append(f"{subindent}{file}")
        generated_hierarchy = '\n'.join(hierarchy)
        print(f"Generated Hierarchy:\n{generated_hierarchy}")  # Add this print statement
        return generated_hierarchy

    def update_file_hierarchy(self):
        print("Updating file hierarchy...")
        hierarchy = self.generate_file_hierarchy_string(self.copy_dir.text())
        transformed_hierarchy = self.transform_hierarchy(hierarchy)
        print(f"Transformed Hierarchy:\n{transformed_hierarchy}")

        model = QStandardItemModel()
        self.hierarchy_tree.setModel(model)

        def populate_tree(parent_item, hierarchy_lines):
            current_level = 0
            stack = [(parent_item, current_level)]

            for line in hierarchy_lines:
                if not line.strip():
                    continue

                item_indent_level = len(line) - len(line.lstrip())
                item_text = line.strip()

                while stack and item_indent_level <= stack[-1][1]:
                    stack.pop()

                if item_text.endswith("/"):
                    item = QStandardItem(item_text[:-1])
                    item.setEditable(False)
                    if stack:
                        stack[-1][0].appendRow(item)
                    else:
                        parent_item.appendRow(item)
                    stack.append((item, item_indent_level))
                else:
                    item = QStandardItem(item_text)
                    item.setEditable(False)
                    if stack:
                        stack[-1][0].appendRow(item)
                    else:
                        parent_item.appendRow(item)

        populate_tree(model.invisibleRootItem(), transformed_hierarchy.split("\n"))
        self.hierarchy_tree.expandAll()

    def generate_file_hierarchy(self):
        hierarchy = self.input_text.toPlainText()
        output_dir = self.output_dir.text()
        output_dir = os.path.normpath(output_dir)  # Normalize the directory path

        if not hierarchy.strip() or not output_dir:
            QMessageBox.warning(self, "Warning", "Please enter the file hierarchy and select an output directory.")
            return

        try:
            # Transform the hierarchy
            transformed_hierarchy = self.transform_hierarchy(hierarchy)
            print(f"Output directory: {output_dir}")  # Print the output directory path
            create_file_hierarchy(output_dir, transformed_hierarchy)
            QMessageBox.information(self, "Success", "File hierarchy generated successfully.")
        except FileNotFoundError as e:
            print(f"Error: {str(e)}")  # Print the error message
            print(f"Traceback: {traceback.format_exc()}")  # Print the traceback
            QMessageBox.critical(self, "Error", f"Directory not found: {output_dir}")
        except ValueError as e:
            print(f"Error: {str(e)}")  # Print the error message
            print(f"Traceback: {traceback.format_exc()}")  # Print the traceback
            QMessageBox.critical(self, "Error", f"Invalid file hierarchy:\n{str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")  # Print the error message
            print(f"Traceback: {traceback.format_exc()}")  # Print the traceback
            QMessageBox.critical(self, "Error", f"An error occurred:\n{str(e)}")

    def transform_hierarchy(self, hierarchy):
        lines = hierarchy.split("\n")
        transformed_lines = []

        for line in lines:
            line = line.strip()
            if line and not any(folder in line for folder in self.hidden_folders):
                transformed_lines.append(line)

        return "\n".join(transformed_lines)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    generator_gui = FileHierarchyGeneratorGUI()
    generator_gui.show()
    sys.exit(app.exec_())