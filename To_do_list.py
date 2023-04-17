import tkinter as tk
from tkinter import messagebox

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List")
        self.geometry("400x400")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        self.task_entry = tk.Entry(self, width=50)
        self.task_entry.pack(padx=5, pady=5)

        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.pack(padx=5, pady=5)

        self.listbox = tk.Listbox(self, width=50, height=15)
        self.listbox.pack(padx=5, pady=5)

        self.remove_button = tk.Button(self, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(padx=5, pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_listbox()
        else:
            messagebox.showerror("Error", "Please select a task to remove.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
