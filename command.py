from book import Book

class Command:

    def __init__(self, lib):
        self.lib = lib
        #  커멘드에 lib를 넣는 것.

    def start(self):
        while True:
            command = input('명령어를 입력해 주세요.')
            print('로그인, 도서추가')

            if command == '로그인':
                self.login()
                #  로그인 실행의 주체 = self !
            elif command == '도서추가':
                self.add_book()
            elif command == '도서검색':
                self.search_book()
            elif command == '가입':
                self.join()

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
            #  self 도서관의 로그인유저는, 어드민이냐.아니냐. 묻는걸로 파악!

            print('관리자만 가능합니다.')
            return

        name = input('책이름')
        author = input('저자')
        remain = input('책 갯수')
        self.lib.add_book(name, author, remain)

    def search_book(self):
        type = input('제목/저자명')

        search_result = []
        if type == '제목':
            name = input('책 제목')
            search_result = self.lib.book_list.search_by_name(name)
        elif type == '저자명':
            pass #  FIXME

        if search_result:
            for book, remain in search_result:
                print('{}님의 {}이 {}권 남았습니다'.format(book.author, book.name, remain))
        else:
            print('찾으시는 책이 없습니다.')
