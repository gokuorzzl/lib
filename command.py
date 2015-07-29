from book import Book, Ebook

class Command:

    def __init__(self, lib):
        self.lib = lib
        self.command_list = {
            '로그인': self.login,
            '도서추가': self.add_book,
            '도서검색': self.search_book,
            '가입': self.join,
            '도움말': self.help,
            '도서대출': self.rent,
            '내가빌린책': self.my_book,
            '도서반납': self.return_book,
        }
        #  커멘드에 lib를 넣는 것.

    def start(self):
        while True:
            command = input('명령어를 입력해 주세요.(도움말)')

            command_function = self.command_list.get(command, self.help)

            command_function()

    def help(self):
        print('사용가능한 명령어: {}'.format(
            ', '.join(self.command_list.keys())
        ))

    def login(self):
        id = input('아이디')

        if self.lib.login(id):
            # 위에 구문 이해가..
            print('로그인 성공')
        else:
            self.join()

    def join(self):
        id = input('사용하고 싶은 아이디')
        user = self.lib.user_list.search_by_id(id)
        if user:
            print('중복된 아이디 입니다.')
            return

        self.lib.join(id)

        print('가입되었습니다. 로그인 해보세요.')

    def add_book(self):
        if self.lib.logged_user is None:
            print('로그인 하세요')
            return
        if not self.lib.logged_user.is_admin:
            # self 도서관의 로그인유저는, 어드민이냐.아니냐. 묻는걸로 파악!

            print('관리자만 가능합니다.')
            return

        type = input('도서/전자도서/논문')

        name = input('타이틀')
        author = input('저자')
        if type == '도서':
            remain = input('책 갯수')
            self.lib.add_book(name, author, remain)
        elif type == '전자도서':
            self.lib.add_ebook(name, author)
        else:
            self.lib.add_paper(name, author)

    def search_book(self):
        search_type = input('제목/저자명')

        search_result = []  # 검색결과를 []배열로 넣자!
        if search_type == '제목':
            name = input('책 제목')
            search_result = self.lib.book_list.search_by_name(name)
        elif search_type == '저자명':
            author = input('저자명')
            search_result = self.lib.book_list.search_by_author(author)

        if search_result:
            for id, book, remain in search_result:
                if type(book) == Book:
                    book_type = '도서'
                elif type(book) == Ebook:
                    book_type = '전자도서'
                else:
                    book_type = '논문'

                print('[No.{}] {}님의 {} {}이 {}권 남았습니다'.format(
                    id, book.author, book_type, book.name, remain
                ))
        else:
            print('찾으시는 책이 없습니다.')

    def rent(self):
        if self.lib.logged_user is None:
            print('로그인이 필요합니다.')
            return

        id = input('책 고유번호')
        try:
            id = int(id)
        except ValueError:
            print('유효하지 않은 번호')
            return

        if not self.lib.is_rentable(id):
            print('빌릴 수 없음')
            return

        rented_book = self.lib.rent(id)

        self.lib.logged_user.book_list.add(id, rented_book)
        print('책을 빌렸습니다.')

    def my_book(self):
        if self.lib.logged_user is None:
            print('로그인 해주세요.')
            return

        if not self.lib.logged_user.book_list:
            print('빌린 책이 없습니다.')
            return

        for id, book in self.lib.logged_user.book_list.items():
            print('[No.{}] {}가 지은 {}'.format(
                id, book.author, book.name
            ))

    def return_book(self):
        if self.lib.logged_user is None:
            print('로그인 해주세요.')
            return

        if not self.lib.logged_user.book_list:
            print('빌린 책이 없습니다.')
            return

        id = input('책번호')
        try:
            id = int(id)
        except ValueError:
            print('올바르지 않은 고유번호')
            return

        if self.lib.user_have_book(id):
            self.lib.return_book(id)
            print('도서를 반납하였습니다.')
        else:
            print('가지고 있지 않은 책입니다.')
