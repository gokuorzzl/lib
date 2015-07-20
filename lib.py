from list import BookList
from book import BookError
from list import UserList

class Lib:
    book_list = BookList()

    def command(self):
        while True:
            command = input('명령어')

            if command == '대출':
                book_title = input('책 이름')
                try:
                    book = self.book_list[book_title]
                except IndexError:
                    print('그런책 없음')
                    continue
                try:
                    rent_book = book.rent()
                except BookError as err:
                    print(str(err))
                    continue
                User.book_list.append(rent_book)


class User:
    userlist = UserList()

    def cammand(self):
        while True:
            command = input('명령어')

            if command == '가입':
                join_id = input('가입 id를 입력하시오')
                if join_id not in UserList:
                    print('가입이 완료 되었습니다.')
