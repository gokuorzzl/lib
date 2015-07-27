from book import Book

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

    def add_book(self):     #  FIXME 도서추가시 로그인 함더 해야된다뜸
        if self.lib.logged_user is None:
            print('로그인 하세요')
            return
        if not self.lib.logged_user.is_admin:
            # self 도서관의 로그인유저는, 어드민이냐.아니냐. 묻는걸로 파악!

            print('관리자만 가능합니다.')
            return

        name = input('책이름')
        author = input('저자')
        remain = input('책 갯수')
        self.lib.add_book(name, author, remain)

    def search_book(self):
        type = input('제목/저자명')

        search_result = []  # 검색결과를 []배열로 넣자!
        if type == '제목':
            name = input('책 제목')
            search_result = self.lib.book_list.search_by_name(name)
        elif type == '저자명':
            author = input('저자명')
            search_result = self.lib.book_list.search_by_author(author)

        if search_result:
            for id, book, remain in search_result:
                print('[No.{}] {}님의 {}이 {}권 남았습니다'.format(
                    id, book.author, book.name, remain
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

        self.lib.logged_user.book_list.append([rented_book, 1])
        print('책을 빌렸습니다.')

    def my_book(self):
        if self.lib.logged_user is None:
            print('로그인 해주세요.')
            return

        if not self.lib.logged_user.book_list:
            print('빌린 책이 없습니다.')
            return

        for i, book_info in enumerate(self.lib.logged_user.book_list):
            book, remain = book_info
            print('[No.{}] {}가 지은 {}'.format(i, book.author, book.name))
