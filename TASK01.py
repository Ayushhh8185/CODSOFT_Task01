import tkinter as tk
from tkinter import messagebox, simpledialog


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x600")
        self.root.configure(bg="#ffefd5") 

        
        self.title_label = tk.Label(
            root, text="To-Do List", font=("Helvetica", 24, "bold"), bg="#ffefd5", fg="#ff4500"
        )
        self.title_label.pack(pady=10)

        
        self.tasks_listbox = tk.Listbox(
            root, font=("Helvetica", 16), width=25, height=15, bg="#fffacd", fg="#000", selectbackground="#32cd32"
        )
        self.tasks_listbox.pack(pady=20)

        
        self.button_frame = tk.Frame(root, bg="#ffefd5")
        self.button_frame.pack(pady=10)

       
        self.add_button = tk.Button(
            self.button_frame, text="Add Task", font=("Helvetica", 14), bg="#7fffd4", fg="#000", width=12, command=self.add_task
        )
        self.add_button.grid(row=0, column=0, padx=10)
        self.add_button.bind("<Enter>", lambda e: self.on_hover(self.add_button))
        self.add_button.bind("<Leave>", lambda e: self.on_leave(self.add_button))

        
        self.delete_button = tk.Button(
            self.button_frame, text="Delete Task", font=("Helvetica", 14), bg="#ff6347", fg="#fff", width=12, command=self.delete_task
        )
        self.delete_button.grid(row=0, column=1, padx=10)
        self.delete_button.bind("<Enter>", lambda e: self.on_hover(self.delete_button))
        self.delete_button.bind("<Leave>", lambda e: self.on_leave(self.delete_button))

        
        self.complete_button = tk.Button(
            self.button_frame, text="Mark Complete", font=("Helvetica", 14), bg="#1e90ff", fg="#fff", width=12, command=self.mark_complete
        )
        self.complete_button.grid(row=0, column=2, padx=10)
        self.complete_button.bind("<Enter>", lambda e: self.on_hover(self.complete_button))
        self.complete_button.bind("<Leave>", lambda e: self.on_leave(self.complete_button))

    def add_task(self):
        task = tk.simpledialog.askstring("Add Task", "Enter your task:")
        if task:
            self.tasks_listbox.insert(tk.END, task)

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.tasks_listbox.delete(selected_task_index)
        else:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")

    def mark_complete(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            task = self.tasks_listbox.get(selected_task_index)
            self.tasks_listbox.delete(selected_task_index)
            self.tasks_listbox.insert(tk.END, f"{task} (Completed)")
        else:
            messagebox.showwarning("Mark Complete", "Please select a task to mark as complete.")

    def on_hover(self, button):
        button.configure(bg="#ffe4b5")  

    def on_leave(self, button):
        if button == self.add_button:
            button.configure(bg="#7fffd4")
        elif button == self.delete_button:
            button.configure(bg="#ff6347")
        elif button == self.complete_button:
            button.configure(bg="#1e90ff")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
