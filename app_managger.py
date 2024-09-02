import subprocess

def open_application(path):
    try:
        subprocess.Popen(path)
        return f"Opened application at {path}"
    except Exception as e:
        return str(e)
