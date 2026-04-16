import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class EncryptionToolkitApp:
    def __init__(self, root):
        self.root = root
        self.cipher_var = tk.StringVar(value="Caesar")
        self.mode_var = tk.StringVar(value="Encrypt")
        self.status_var = tk.StringVar(value="Status: Ready")
        self.shift_var = tk.StringVar()
        self.keyword_var = tk.StringVar()
        self.rails_var = tk.StringVar()
        self.active_key_name = "Caesar"

        self._configure_window()
        self._build_layout()
        self._bind_events()
        self._update_key_field()

    def _configure_window(self):
        self.root.title("Encryption Toolkit")
        self.root.geometry("900x650")
        self.root.minsize(700, 500)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

    def _build_layout(self):
        main_frame = ttk.Frame(self.root, padding=16)
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        main_frame.rowconfigure(4, weight=1)

        self._build_options_frame(main_frame)
        self._build_input_frame(main_frame)
        self._build_key_frame(main_frame)
        self._build_button_frame(main_frame)
        self._build_output_frame(main_frame)

    def _build_options_frame(self, parent):
        frame = ttk.LabelFrame(parent, text="Options", padding=12)
        frame.grid(row=0, column=0, sticky="ew")
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(3, weight=1)

        ttk.Label(frame, text="Cipher").grid(row=0, column=0, padx=(0, 8), pady=4, sticky="w")
        self.cipher_box = ttk.Combobox(
            frame,
            textvariable=self.cipher_var,
            values=("Caesar", "Vigenere", "Rail Fence"),
            state="readonly",
        )
        self.cipher_box.grid(row=0, column=1, padx=(0, 16), pady=4, sticky="ew")

        ttk.Label(frame, text="Mode").grid(row=0, column=2, padx=(0, 8), pady=4, sticky="w")
        self.mode_box = ttk.Combobox(
            frame,
            textvariable=self.mode_var,
            values=("Encrypt", "Decrypt", "Brute Force"),
            state="readonly",
        )
        self.mode_box.grid(row=0, column=3, pady=4, sticky="ew")

    def _build_input_frame(self, parent):
        frame = ttk.LabelFrame(parent, text="Input", padding=12)
        frame.grid(row=1, column=0, pady=(12, 0), sticky="nsew")
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1)

        self.upload_button = ttk.Button(frame, text="Upload File")
        self.upload_button.grid(row=0, column=0, pady=(0, 8), sticky="e")

        self.input_text = tk.Text(frame, wrap="word", height=10)
        self.input_text.grid(row=1, column=0, sticky="nsew")

    def _build_key_frame(self, parent):
        frame = ttk.LabelFrame(parent, text="Key", padding=12)
        frame.grid(row=2, column=0, pady=(12, 0), sticky="ew")
        frame.columnconfigure(0, weight=1)

        self.key_fields = {
            "Caesar": self._create_key_row(frame, "Shift", self.shift_var),
            "Vigenere": self._create_key_row(frame, "Keyword", self.keyword_var),
            "Rail Fence": self._create_key_row(frame, "Rails", self.rails_var),
        }

    def _create_key_row(self, parent, label_text, variable):
        frame = ttk.Frame(parent)
        frame.grid(row=0, column=0, sticky="ew")
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text=label_text).grid(row=0, column=0, padx=(0, 8), pady=4, sticky="w")
        entry = ttk.Entry(frame, textvariable=variable)
        entry.grid(row=0, column=1, pady=4, sticky="ew")
        return {"frame": frame, "entry": entry}

    def _build_button_frame(self, parent):
        frame = ttk.Frame(parent, padding=(0, 12, 0, 0))
        frame.grid(row=3, column=0, sticky="ew")
        frame.columnconfigure(3, weight=1)

        self.run_button = ttk.Button(frame, text="Run")
        self.run_button.grid(row=0, column=0, padx=(0, 8))

        self.clear_button = ttk.Button(frame, text="Clear")
        self.clear_button.grid(row=0, column=1, padx=(0, 8))

        self.save_button = ttk.Button(frame, text="Save")
        self.save_button.grid(row=0, column=2)

        self.status_label = tk.Label(frame, textvariable=self.status_var, anchor="w", fg="#333333")
        self.status_label.grid(row=0, column=3, padx=(16, 0), sticky="ew")

    def _build_output_frame(self, parent):
        frame = ttk.LabelFrame(parent, text="Output", padding=12)
        frame.grid(row=4, column=0, pady=(12, 0), sticky="nsew")
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

        self.output_text = tk.Text(frame, wrap="word", height=10, state="disabled")
        self.output_text.grid(row=0, column=0, sticky="nsew")

    def _bind_events(self):
        self.cipher_box.bind("<<ComboboxSelected>>", self._on_cipher_change)
        self.mode_box.bind("<<ComboboxSelected>>", self._on_mode_change)

    def _on_cipher_change(self, event=None):
        if self.cipher_var.get() != "Caesar" and self.mode_var.get() == "Brute Force":
            self.mode_var.set("Encrypt")
        self._update_key_field()

    def _on_mode_change(self, event=None):
        if self.mode_var.get() == "Brute Force" and self.cipher_var.get() != "Caesar":
            self.mode_var.set("Encrypt")
        self._update_key_state()

    def _update_key_field(self):
        for key_field in self.key_fields.values():
            key_field["frame"].grid_remove()

        self.active_key_name = self.cipher_var.get()
        self.key_fields[self.active_key_name]["frame"].grid()
        self._update_key_state()

    def _update_key_state(self):
        for key_field in self.key_fields.values():
            key_field["entry"].configure(state="normal")

        if self.mode_var.get() == "Brute Force":
            self.key_fields[self.active_key_name]["entry"].configure(state="disabled")

    def set_button_commands(self, run_command, clear_command, save_command, upload_command):
        self.run_button.configure(command=run_command)
        self.clear_button.configure(command=clear_command)
        self.save_button.configure(command=save_command)
        self.upload_button.configure(command=upload_command)

    def get_cipher(self):
        return self.cipher_var.get()

    def get_mode(self):
        return self.mode_var.get()

    def get_key_value(self):
        values = {
            "Caesar": self.shift_var,
            "Vigenere": self.keyword_var,
            "Rail Fence": self.rails_var,
        }
        return values[self.cipher_var.get()].get().strip()

    def get_input_text(self):
        return self._get_text(self.input_text)

    def set_input_text(self, content):
        self._replace_text(self.input_text, content)

    def get_output_text(self):
        return self._get_text(self.output_text)

    def set_output_text(self, content):
        self.output_text.configure(state="normal")
        self._replace_text(self.output_text, content)
        self.output_text.configure(state="disabled")

    def clear_all(self):
        self._replace_text(self.input_text, "")
        self.set_output_text("")
        self.shift_var.set("")
        self.keyword_var.set("")
        self.rails_var.set("")
        self.mode_var.set("Encrypt")
        self.cipher_var.set("Caesar")
        self._update_key_field()
        self.set_status("Ready")

    @staticmethod
    def ask_open_file():
        return filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

    @staticmethod
    def ask_save_file():
        return filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")],
        )

    @staticmethod
    def show_error(title, message):
        messagebox.showerror(title, message)

    @staticmethod
    def show_warning(title, message):
        messagebox.showwarning(title, message)

    def set_status(self, status, message=""):
        colors = {
            "Ready": "#333333",
            "Success": "#1f6f43",
            "Error": "#b42318",
        }
        text = f"Status: {status}"
        if message:
            text = f"{text} - {message}"
        self.status_var.set(text)
        self.status_label.configure(fg=colors.get(status, "#333333"))

    def start(self):
        self.root.mainloop()

    @staticmethod
    def _get_text(widget):
        return widget.get("1.0", "end-1c")

    @staticmethod
    def _replace_text(widget, content):
        widget.delete("1.0", "end")
        widget.insert("1.0", content)
