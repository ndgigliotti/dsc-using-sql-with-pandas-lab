import pandas as pd

def fetch2frame(cursor):
    """Fetch all items from `cursor` and return a DataFrame."""
    columns = [x[0] for x in cursor.description]
    return pd.DataFrame(cursor.fetchall(), columns=columns)

def fetch_tables(cursor):
    cursor.execute("""SELECT name as table_name
                      FROM sqlite_master 
                      WHERE type ='table'
                      AND name NOT LIKE 'sqlite_%';""")
    return fetch2frame(cursor)
