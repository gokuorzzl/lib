from list import BookList, UserList
from book import Book
from command import Command

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
