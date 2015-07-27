from list import BookList, UserList
from book import Book
from command import Command
from user import User

class Library:

    def __init__(self):
        self.book_list = BookList()
        self.user_list = UserList()
        self.logged_user = None
        self.command = Command(self)

    def login(self, id):
        user = self.user_list.search_by_id(id)
        self.logged_user = user
        return user

    def join(self, id, is_admin=False):
        user = User(id, is_admin)
        self.user_list.append(user)

    def add_book(self, name, author, remain):
        book = Book(name, author)
        self.book_list.append([book, remain])

    def is_rentable(self, id):
        try:
            return self.book_list[id][1] > 0
        except IndexError:
            return False

    def rent(self, id):
        book_info = self.book_list[id]
        book_info[1] -= 1
        return book_info[0]

if __name__ == '__main__':
    lib = Library()
    lib.join('admin', True)
    lib.add_book('치즈인더트랩', '순끼', 5)
    lib.add_book('신의 탑', 'SIU', 10)
    lib.add_book('고고고', '하일권', 1)
    lib.command.start()
