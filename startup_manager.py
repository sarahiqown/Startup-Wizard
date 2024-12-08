import tkinter as tk
from tkinter import messagebox, ttk
import subprocess

class StartupManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Startup Wizard")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.create_widgets()

        # Load startup programs
        self.startup_programs = self.get_startup_programs()
        self.update_program_list()

    def create_widgets(self):
        # Header Label
        header_label = tk.Label(self.root, text="Startup Wizard", font=("Arial", 18, "bold"))
        header_label.pack(pady=10)

        # Treeview to display startup programs
        self.tree = ttk.Treeview(self.root, columns=("Name", "Command"), show="headings", height=12)
        self.tree.heading("Name", text="Program Name")
        self.tree.heading("Command", text="Command")
        self.tree.column("Name", width=200)
        self.tree.column("Command", width=350)
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10, fill=tk.X)

        add_button = tk.Button(button_frame, text="Add Program", command=self.add_program, width=15)
        add_button.pack(side=tk.LEFT, padx=5)

        remove_button = tk.Button(button_frame, text="Remove Program", command=self.remove_program, width=15)
        remove_button.pack(side=tk.LEFT, padx=5)

        refresh_button = tk.Button(button_frame, text="Refresh", command=self.refresh_programs, width=15)
        refresh_button.pack(side=tk.LEFT, padx=5)

    def get_startup_programs(self):
        """Retrieve the list of startup programs using Windows Registry."""
        try:
            reg_query = 'reg query "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"'
            result = subprocess.run(reg_query, shell=True, capture_output=True, text=True)
            lines = result.stdout.strip().split("\n")
            programs = []

            for line in lines[1:]:
                parts = line.split("    ")
                if len(parts) >= 3:
                    name = parts[0].strip()
                    command = parts[2].strip()
                    programs.append((name, command))

            return programs
        except Exception as e:
            messagebox.showerror("Error", f"Failed to retrieve startup programs: {e}")
            return []

    def update_program_list(self):
        """Update the treeview with the list of startup programs."""
        self.tree.delete(*self.tree.get_children())

        for program in self.startup_programs:
            self.tree.insert("", "end", values=program)

    def add_program(self):
        """Add a new program to the startup list."""
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Startup Program")
        add_window.geometry("400x200")

        tk.Label(add_window, text="Program Name:").pack(pady=5)
        name_entry = tk.Entry(add_window, width=40)
        name_entry.pack(pady=5)

        tk.Label(add_window, text="Command:").pack(pady=5)
        command_entry = tk.Entry(add_window, width=40)
        command_entry.pack(pady=5)

        def save_program():
            name = name_entry.get().strip()
            command = command_entry.get().strip()
            if name and command:
                try:
                    reg_add = f'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "{name}" /d "{command}" /f'
                    subprocess.run(reg_add, shell=True, check=True)
                    self.refresh_programs()
                    messagebox.showinfo("Success", f"{name} added to startup programs!")
                    add_window.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to add program: {e}")
            else:
                messagebox.showwarning("Input Error", "Please provide both name and command.")

        tk.Button(add_window, text="Add Program", command=save_program).pack(pady=10)

    def remove_program(self):
        """Remove a selected program from the startup list."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a program to remove.")
            return

        program_name = self.tree.item(selected_item, "values")[0]
        try:
            reg_delete = f'reg delete "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v "{program_name}" /f'
            subprocess.run(reg_delete, shell=True, check=True)
            self.refresh_programs()
            messagebox.showinfo("Success", f"{program_name} removed from startup programs!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to remove program: {e}")

    def refresh_programs(self):
        """Refresh the list of startup programs."""
        self.startup_programs = self.get_startup_programs()
        self.update_program_list()


if __name__ == "__main__":
    root = tk.Tk()
    app = StartupManagerApp(root)
    root.mainloop()
