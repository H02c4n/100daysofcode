class User:
    def __init__(self, user_id, username):
        print("new user being created")        
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","Halil")

# user_1.id = "001"
# user_1.username = "Halil"

print(user_1.username)


user_2 = User("002","Cemal")

# user_2.id = "002"
# user_2.username = "Cemal"

user_3 = User("003", "Faik")

print(user_3.username)
print(user_3.followers)

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)