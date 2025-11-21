

CREATE_LIST = """
CREATE TABLE IF NOT EXISTS shopping_list (
id INTEGER PRIMARY KEY AUTOINCREMENT,
item TEXT NOT NULL,
completed BOOLEAN NOT NULL DEFAULT 0)"""

ADD_ITEM = "INSERT INTO shopping_list (item) VALUES (?)"

GET_ITEMS = "SELECT id, item, completed FROM shopping_list"

UPDATE_ITEM = "UPDATE shopping_list SET completed = ? WHERE id = ?"

DELETE_ITEM = "DELETE FROM shopping_list WHERE id = ?"
