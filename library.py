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

    def add_book(self, name, author):
        book = Book(name, author)
        self.book_list.append(book)

if __name__ == '__main__':
    lib = Library()
    lib.join('admin', True)
    lib.command.start()
