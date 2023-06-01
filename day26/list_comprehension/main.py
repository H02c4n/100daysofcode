numbers = [1,3,4,56,7]
new_list =[n+1 for n in numbers]
print(new_list)

name = "Halil"

letters = [l for l in name]

print(letters)

range_list = [num*2 for num in range(1,5)]

print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

short_names = [name for name in names if len(name) < 5]

print(short_names)

name_has_a_letter = [name for name in names if name.__contains__("a")]
print(name_has_a_letter)

UpperCaseAndLongName = [name.upper() for name in names if len(name) > 5]

print(UpperCaseAndLongName)


numbers = [1,1,2,3,5,8,13,21,34,55]

squared_numbers = [num**2 for num in numbers]

print(squared_numbers)

even_numbers = [n for n in numbers if n % 2 == 0]

print(even_numbers)


#######################Data Overlap#####################################

with open("file1.txt") as file1:
    nums1 = file1.readlines()

with open("file2.txt") as file2:
    nums2 = file2.readlines()

result = [int(num) for num in nums1 if num in nums2]

print(result)
