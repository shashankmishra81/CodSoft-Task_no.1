import tkinter as tk
from tkinter import messagebox

class TodoList:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(master, width=50)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)
        
        self.task_listbox = tk.Listbox(master, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=0, columnspan=2, pady=5)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please enter a task.")
    
    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        except IndexError:
            messagebox.showerror("Error", "No task selected.")

def main():
    root = tk.Tk()
    todo_list = TodoList(root)
    root.mainloop()

if __name__ == "__main__":
    main()
