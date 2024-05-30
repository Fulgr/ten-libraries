import os

def run(command):
    return os.system(command)

def exec(data, q):
    if data == "o":
        return run(q)
    return False