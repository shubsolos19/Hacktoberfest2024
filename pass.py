import tkinter as tk

def toggle():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_button.config(text='Show')
    else:
        password_entry.config(show='')
        toggle_button.config(text='Hide')

root = tk.Tk()
password_entry = tk.Entry(root, show='*')
password_entry.pack(pady=10)

toggle_button = tk.Button(root, text="Show", command=toggle)
toggle_button.pack(pady=5)

root.mainloop()
