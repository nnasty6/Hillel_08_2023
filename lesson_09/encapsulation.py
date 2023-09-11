from typing import Any


class User:
    def __init__(self, username: str, password: str):
        self.username: str = username
        self._password: str = password
        self._authorized = False

    def __getattribute__(self, name: str) -> Any:
        if name == "password":
            return "Access Denied!"
        return super().__getattribute__(name)

    def login(self, entered_login: str, entered_password: str) -> None:
        if entered_login == self.username and entered_password == self._password:
            self._authorized = True
        else:
            self._authorized = False

    @property
    def is_authorized(self) -> bool:
        return self._authorized

    @property
    def password(sself):
        return "*******"


john = User(username="john", password="12345")


def login(username: str, password: str):
    john.login(username, password)
    print(john.password)
    if john.is_authorized:
        print("Success")
    else:
        print("Not success")


login("john", "12345")
