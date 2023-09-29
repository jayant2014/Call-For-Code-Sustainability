class User:
    def __init__(self, username, initial_credits=0):
        self.username = username
        self.credits = initial_credits

class CarbonTradingPlatform:
    def __init__(self):
        self.users = {}  # Dictionary to store user objects

    def add_user(self, username, initial_credits=0):
        if username not in self.users:
            user = User(username, initial_credits)
            self.users[username] = user
            return f'User {username} added successfully.'
        else:
            return f'User {username} already exists.'

    def transfer_credits(self, sender, receiver, credits):
        if sender in self.users and receiver in self.users:
            sender_user = self.users[sender]
            receiver_user = self.users[receiver]

            if sender_user.credits >= credits:
                sender_user.credits -= credits
                receiver_user.credits += credits
                return f'{credits} credits transferred from {sender} to {receiver}.'
            else:
                return f'Insufficient credits for transfer.'
        else:
            return f'User not found.'

    def get_user_credits(self, username):
        if username in self.users:
            return self.users[username].credits
        else:
            return f'User not found.'

# Example usage:
platform = CarbonTradingPlatform()

print(platform.add_user('UserA', initial_credits=100))
print(platform.add_user('UserB', initial_credits=50))

print(platform.transfer_credits('UserA', 'UserB', credits=30))
print(platform.transfer_credits('UserA', 'UserB', credits=80))

print(f'UserA credits: {platform.get_user_credits("UserA")}')
print(f'UserB credits: {platform.get_user_credits("UserB")}')
