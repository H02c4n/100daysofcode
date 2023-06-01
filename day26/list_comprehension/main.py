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