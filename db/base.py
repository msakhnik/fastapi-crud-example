from databases import Database


class BaseDBHelper:
    def __init__(self, database: Database):
        self.database = database
