from user import user
from PC import PC

class store():
    users = {}

    MB = {}
    RAM = {}
    Micro = {}
    HD = {}

    bought_PCs = []

    def __init__(self, dics= 0):  #dics = [dic1, dic2, dic3, list?...]
        if not dics == 0:
            for e in dics:
                self.e = e
        return

    def add(self, user, password, dic, obj, dics = []):
        if dics == []:
           dics=[self.MB,self.RAM,self.Micro,self.HD,self.bought_PCs,self.users]

        if not user.check(user.username,password):
            print "Wrong username or password"
            return
        if not user.is_admin():
            print "User is not an admin"
            return

        if dic not in dics:
            print "Diccionary not found"
            return
        if obj in dic:
            print "Object already added"
            return

        if not dic == self.bought_PCs:
            dic[obj] = obj.serial
            print "Sucessfuly added to diccionary"
            return
        else:
            if not isinstance(obj, PC):
                print "Object not accepted"
                return
            else:
                self.bought_PCs.append(obj)
                print "Sucessfuly added to diccionary"
                return
        print "Critical Error, seek help"
        return

    def delete(self, user, password, dic, obj, dics = []):
        if dics == []:
           dics=[self.MB,self.RAM,self.Micro,self.HD,self.bought_PCs,self.users]

        if not user.check(user.username,password):
            print "Wrong username or password"
            return
        if not user.is_admin():
            print "User is not an admin"
            return

        if dic not in dics:
            print "Diccionary not found"
            return
        if obj not in dic:
            print "Object not found"
            return

        del dic[obj]
        print "Sucessfuly deleted object from diccionary"
        return

    def mod(self, user, password, dic, del_obj, add_obj, dics = []):
        print "Modifying..."
        self.add(user, password, dic, add_obj, dics)
        self.delete(user, password, dic, del_obj, dics)
        return
