class UserList(list):

    def search_by_id(self, id):
        for user in self:
            if user.id == id:
                return user
        return None


class BookList(list):
    pass
