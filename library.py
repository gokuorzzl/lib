from list import BookList, UserList
from book import Book, Ebook, Paper
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

    def add_ebook(self, name, author):
        ebook = Ebook(name, author)
        self.book_list.append([ebook, None])

    def add_paper(self, name, author):
        paper = Paper(name, author)
        self.book_list.append([paper, None])

    def is_rentable(self, id):
        if type(self.book_list[id][1]) == Book:
            try:
                return self.book_list[id][1] > 0
            except IndexError:
                return False
        else:
            return True

    def rent(self, id):
        book_info = self.book_list[id]
        if type(self.book_list[id][1]) == Book:
            book_info[1] -= 1
        return book_info[0]

    def return_book(self, id):
        book = self.logged_user.book_list[id]
        del self.logged_user.book_list[id]
        if type(self.book_list[id][1]) == Book:
            self.book_list[id][1] += 1

    def user_have_book(self, id):
        return id in self.logged_user.book_list

if __name__ == '__main__':
    lib = Library()
    lib.join('admin', True)
    lib.add_book('치즈인더트랩', '순끼', 5)
    lib.add_book('신의 탑', 'SIU', 10)
    lib.add_book('고고고', '하일권', 1)
    lib.add_ebook('강아지와 고양이는 왜 싸우는가', '고영욱')
    lib.add_paper('아청법의 이해', '경찰청')
    lib.command.start()
