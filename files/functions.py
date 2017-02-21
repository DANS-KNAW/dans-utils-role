import os

def version_from_textfile(path):
    if os.path.isfile(path):
        with open(path, 'r') as myfile:
            return myfile.read().strip()
    else:
        return None
