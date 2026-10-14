
def greet(name):
    if not name.strip():
        raise ValueError("Name cannot be empty")
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("Student"))
