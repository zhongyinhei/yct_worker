import sqlite3
num = 'test'
conn = sqlite3.connect('/code/data_all/source_data-v1.db')
cursor = conn.cursor()
cursor.execute("insert into check0 (num) values ('%s')" %(num))
cursor.close()
conn.commit()
conn.close()
