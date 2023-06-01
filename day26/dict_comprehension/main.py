

##! new_dict = {new_key:new_value for item in list}  ##

import random


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_score = {name:random.randint(1,100) for name in names}

print(students_score)

passed_students = {name:score for (name, score) in students_score.items() if score > 50 }

print(passed_students)

##! In the given sentence and calculates the number of letters in each word. ##
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

word_list = sentence.split()
print(word_list)


result = {word:len(word) for word in word_list}

print(result)

##? Or just one line

print({word:len(word) for word in sentence.split()})

#! Convert weather degree from celcius to Farenheight  ##

weather_c ={
    "Monday":12,
    "Tuesday":14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24,
}


weather_f ={day:(degree)*9/5+32 for (day,degree) in weather_c.items()}

print(weather_f)