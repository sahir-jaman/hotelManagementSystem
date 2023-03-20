import tkinter as tk

root = tk.Tk()
root.geometry("400x200")  # set the size of the window

# create a label for the ID card box
label = tk.Label(root, text="ID Card Box", font=("Arial", 16))
label.pack()

# create a frame to hold the ID card information
frame = tk.Frame(root)
frame.pack(pady=20)

# create labels and entry widgets for each field
tk.Label(frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="ID Number").grid(row=1, column=0, padx=5, pady=5)
id_entry = tk.Entry(frame)
id_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Department").grid(row=2, column=0, padx=5, pady=5)
dept_entry = tk.Entry(frame)
dept_entry.grid(row=2, column=1, padx=5, pady=5)

# create a button to submit the ID card information
def submit():
    name = name_entry.get()
    id_num = id_entry.get()
    dept = dept_entry.get()
    print(f"Name: {name}\nID Number: {id_num}\nDepartment: {dept}")
    
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack(pady=10)

root.mainloop()
