class TaskManager:
    """Store and manage task descriptions for the GUI applications."""

    def __init__(self):
        self._tasks = []

    def add_task(self, task):
        task = task.strip()
        if not task:
            raise ValueError("Task cannot be empty.")
        self._tasks.append(task)
        return task

    def get_tasks(self):
        return self._tasks.copy()

    def delete_task(self, index):
        del self._tasks[index]

    def clear_tasks(self):
        self._tasks.clear()