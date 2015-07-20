class BookList(list):

    def search_by_title(self, title):
        result = []
        for book in self:
            # for문 self title을 찾는 객체를 말함.
            # 여기서는 책의 이름을 찾는것이니. 책이라고 편하게 쓴것이다.
            if title in book.title:
                result.append(book)
                #  append= 추가한다. result 결과값 (찾기한목록에 추가해줌)
        return result

    def lent_list(self, title):
        result = []
        for book in self:
            if title in book.title:
                result.append(book)
                return result

class UserList(list):
    def join(self, id):
        user_id = []
        if id not in user_id:
            user_id.append(id)
        return print('가입되었습니다.')






