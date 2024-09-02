import os

def list_files(directory):
    try:
        return os.listdir(directory)
    except Exception as e:
        return str(e)

def create_file(file_name, content=""):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        return f"{file_name} created successfully."
    except Exception as e:
        return str(e)

def delete_file(file_name):
    try:
        os.remove(file_name)
        return f"{file_name} deleted successfully."
    except Exception as e:
        return str(e)
