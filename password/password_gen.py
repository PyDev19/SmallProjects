import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_var.get())
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_numbers = number_var.get()
    use_special = special_var.get()

    if not (use_upper or use_lower or use_numbers or use_special):
        messagebox.showerror("Input Error", "You must select at least one character type.")
        return

    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_numbers:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    result_var.set(password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x250")
root.configure(bg="#F4F4F9")

length_var = tk.StringVar(value="8")
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
number_var = tk.BooleanVar()
special_var = tk.BooleanVar()
result_var = tk.StringVar()

font = ("Helvetica", 12)
button_font = ("Helvetica", 12, "bold")

tk.Label(root, text="Password Length:", font=font, bg="#F4F4F9").grid(row=0, column=0, padx=10, pady=10, sticky="w")
tk.Entry(root, textvariable=length_var, font=font, width=5).grid(row=0, column=1, padx=10, pady=10, sticky="w")

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var, font=font, bg="#F4F4F9").grid(row=1, column=0, columnspan=2, sticky="w", padx=10)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var, font=font, bg="#F4F4F9").grid(row=2, column=0, columnspan=2, sticky="w", padx=10)
tk.Checkbutton(root, text="Include Numbers", variable=number_var, font=font, bg="#F4F4F9").grid(row=3, column=0, columnspan=2, sticky="w", padx=10)
tk.Checkbutton(root, text="Include Special Characters", variable=special_var, font=font, bg="#F4F4F9").grid(row=4, column=0, columnspan=2, sticky="w", padx=10)

tk.Button(root, text="Generate Password", font=button_font, bg="#0D99FF", fg="white", command=generate_password).grid(row=5, column=0, columnspan=2, pady=20)

tk.Entry(root, textvariable=result_var, state='readonly', font=font, width=30, bd=0, bg="#E0E0E0", justify="center").grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
