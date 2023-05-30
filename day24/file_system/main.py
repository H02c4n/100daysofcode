
#file = open("new.txt")

# with open("new.txt") as file:
#     content = file.read()
#     print(content)
#     file.close()


with open("new.txt", mode="a") as file:
    file.write("new text")
    file.close()

