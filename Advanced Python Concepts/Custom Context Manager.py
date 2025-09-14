# 🔹 5. Custom Context Manager (function se — contextlib)

from contextlib import contextmanager

@contextmanager
def open_file(file, mode):
    f = open(file, mode)
    try:
        yield f
    finally:
        f.close()
        print("File closed")

with open_file("demo2.txt", "w") as f:
    f.write("This is via contextlib!")       


# 🔹 6. Real-Life Uses

# File Handling → with open("file.txt") as f:
# Database Connection → ensure connection closes
# Threading Locks → with lock:
# Resource Management → sockets, network calls


# 🔹 7. Summary

# with statement = context manager use karna
# Automatic resource cleanup (close/release)
# Do ways:
# Class ke saath (__enter__, __exit__)
# Function + @contextmanager