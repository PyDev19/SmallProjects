import tkinter as tk
from tkinter import ttk
from googletrans import LANGUAGES, Translator

translator = Translator()

def on_translate():
    input_lang = [i for i in LANGUAGES if LANGUAGES[i] == input_lang_choice.get().lower()][0]
    output_lang = [i for i in LANGUAGES if LANGUAGES[i] == language_choice.get().lower()][0]
    
    input_text_str = input_text.get("1.0", tk.END)
    
    translated_text = translator.translate(input_text_str, src=input_lang, dest=output_lang)
    
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated_text.text)
    output_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Translator")
root.geometry("500x500")
root.config(bg="#f4f4f9")

label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 10)
button_font = ("Helvetica", 12, "bold")

input_frame = tk.Frame(root, bg="#f4f4f9", padx=10, pady=10)
input_frame.pack(fill=tk.X)

input_language = tk.Label(input_frame, text="Select Input Language:", font=label_font, bg="#f4f4f9")
input_language.grid(row=0, column=0, sticky="w")
input_lang_choice = ttk.Combobox(input_frame, values=[lang.capitalize() for lang in LANGUAGES.values()], font=entry_font)
input_lang_choice.grid(row=0, column=1, padx=10, pady=5)
input_lang_choice.set('English')

text_input_frame = tk.Frame(root, bg="#f4f4f9", padx=10, pady=10)
text_input_frame.pack(fill=tk.X)

input_label = tk.Label(text_input_frame, text="Enter text to translate:", font=label_font, bg="#f4f4f9")
input_label.grid(row=0, column=0, sticky="w")

input_text = tk.Text(text_input_frame, height=5, width=60, font=entry_font)
input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

input_scrollbar = tk.Scrollbar(text_input_frame)
input_scrollbar.grid(row=1, column=2, sticky="ns")
input_text.config(yscrollcommand=input_scrollbar.set)
input_scrollbar.config(command=input_text.yview)

output_frame = tk.Frame(root, bg="#f4f4f9", padx=10, pady=10)
output_frame.pack(fill=tk.X)

language_label = tk.Label(output_frame, text="Select Target Language:", font=label_font, bg="#f4f4f9")
language_label.grid(row=0, column=0, sticky="w")
language_choice = ttk.Combobox(output_frame, values=[lang.capitalize() for lang in LANGUAGES.values()], font=entry_font)
language_choice.grid(row=0, column=1, padx=10, pady=5)

translate_button = tk.Button(root, text="Translate", font=button_font, bg="#4CAF50", fg="white", command=on_translate)
translate_button.pack(pady=10)

output_text_frame = tk.Frame(root, bg="#f4f4f9", padx=10, pady=10)
output_text_frame.pack(fill=tk.X)

output_label = tk.Label(output_text_frame, text="Translated text:", font=label_font, bg="#f4f4f9")
output_label.grid(row=0, column=0, sticky="w")

output_text = tk.Text(output_text_frame, height=5, width=60, font=entry_font)
output_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5)
output_text.config(state=tk.DISABLED)

output_scrollbar = tk.Scrollbar(output_text_frame)
output_scrollbar.grid(row=1, column=2, sticky="ns")
output_text.config(yscrollcommand=output_scrollbar.set)
output_scrollbar.config(command=output_text.yview)

root.mainloop()
