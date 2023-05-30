
#file = open("new.txt")

# with open("new.txt") as file:
#     content = file.read()
#     print(content)
#     file.close()


#! mode="a" => append
#! mode="r" => read
#! mode="w" => write

with open("new.txt", mode="a") as file:
    file.write("\nnew text")
    file.close()

