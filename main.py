import tkinter as tk
from tkinter import ttk, messagebox
from translator import translate_text, LANGUAGES

def on_translate():
    text = input_text.get("1.0", tk.END).strip()
    src_lang = lang_dict[src_lang_var.get()]
    dest_lang = lang_dict[dest_lang_var.get()]
    if not text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return
    try:
        translated_text = translate_text(text, src_lang, dest_lang)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))

root = tk.Tk()
root.title("Language Translation Tool")

# Convert LANGUAGES dictionary to a sorted list of language names and create a reverse lookup dictionary
languages = sorted(LANGUAGES.items(), key=lambda x: x[1])
lang_names = [name for code, name in languages]
lang_dict = {name: code for code, name in languages}

# Source language selection
tk.Label(root, text="Source Language:").grid(row=0, column=0, padx=10, pady=10)
src_lang_var = tk.StringVar(value='english')
src_lang_menu = ttk.Combobox(root, textvariable=src_lang_var, values=lang_names)
src_lang_menu.grid(row=0, column=1, padx=10, pady=10)

# Destination language selection
tk.Label(root, text="Destination Language:").grid(row=1, column=0, padx=10, pady=10)
dest_lang_var = tk.StringVar(value='spanish')
dest_lang_menu = ttk.Combobox(root, textvariable=dest_lang_var, values=lang_names)
dest_lang_menu.grid(row=1, column=1, padx=10, pady=10)

# Input text
tk.Label(root, text="Enter Text:").grid(row=2, column=0, padx=10, pady=10)
input_text = tk.Text(root, height=10, width=40)
input_text.grid(row=2, column=1, padx=10, pady=10)

# Translate button
translate_button = tk.Button(root, text="Translate", command=on_translate)
translate_button.grid(row=3, column=1, padx=10, pady=10)

# Output text
tk.Label(root, text="Translated Text:").grid(row=4, column=0, padx=10, pady=10)
output_text = tk.Text(root, height=10, width=40)
output_text.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
