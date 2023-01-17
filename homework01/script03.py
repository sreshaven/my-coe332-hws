# Name: Sresha Ventrapragada
# UT EID: svv346
import names

def get_char_length(full_name):
    length = 0
    for char in full_name:
        if char != ' ':
            length += 1
    return length

names_list = []

for _ in range(5):
    names_list.append(names.get_full_name())

for name in names_list:
    print(name, get_char_length(name))
