numbers = [1,2,3]
#to increase each element by 1 using keyword
new_number = [n + 1 for n in numbers]
#sequence
new_range = [n * 2 for n in range(1, 5)]
#conditional comprehension of list
names = ["Alex", "Bath", "caroline", "Dave", "Eleanor", "Freddle", "Kessie"]
short_name = [name for name in names if len(name) < 5]
long_name = [name.upper() for name in names if len(name) > 5]
numbers1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers1]
# print(new_number)
# print(new_range)
# print(short_name)
# print(long_name)
#print(squared_numbers)

numbers2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_list = [n for n in numbers2 if n % 2 == 0]
#print(even_list)

with open("./List_comprehension/file1.txt") as file:
    #this will help to create a list of each lines
    content = file.readlines()
    new_content = [n.strip() for n in content]

with open("./List_comprehension/file2.txt") as file2:
    content = file2.readlines()
    new_content2 = [n.strip() for n in content]
    
    
result = [int(n) for n in new_content if n in new_content2]  
print(result) 
