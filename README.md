# Lab 4 – Git and GitHub Collaboration

## Team Members

- Haya Karanouh — Tkinter
- Omar Khalil — PyQt

## Project Description
This project implements the same Task Manager functionality using Tkinter and
PyQt5 while demonstrating collaborative development with Git and GitHub. Both
interfaces use `backend.py` to add, list, delete, and clear tasks. Empty tasks
are rejected with a warning; deleting without a selection shows an information
message. Tasks are held in memory only. Each running interface has its own task
list; tasks are not saved to disk or synchronized between windows.

## Branches

- feature-tkinter — Haya Karanouh
- feature-pyqt — Omar Khalil

## Project Structure

### backend.py
Contains shared Task Manager logic used by both GUI implementations.

### tkinter_app.py
Tkinter implementation developed by Haya Karanouh.

### pyqt_app.py
PyQt5 interface developed for Omar Khalil's contribution. Includes task input,
Add Task, Delete Selected, Clear All, a task list, and validation dialogs.

### requirements.txt
External dependency required by the PyQt version: PyQt5.

### test_pyqt.py
Automated PyQt functional tests and a compatibility check for the existing Tkinter app.

## Installation

Use Python 3 with Tkinter support. From the repository folder:

```bash
python -m pip install -r requirements.txt
```

Tkinter is included with standard Windows Python installations.

## Running the Tkinter Version

```bash
python tkinter_app.py
```

## Running the PyQt Version

```bash
python pyqt_app.py
```

Enter a description, then click Add Task or press Enter. Select a task before
clicking Delete Selected. Clear All removes every task from the current session.
Closing a window discards its tasks.

## Testing

```bash
python -m unittest -v test_pyqt
```

Eight automated tests passed on Windows with Python 3.13 and PyQt5 5.15.11:
startup, adding and trimming tasks, rejecting empty input, deleting a selected
duplicate by its index, handling no selection, clearing populated/empty lists,
backend delegation, and the unchanged Tkinter interface's basic operations.
Qt tests run offscreen; the Tkinter check requires a desktop session.

## Git Collaboration Workflow

- Haya's Tkinter contribution is on `feature-tkinter`.
- Omar's PyQt contribution must be committed and pushed on `feature-pyqt`,
  created from `main` after Haya's contribution is merged.
- Each feature is integrated into `main` through a reviewed pull request.
- After both PRs are merged, test both interfaces from `main`, complete the
  documentation, and create the final `v1.0` tag and GitHub release.

At preparation time, Haya's branch had not yet been merged and Omar's local
PyQt files had not yet been pushed. Update this status after the actual merges;
the test results above concern the locally combined files.

## Contributions

### Haya Karanouh

- Initial shared repository setup
- Shared backend logic
- Tkinter interface
- Tkinter testing

### Omar Khalil

- PyQt interface using the shared backend
- PyQt dependency configuration
- Automated PyQt testing and Tkinter compatibility verification
- PyQt setup, usage, and testing documentation
