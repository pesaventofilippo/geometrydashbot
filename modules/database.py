from pony.orm import Database, Required, Optional, IntArray

db = Database("sqlite", "../geometrydashbot.db", create_db=True)


class User(db.Entity):
    chatId = Required(int)
    username = Optional(str)
    password = Optional(str)
    status = Required(str, default="normal")
    savedLevels = Optional(IntArray)


db.generate_mapping(create_tables=True)
