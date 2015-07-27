class UserList(list):

    def search_by_id(self, id):
        for user in self:
            if user.id == id:
                return user
        return None


class BookList(list):

    def search_by_name(self, name):
        search_result = []
        for i, book_info in enumerate(self):
            book, remain = book_info
            if name in book.name:
                search_result.append([i, book, remain])

        return search_result

    def search_by_author(self, author):
        search_result = []
        for i, book_info in self:
            book, remain = book_info
            if author in book.author:
                search_result.append([i, book, remain])

        return search_result
