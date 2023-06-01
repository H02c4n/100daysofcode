

##! new_dict = {new_key:new_value for item in list}  ##

import random


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_score = {name:random.randint(1,100) for name in names}

print(students_score)

passed_students = {name:}