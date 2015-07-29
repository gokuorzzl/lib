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


class UserBookList:

    def __init__(self):
        self.data = {}

    def add(self, id, book):
        key = str(id)
        self.data[key] = book

    def contains(self, id):
        return str(id) in self.data

    def delete(self, id):
        del self.data[str(id)]

    def __contains__(self, id):
        return self.contains(id)

    def __getitem__(self, id):
        return self.data[str(id)]

    def __delitem__(self, id):
        self.delete(id)

    def items(self):
        return self.data.items()

    def __bool__(self):
        return bool(self.data)
