class UserList(list):

    def search_by_id(self, id):
        for user in self:
            if user.id == id:
                return user
        return None


class BookList(list):

    def search_by_name(self, name):
        search_result = []
        for book, remain in self:
            if name in book.name:
                search_result.append([book, remain])

        return search_result
