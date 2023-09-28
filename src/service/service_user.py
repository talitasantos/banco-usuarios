from src.models import user
from src.models.store import Store
from src.models.user import User


class ServiceUser:

    def __init__(self):
        self.store = Store()

    def verify_user(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user, self.store.bd.index(user)
        return None, None

    def add_user(self, name, job):
        if name != None and job != None:
            if isinstance(name, str) and isinstance(job, str):
                existsUser, index = self.verify_user(name)
                if existsUser == None:
                    user = User(name=name, job=job)
                    self.store.bd.append(user)
                    return "Usuário adicionado"
                else:
                    return "Usuário já existe!"
            else:
                return "Usuário inválido"
        else:
            return "Usuário inválido"

    def remove_user(self, name, job):
        if name != None and job != None:
            if isinstance(name, str) and isinstance(job, str):
                user, index = self.verify_user(name)
                if user != None:
                    self.store.bd.remove(user)
                    return "Usuário removido!"
                else:
                    return "Usuário não existe!"
            else:
                "Usuário inválido"
        else:
            return "Usuário inválido"

    def update_user_name(self, name, job, new_name):
        if name != None and job != None:
            if isinstance(name, str) and isinstance(job, str):
                existsUser, index = self.verify_user(name)
                if existsUser != None:
                    existsUser.name = new_name
                    existsUser.job = job
                    self.store.bd[index] = existsUser
                    return "Usuário atualizado: " + existsUser.name
                else:
                    return "Usuário já existe!"
            else:
                return "Usuário inválido"
        else:
            return "Usuário inválido"

    def get_user_by_name(self, name, job):
        if name != None and job != None:
            if isinstance(name, str) and isinstance(job, str):
                existsUser, index = self.verify_user(name)
                return existsUser.name
            else:
                return "Usuário inválido"
        else:
            return "Usuário inválido"

    def list_user(self):
        for user in self.store.bd:
            print(user.name, user.job)
