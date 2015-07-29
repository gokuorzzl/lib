from list import UserBookList


class User:

    def __init__(self, id, is_admin=False):
        self.id = id
        self.is_admin = is_admin
        self.book_list = UserBookList()
