import tkinter as tk
from tkinter import messagebox

from backend import TaskManager


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.task_manager = TaskManager()

        self.root.title("Task Manager")
        self.root.geometry("420x360")
        self.root.minsize(320, 280)

        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack(fill="x", padx=12, pady=(12, 6))

        tk.Button(self.root, text="Add Task", command=self.add_task).pack(
            fill="x", padx=12, pady=4
        )

        self.task_list = tk.Listbox(self.root, selectmode=tk.SINGLE)
        self.task_list.pack(fill="both", expand=True, padx=12, pady=8)

        tk.Button(
            self.root, text="Delete Selected", command=self.delete_selected
        ).pack(fill="x", padx=12, pady=4)
        tk.Button(self.root, text="Clear All", command=self.clear_tasks).pack(
            fill="x", padx=12, pady=(4, 12)
        )

    def refresh_tasks(self):
        self.task_list.delete(0, tk.END)
        for task in self.task_manager.get_tasks():
            self.task_list.insert(tk.END, task)

    def add_task(self):
        try:
            self.task_manager.add_task(self.task_entry.get())
        except ValueError:
            messagebox.showwarning("Empty task", "Please enter a task.")
            return

        self.task_entry.delete(0, tk.END)
        self.refresh_tasks()

    def delete_selected(self):
        selection = self.task_list.curselection()
        if not selection:
            messagebox.showinfo("No task selected", "Select a task to delete.")
            return

        self.task_manager.delete_task(selection[0])
        self.refresh_tasks()

    def clear_tasks(self):
        self.task_manager.clear_tasks()
        self.refresh_tasks()


def main():
    root = tk.Tk()
    TaskManagerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()