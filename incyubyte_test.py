def add():

	user_input = input("Enter Numbers: ")
	user_in_list = user_input.split(',')
	print(user_in_list)
	addition = 0
	addition_char = 0
	val_sum = 0
	for i in user_in_list:

		if i.isdigit():
			int_num = int(i)

			if int_num < 1000:
				addition += int_num

		else :
			val = ord(i)
			val_num = val - 96
			val_sum += val_num

		addition_char = addition + val_sum

	print(addition_char)

add()
