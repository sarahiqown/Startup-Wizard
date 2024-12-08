# Startup Wizard

**Startup Wizard** is a user-friendly GUI-based tool designed to help you manage your Windows startup programs with ease. It allows you to view, add, and remove programs that launch automatically when your computer starts.

---

## Features

- **View Startup Programs**: See a list of programs currently set to launch at startup, including their names and commands.
- **Add New Programs**: Easily add new programs to the startup list by providing their name and executable command.
- **Remove Existing Programs**: Select and remove programs from the startup list to streamline your system's startup process.
- **Refresh Program List**: Quickly update the displayed list of startup programs to reflect recent changes.

---

## How It Works

1. **Retrieve Startup Programs**: Reads the current startup programs from the Windows Registry.
2. **Modify Startup Settings**: Adds or removes entries in the Registry to manage the startup programs.
3. **Real-Time Updates**: Automatically updates the displayed list when changes are made.

---

## System Requirements

- **Operating System**: Windows 10 or later
- **Python Version**: Python 3.7 or later
- **Dependencies**: None (uses built-in Python modules)

---

## GUI Overview

1. **Program List**: Displays all current startup programs in a table with their names and commands.
2. **Add Program**: Opens a dialog to input the name and command of a new startup program.
3. **Remove Program**: Allows you to remove a selected program from the list.
4. **Refresh Button**: Reloads the program list to show the most up-to-date information.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Disclaimer

Modifying startup programs can affect the performance and behavior of your computer. Ensure that you trust the programs you add to the startup list. The author is not responsible for any issues caused by misuse of this tool.
