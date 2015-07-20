class Book:

    def __init__(self, title, author, remain_book):
        self.title = title
        self.author = author
        self.remain_book = remain_book

    def rent(self):
        if self.remain_book > 0:
            self.remain_book -= 1
            return self
        else:
            raise BookError('남은 책이 없습니다.')


class Ebook(Book):
    def rent(self):
        return

class Paper(Book):
    pass


class BookError(Exception):
    pass
