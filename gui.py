import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QFileDialog, QMessageBox, QComboBox
from file_hierarchy_generator import create_file_hierarchy, get_python_project_structure, get_csharp_project_structure, get_cpp_project_structure

class FileHierarchyGeneratorGUI(QWidget):
    def __init__(self):
        super().__init__()
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
        input_layout.addWidget(input_label)
        input_layout.addWidget(self.input_text)
        layout.addLayout(input_layout)

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

    def update_file_hierarchy(self, language):
        if language == "Python":
            self.input_text.setPlainText(get_python_project_structure())
        elif language == "C#":
            self.input_text.setPlainText(get_csharp_project_structure())
        elif language == "C++":
            self.input_text.setPlainText(get_cpp_project_structure())

    def generate_file_hierarchy(self):
        hierarchy = self.input_text.toPlainText()
        output_dir = self.output_dir.text()

        if not hierarchy.strip() or not output_dir:
            QMessageBox.warning(self, "Warning", "Please enter the file hierarchy and select an output directory.")
            return

        try:
            create_file_hierarchy(output_dir, hierarchy)
            QMessageBox.information(self, "Success", "File hierarchy generated successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    generator_gui = FileHierarchyGeneratorGUI()
    generator_gui.show()
    sys.exit(app.exec_())