import tkinter as tk
import sqlite3

# Function to insert data into the database
def insert_data():
    name = name_entry.get()
    age = age_entry.get()
    
    # Insert data into the database
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

    # Clear entry fields after insertion
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

# Function to display data from the database
def display_data():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Create Tkinter window
root = tk.Tk()
root.title("SQL and Tkinter")

# Create labels and entry fields
tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0)
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

# Create buttons
insert_button = tk.Button(root, text="Insert", command=insert_data)
insert_button.grid(row=2, column=0)

display_button = tk.Button(root, text="Display", command=display_data)
display_button.grid(row=2, column=1)

# Connect to the SQLite database
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)''')

# Start the Tkinter event loop
root.mainloop()