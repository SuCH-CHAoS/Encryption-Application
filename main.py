import tkinter as tk

from ciphers import caesar, rail_fence, vigenere
from gui.interface import EncryptionToolkitApp
from utils.file_handler import read_file, write_file


class EncryptionToolkitController:
    def __init__(self, app):
        self.app = app
        self.app.set_button_commands(
            run_command=self.run_action,
            clear_command=self.clear_fields,
            save_command=self.save_output,
            upload_command=self.upload_file,
        )
        self.app.set_status("Ready")

    def run_action(self):
        text = self.app.get_input_text()
        if not text:
            self.app.set_status("Error", "Please enter or upload text.")
            self.app.show_warning("Missing Input", "Please enter or upload text.")
            return

        try:
            result = self._process_text(text)
        except ValueError as error:
            self.app.set_status("Error", str(error))
            self.app.show_error("Invalid Input", str(error))
            return

        self.app.set_output_text(result)
        self.app.set_status("Success", "Operation completed.")

    def clear_fields(self):
        self.app.clear_all()

    def upload_file(self):
        path = self.app.ask_open_file()
        if not path:
            return

        try:
            self.app.set_input_text(read_file(path))
        except OSError as error:
            self.app.set_status("Error", str(error))
            self.app.show_error("File Error", str(error))
        except ValueError as error:
            self.app.set_status("Error", str(error))
            self.app.show_error("Invalid File", str(error))
        else:
            self.app.set_status("Success", "File loaded.")

    def save_output(self):
        content = self.app.get_output_text()
        if not content:
            self.app.set_status("Error", "There is no output to save.")
            self.app.show_warning("No Output", "There is no output to save.")
            return

        path = self.app.ask_save_file()
        if not path:
            return

        try:
            write_file(path, content)
        except OSError as error:
            self.app.set_status("Error", str(error))
            self.app.show_error("File Error", str(error))
        except ValueError as error:
            self.app.set_status("Error", str(error))
            self.app.show_error("Invalid File", str(error))
        else:
            self.app.set_status("Success", "File saved.")

    def _process_text(self, text):
        cipher = self.app.get_cipher()
        mode = self.app.get_mode()

        if cipher == "Caesar":
            return self._run_caesar(text, mode)
        if cipher == "Vigenere":
            return self._run_vigenere(text, mode)
        return self._run_rail_fence(text, mode)

    def _run_caesar(self, text, mode):
        if mode == "Brute Force":
            return caesar.brute_force(text)

        shift = self._get_number(self.app.get_key_value(), "Shift")
        if mode == "Encrypt":
            return caesar.encrypt_traditional(text, shift)
        return caesar.decrypt_traditional(text, shift)

    def _run_vigenere(self, text, mode):
        if mode == "Brute Force":
            raise ValueError("Brute Force is only available for Caesar.")

        key = self._require_value(self.app.get_key_value(), "Keyword")
        if mode == "Encrypt":
            return vigenere.encrypt_traditional(text, key)
        return vigenere.decrypt_traditional(text, key)

    def _run_rail_fence(self, text, mode):
        if mode == "Brute Force":
            raise ValueError("Brute Force is only available for Caesar.")

        rails = self._get_number(self.app.get_key_value(), "Rails")
        if mode == "Encrypt":
            return rail_fence.encrypt(text, rails)
        return rail_fence.decrypt(text, rails)

    @staticmethod
    def _require_value(value, label):
        if not value:
            raise ValueError(f"{label} is required.")
        return value

    @classmethod
    def _get_number(cls, value, label):
        value = cls._require_value(value, label)
        try:
            return int(value)
        except ValueError as error:
            raise ValueError(f"{label} must be a whole number.") from error


def main():
    root = tk.Tk()
    app = EncryptionToolkitApp(root)
    EncryptionToolkitController(app)
    app.start()


if __name__ == "__main__":
    main()
