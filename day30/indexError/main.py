fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as err_message:
        if index > len(fruits) - 1:
            print("Fruit pie")
            print(f"Index should not be over {len(fruits)-1}")
    else:
        print(fruit + " pie")
        



make_pie(3)