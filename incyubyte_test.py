def add():

	user_input = input("Enter Numbers: ")
	addition = 0
	addition_char = 0

	for i in user_input:

		if i.isnumeric():
			addition += int(i)

		else:
			val = ord(i)
			val_num = val - 96
			addition_char = addition + val_num
	
	print(addition_char)

add()
