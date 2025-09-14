text = "hello"

# # Method 1: Slicing
# rev1 = text[::-1]   
# print(rev1)   # "olleh"


# # Method 2: reversed() + join()
# rev2 = "".join(reversed(text))
# print(rev2)   # "olleh"


# Method 3: Loop (manual method)
# rev3 = ""
# for ch in text:
#     rev3 = ch + rev3
# print(rev3)   # "olleh"



