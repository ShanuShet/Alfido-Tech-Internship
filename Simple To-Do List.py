import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple To-Do List")
        self.tasks = []

        self.text = tk.Text(root, width=50, height=18)
        self.text.pack(padx=10, pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Add Task", command=self.add_task).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Remove Task", command=self.remove_task).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Exit", command=root.quit).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Notepad", command=self.open_notepad).pack(side=tk.LEFT, padx=5)
        self.update_tasks()

    def open_notepad(self):
        notepad = tk.Toplevel(self.root)
        notepad.title("Notepad")
        text_area = tk.Text(notepad, width=60, height=20)
        text_area.pack(padx=10, pady=10)
        
    def update_tasks(self):
        self.text.delete(1.0, tk.END)
        if not self.tasks:
            self.text.insert(tk.END, "No tasks in your to-do list.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                self.text.insert(tk.END, f"{idx}. {task}\n")

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter the task:")
        if task and task.strip():
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Store only the task text, not the time
            self.tasks.append(task.strip())
            messagebox.showinfo("Task Added", f"Task added on {now}")
            self.update_tasks()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty.")

    def remove_task(self):
        if not self.tasks:
            messagebox.showinfo("Info", "No tasks to remove.")
            return
        num_str = simpledialog.askstring("Remove Task", "Enter the task number to remove:")
        try:
            num = int(num_str)
            if 1 <= num <= len(self.tasks):
                removed = self.tasks.pop(num - 1)
                messagebox.showinfo("Removed", f"Removed: {removed}")
                self.update_tasks()
            else:
                messagebox.showerror("Error", "Invalid task number.")
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()