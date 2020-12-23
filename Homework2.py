first_name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
year_of_birth = int(input("Enter your birthday: "))
my_list = []

my_list.append(first_name)
my_list.append(last_name)
my_list.append(age)
my_list.append(year_of_birth)

for i in range(len(my_list)):
    print(my_list[i])

if (age < 18):
    print("You can't go out because it's too dangerous.")
else:
    print("You can go out to the street.")
