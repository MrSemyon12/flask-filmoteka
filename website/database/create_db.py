import sqlite3
import pandas as pd

con = sqlite3.connect('website/filmoteka.db')

# f_damp = open('website/database/script.db', 'r', encoding='utf-8-sig')
# damp = f_damp.read()
# f_damp.close()

# con.executescript(damp)
# con.commit()

# cursor = con.cursor()
# df = pd.read_sql('''
#     SELECT sql
#     FROM sqlite_schema
#     WHERE name = 'director';
# ''', con)

df = pd.read_sql('''
    SELECT *
    FROM
        actor       
''', con)

print(df)

con.close()
