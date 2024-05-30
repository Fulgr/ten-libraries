import os

def read(data):
    print(data)
    with open(data, "r") as f:
        return f.read()
    
def write(data):
    data = data.split(",")
    filename = data[0]
    content = ','.join(data[1:])
    with open(filename, "w") as f:
        f.write(content)
    return True

def delete(data):
    os.remove(data)
    return True

def exec(data, q):
    if data == "r":
        return read(str(q))
    elif data == "w":
        return write(str(q))
    elif data == "d":
        return delete(str(q))
    return False