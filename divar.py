class Ad:
    def __init__(self, title, owner):
        self.title = title
        self.owner = owner  # User object


class User:
    def __init__(self, username):
        self.username = username
        self.posted_ads = []    # List of Ad objects
        self.favorites = []     # List of Ad objects


class AdSystem:
    def __init__(self):
        self.users = {}           # username -> User
        self.ads_by_title = {}    # title -> Ad

    def register_user(self, username):
        if username in self.users:
            print("invalid username")
        else:
            self.users[username] = User(username)
            print("registered successfully")

    def add_advertise(self, username, title):
        if username not in self.users:
            print("invalid username")
            return

        if title in self.ads_by_title:
            print("invalid title")
            return

        user = self.users[username]
        ad = Ad(title, user)
        user.posted_ads.append(ad)
        self.ads_by_title[title] = ad
        print("posted successfully")

    def rem_advertise(self, username, title):
        if username not in self.users:
            print("invalid username")
            return

        if title not in self.ads_by_title:
            print("invalid title")
            return

        ad = self.ads_by_title[title]
        if ad.owner.username != username:
            print("access denied")
            return

        user = self.users[username]
        user.posted_ads = [a for a in user.posted_ads if a.title != title]
        del self.ads_by_title[title]
        print("removed successfully")

    def list_my_advertises(self, username):
        if username not in self.users:
            print("invalid username")
            return

        user = self.users[username]
        titles = [ad.title for ad in user.posted_ads]
        print(" ".join(titles))

    def process_command(self, command_str):
        parts = command_str.strip().split(maxsplit=2)

        if not parts:
            print("invalid command")
            return

        command = parts[0]

        if command == "register" and len(parts) == 2:
            self.register_user(parts[1])

        elif command == "add_advertise" and len(parts) == 3:
            username = parts[1]
            title = parts[2]
            self.add_advertise(username, title)

        elif command == "rem_advertise" and len(parts) == 3:
            username = parts[1]
            title = parts[2]
            self.rem_advertise(username, title)

        elif command == "list_my_advertises" and len(parts) == 2:
            self.list_my_advertises(parts[1])

        else:
            print("invalid command")
