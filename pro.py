import tkinter as tk
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(
    host="your_mysql_host",
    user="your_mysql_user",
    password="your_mysql_password",
    database="your_database_name"
)

cursor = db.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")

def login():
    username = entry_username.get()
    password = entry_password.get()

record in the database
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Login", "Login successful!")
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

root = tk.Tk()
root.title("Login Page")

label_username = tk.Label(root, text="Username:")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password:")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

btn_login = tk.Button(root, text="Login", command=login)
btn_login.pack()

root.mainloop()
