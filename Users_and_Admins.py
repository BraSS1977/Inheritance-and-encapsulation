# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.
#
# Требования:
#
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа
# ('user' для обычных сотрудников).
#
# 2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка
# (представь, что это просто список экземпляров User).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = "user"

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.access_level = 'admin'

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"Добавлен новый пользователь {user.get_name()}")
        print(user_list)

    def remove_user(self, user_list, user):
        user_list.remove(user)
        print(f"\nПользователь {user.get_name()} удален")
        print(user_list)

user1 = User ("user1", "Павел")
user2 = User ("user2", "Андрей")
user3 = User ("user3", "Сергей")

user_list = [user1, user2, user3]

admin = Admin("admin1", "Никита")

admin.add_user(user_list, user1)
admin.add_user(user_list, user2)
admin.add_user(user_list, user3)

print(f"ID пользователя {user1.get_name()}: {user1.get_user_id()}")


admin.remove_user(user_list, user1)
