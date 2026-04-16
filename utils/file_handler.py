def _validate_txt_path(path):
    if not str(path).lower().endswith(".txt"):
        raise ValueError("Only .txt files are supported.")
    return path


def read_file(path):
    path = _validate_txt_path(path)
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def write_file(path, content):
    path = _validate_txt_path(path)
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
