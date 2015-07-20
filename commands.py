class Command:

    def __init__(self, lib):
        self.lib = lib

    def start(self):
        while True:
            command = input('명령어')

            if command == '로그인':
                self.login()
            elif command == '도서추가':
                self.add_book()

    def login(self):
        id = input('아이디')

        if self.lib.login(id):
            성공했습니다
        else:
            self.join()

    def join(self):
        pass

    def add_book(self):
        if self.lib.logged_user is None:
            로그인 해주세요
            멈춤
        elif not self.lib.logged_user.is_admin:
            관리자만 가능합니다.
            멈춤
        name = input('책이름')
        author = input('저자')
        book = Book(name, author)
        self.lib.book_list.append(book)


class Libaray:

    def __init__(self):
        self.book_list = BookList(Book('치즈인더트랩', '순끼'))
        self.user_list = UserList()
        self.logged_user = None
        self.command = Command(self)

    def login(self, id):
        user = self.user_list.search_by_id(id)
        self.logged_user = user
        return user



class User:

    def __init__(self, id, is_admin=False):
        self.id = id
        self.is_admin = is_admin
        self.book_list = []


class UserList(list):

    def search_by_id(self, id):
        for user in self:
            if user.id == id:
                return user
        return None


class Book:

    def __init__(self, name, author):
        self.name = name
        self.author = author


class BookList(list):
    pass
