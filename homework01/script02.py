# Name: Sresha Ventrapragada
# UT EID: svv346
import names

count = 0
while (count < 5):
	current_name = names.get_full_name()
	if (len(current_name) == 9):
		print(current_name)
		count = count + 1
