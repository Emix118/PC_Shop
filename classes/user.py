

class user():

    def __init__(self, username, password, confirm_password, admin = False):

        if username in store.users:
            print "Username Taken"
            return
        if password != confirm_password:
            print "Passwords don't match"
            return
        if password == "" or username == "" or confirm_password == "":
            print "Missing Data"
            return

        if admin == True:
            self.status = True
        else:
            self.status = False

        self.username = username
        self.password = password

        store.users[username] = [password, self.status]

        print "Welcome " + self.username
        return

    def change_password(self, old_pass, new_pass, confirm_new):

        if self.username not in store.users:
            print "User not found"
            return
        if old_pass != self.password:
            print "Wrong password"
            return

        if new_pass != confirm_new:
            print "Passwords don't match"
            return

        status = self.status
        self.password = new_pass
        store.users[self.username] = [new_pass, status]

        print "Password changed"
        return


    def is_admin(self):
        return self.status

    def check(self, username, password):

        if username not in store.users:
            print "User not found"
            return False

        if password != store.users[username][0]:
            print "Wrong password"
            return False

        return True

    def info(self):
        print "Username: " + self.username
        print "Password: " + self.password
        print "Admin Status: " + str(self.status)
        return

from store import store
