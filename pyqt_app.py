"""PyQt5 Task Manager interface for Omar Khalil's Lab 4 contribution."""

import sys

from PyQt5.QtWidgets import (
    QApplication, QLineEdit, QListWidget, QMessageBox,
    QPushButton, QVBoxLayout, QWidget,
)

from backend import TaskManager


class TaskManagerApp(QWidget):
    """Display tasks and delegate task operations to the shared backend."""

    def __init__(self):
        super().__init__()
        self.task_manager = TaskManager()
        self.setWindowTitle("Task Manager - PyQt")
        self.resize(420, 360)
        self.setMinimumSize(320, 280)

        layout = QVBoxLayout(self)
        self.task_entry = QLineEdit()
        self.task_entry.setPlaceholderText("Enter a task")
        self.task_entry.setAccessibleName("Task description")
        layout.addWidget(self.task_entry)

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.task_entry.returnPressed.connect(self.add_task)
        layout.addWidget(self.add_button)

        self.task_list = QListWidget()
        self.task_list.setAccessibleName("Tasks")
        layout.addWidget(self.task_list)

        self.delete_button = QPushButton("Delete Selected")
        self.delete_button.clicked.connect(self.delete_selected)
        layout.addWidget(self.delete_button)

        self.clear_button = QPushButton("Clear All")
        self.clear_button.clicked.connect(self.clear_tasks)
        layout.addWidget(self.clear_button)

    def refresh_tasks(self):
        """Show the backend's current task list."""
        self.task_list.clear()
        self.task_list.addItems(self.task_manager.get_tasks())

    def add_task(self):
        """Add input through the backend, reporting rejected empty tasks."""
        try:
            self.task_manager.add_task(self.task_entry.text())
        except ValueError:
            QMessageBox.warning(self, "Empty task", "Please enter a task.")
            return
        self.task_entry.clear()
        self.refresh_tasks()
        self.task_entry.setFocus()

    def delete_selected(self):
        """Delete the selected row, or explain that a selection is needed."""
        index = self.task_list.currentRow()
        if index < 0:
            QMessageBox.information(self, "No task selected", "Select a task to delete.")
            return
        self.task_manager.delete_task(index)
        self.refresh_tasks()

    def clear_tasks(self):
        """Clear tasks using the shared backend and refresh the display."""
        self.task_manager.clear_tasks()
        self.refresh_tasks()


def main():
    """Create the application and start the Qt event loop."""
    app = QApplication(sys.argv)
    window = TaskManagerApp()
    window.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
