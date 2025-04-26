# Python To-Do List

A simple command-line to-do list application built in Python. This application allows you to add, modify, check-off, and list tasks from the terminal.

## Features

- Add Tasks
- Modify Tasks
- Check-off Tasks
- List Tasks

## Prerequisites

- Python 3.x or higher

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Troaxx/toDoList.git
   cd toDoList
   ```

2. No additional dependencies required, this project only uses Python's standard library.

## Usage

Run the application using:
```bash
python toDoList.py
```

## Example Session

```
Welcome to the To-Do List menu! Select from one of the options below:
        [1] Add/Modify Task
        [2] List out tasks
        [3] Quit
Enter in your choice: [1/2/3] 1
Select an option: [a] - Add Task | [b] - Remove/Check off Task | [c] - Edit Task | [d] - Undo Task
a
Enter Task Name: Write 500 word essay
Added task: 'Write 500 word essay' ! 

Welcome to the To-Do List menu! Select from one of the options below:
        [1] Add/Modify Task
        [2] List out tasks
        [3] Quit
Enter in your choice: [1/2/3] 2
Here are your tasks:
1. Write 500 word essay

Welcome to the To-Do List menu! Select from one of the options below:
        [1] Add/Modify Task
        [2] List out tasks
        [3] Quit
Enter in your choice: [1/2/3] 1
Select an option: [a] - Add Task | [b] - Remove/Check off Task | [c] - Edit Task | [d] - Undo Task
c
Enter the title of the task you'd like to edit (Case Sensitive): Write 500 word essay
Enter the new title of the task: Write 600 word essay
'Write 500 word essay' has been changed to 'Write 600 word essay'.

Welcome to the To-Do List menu! Select from one of the options below:
        [1] Add/Modify Task
        [2] List out tasks
        [3] Quit
Enter in your choice: [1/2/3] 2
Here are your tasks:
1. Write 600 word essay

Welcome to the To-Do List menu! Select from one of the options below:
        [1] Add/Modify Task
        [2] List out tasks
        [3] Quit
Enter in your choice: [1/2/3]
```

## Project Structure
```
├── toDoList.py      # Main application file
├── README.md        # Documentation
└── LICENSE          # MIT License
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
