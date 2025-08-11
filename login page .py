#tkinter is pacakge that is useful to python's GUI toolkit
import tkinter as tk
#popup dialog boxes to genarate-alters,messages and notifications
from tkinter import messagebox

# Sample credentials (in real apps, use a secure database)
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

# Function to validate login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

# Create main window
# login page and bigger window  
root = tk.Tk()
root.title("Login Page")
root.geometry("300x180")

# Username label and entry
tk.Label(root, text="Username").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack()

# Password label and entry
tk.Label(root, text="Password").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Login button
tk.Button(root, text="Login", command=login).pack(pady=15)

# Run the application
root.mainloop()
