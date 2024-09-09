#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 13:44:59 2024

@author: bikramgahley
"""

import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

# Initialize a list to store tasks
tasks = []

# Create an entry widget to input tasks
task_entry = tk.Entry(root, width=25)
task_entry.pack(pady=10)

# Create a listbox to display tasks
task_listbox = tk.Listbox(root, width=25, height=10)
task_listbox.pack(pady=10)

# Function to add a task
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
        tasks.pop(selected_task_index)
    except IndexError:
        pass

# Save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()
                tasks.append(task)
                task_listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

# Load tasks when the app starts
load_tasks()

# Create buttons to add and delete tasks
add_button = tk.Button(root, text="Add Task", width=15, command=lambda: add_task())
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=lambda: delete_task())
delete_button.pack(pady=5)

# Save tasks when the window is closed
root.protocol("WM_DELETE_WINDOW", lambda: (save_tasks(), root.destroy()))

# Start the main loop
root.mainloop()
