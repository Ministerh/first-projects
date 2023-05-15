class User:
    def __init__(self, user_id, username) -> None:
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
#this is a method declaration in a class to modify function
    def follower(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'uchechukwu')
user_2 = User('002', 'faruk')

user_1.follower(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.followers)