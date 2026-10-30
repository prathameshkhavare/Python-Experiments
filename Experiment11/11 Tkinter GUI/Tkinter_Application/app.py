import re
import tkinter as tk
from tkinter import messagebox, ttk

EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
PHONE_PATTERN = re.compile(r"^\+?[0-9]{10,15}$")


def register_student():
    name = name_var.get().strip()
    email = email_var.get().strip()
    phone = phone_var.get().strip()
    course = course_var.get().strip()

    if not name:
        messagebox.showerror("Invalid input", "Enter the student's name.")
        return
    if not EMAIL_PATTERN.fullmatch(email):
        messagebox.showerror("Invalid input", "Enter a valid email address.")
        return
    if not PHONE_PATTERN.fullmatch(phone):
        messagebox.showerror("Invalid input", "Enter a phone number with 10 to 15 digits.")
        return
    if not course:
        messagebox.showerror("Invalid input", "Select a course.")
        return

    messagebox.showinfo("Registration complete", f"Name: {name}\nEmail: {email}\nPhone: {phone}\nCourse: {course}")
    name_var.set("")
    email_var.set("")
    phone_var.set("")
    course_var.set("")


root = tk.Tk()
root.title("Student Registration")
root.geometry("440x390")
root.resizable(False, False)

name_var = tk.StringVar()
email_var = tk.StringVar()
phone_var = tk.StringVar()
course_var = tk.StringVar()

container = ttk.Frame(root, padding=24)
container.pack(fill="both", expand=True)
ttk.Label(container, text="Student Registration", font=("Segoe UI", 18, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 18))
ttk.Label(container, text="Name").grid(row=1, column=0, sticky="w", pady=6)
ttk.Entry(container, textvariable=name_var, width=32).grid(row=1, column=1, sticky="ew", pady=6)
ttk.Label(container, text="Email").grid(row=2, column=0, sticky="w", pady=6)
ttk.Entry(container, textvariable=email_var, width=32).grid(row=2, column=1, sticky="ew", pady=6)
ttk.Label(container, text="Phone").grid(row=3, column=0, sticky="w", pady=6)
ttk.Entry(container, textvariable=phone_var, width=32).grid(row=3, column=1, sticky="ew", pady=6)
ttk.Label(container, text="Course").grid(row=4, column=0, sticky="w", pady=6)
ttk.Combobox(container, textvariable=course_var, values=("Python", "Data Science", "Web Development", "Computer Networks"), state="readonly", width=29).grid(row=4, column=1, sticky="ew", pady=6)
ttk.Button(container, text="Register", command=register_student).grid(row=5, column=0, columnspan=2, sticky="ew", pady=(20, 8))
ttk.Label(container, text="Email and phone entries are checked before registration.").grid(row=6, column=0, columnspan=2, sticky="w", pady=(8, 0))
container.columnconfigure(1, weight=1)
root.mainloop()
