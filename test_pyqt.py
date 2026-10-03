"""Functional checks for the PyQt UI and the existing Tkinter interface."""

import os
import unittest
from unittest.mock import patch

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
from PyQt5.QtWidgets import QApplication
from pyqt_app import TaskManagerApp


class PyQtTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def setUp(self):
        self.window = TaskManagerApp()

    def tearDown(self):
        self.window.close()

    def test_startup(self):
        self.window.show()
        self.app.processEvents()
        self.assertTrue(self.window.isVisible())
        self.assertEqual(self.window.task_list.count(), 0)

    def test_add_and_trim(self):
        self.window.task_entry.setText("  Finish Lab 4  ")
        self.window.add_button.click()
        self.assertEqual(self.window.task_manager.get_tasks(), ["Finish Lab 4"])
        self.assertEqual(self.window.task_list.item(0).text(), "Finish Lab 4")
        self.assertEqual(self.window.task_entry.text(), "")

    def test_empty_input(self):
        for text in ("", "   "):
            with self.subTest(text=text), patch("pyqt_app.QMessageBox.warning") as warning:
                self.window.task_entry.setText(text)
                self.window.add_button.click()
                warning.assert_called_once()
                self.assertEqual(self.window.task_manager.get_tasks(), [])

    def test_delete_selected_duplicate_by_index(self):
        for text in ("Same", "Other", "Same"):
            self.window.task_entry.setText(text)
            self.window.add_button.click()
        self.window.task_list.setCurrentRow(2)
        self.window.delete_button.click()
        self.assertEqual(self.window.task_manager.get_tasks(), ["Same", "Other"])
        self.assertEqual(self.window.task_list.count(), 2)

    def test_no_selection(self):
        self.window.task_manager.add_task("Keep this")
        self.window.refresh_tasks()
        with patch("pyqt_app.QMessageBox.information") as info:
            self.window.delete_button.click()
            info.assert_called_once()
        self.assertEqual(self.window.task_manager.get_tasks(), ["Keep this"])

    def test_clear_and_clear_empty(self):
        self.window.task_manager.add_task("Task")
        self.window.refresh_tasks()
        for _ in range(2):
            self.window.clear_button.click()
            self.assertEqual(self.window.task_manager.get_tasks(), [])
            self.assertEqual(self.window.task_list.count(), 0)

    def test_backend_delegation(self):
        with patch.object(self.window.task_manager, "add_task", wraps=self.window.task_manager.add_task) as add:
            self.window.task_entry.setText("Backend task")
            self.window.add_task()
            add.assert_called_once_with("Backend task")
        with patch.object(self.window.task_manager, "delete_task", wraps=self.window.task_manager.delete_task) as delete:
            self.window.task_list.setCurrentRow(0)
            self.window.delete_selected()
            delete.assert_called_once_with(0)
        with patch.object(self.window.task_manager, "clear_tasks", wraps=self.window.task_manager.clear_tasks) as clear:
            self.window.clear_tasks()
            clear.assert_called_once_with()


class TkinterCompatibilityTests(unittest.TestCase):
    def test_existing_tkinter_flow(self):
        import tkinter as tk
        from tkinter_app import TaskManagerApp as TkinterApp
        root = tk.Tk()
        root.withdraw()
        try:
            window = TkinterApp(root)
            root.update_idletasks()
            window.task_entry.insert(0, "Tkinter task")
            window.add_task()
            self.assertEqual(window.task_list.get(0), "Tkinter task")
            window.task_list.selection_set(0)
            window.delete_selected()
            self.assertEqual(window.task_manager.get_tasks(), [])
            window.clear_tasks()
            with patch("tkinter_app.messagebox.showwarning") as warning:
                window.add_task()
                warning.assert_called_once()
            with patch("tkinter_app.messagebox.showinfo") as info:
                window.delete_selected()
                info.assert_called_once()
        finally:
            root.destroy()


if __name__ == "__main__":
    unittest.main()
