def write_file(file_name, file_content):
    """
    Creates a new .txt file (or overwrites if it exists) 
    and writes file_content into it.
    """
    with open(f"{file_name}.txt", "w") as f:
        f.write(file_content)


def append_file(file_name, append_content):
    """
    Opens the .txt file in append mode and adds new content.
    """
    with open(f"{file_name}.txt", "a") as f:
        f.write(append_content)


def read_file(file_name):
    """
    Opens the .txt file in read mode and returns its contents as a string.
    """
    with open(f"{file_name}.txt", "r") as f:
        return f.read()
