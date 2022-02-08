print("Enter a number 4 times")
my_list = []

my_list.append(int(input("1. ")))
my_list.append(int(input("2. ")))
my_list.append(int(input("3. ")))
my_list.append(int(input("4. ")))

#print(my_list)

print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

my_list[0], my_list[3] = my_list[3], my_list[0]

#print(my_list)