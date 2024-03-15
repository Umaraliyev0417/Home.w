class User:
    user_count = 0

    def __init__(self, username):
        self.username = username
        User.user_count += 1


u1 = User("johnsmith10")
print(u1.user_count)
u2 = User("marysue1989")
print(u2.user_count)
u3 = User("milan_rodrick")
print(u3.user_count)
