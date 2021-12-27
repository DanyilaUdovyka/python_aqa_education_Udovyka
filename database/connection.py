import sqlite3


con = sqlite3.connect('test.db')
cur = con.cursor()

def select_all(cur):
    sql_query_select = ''' SELECT * FROM movie_info; '''
    cur.execute(sql_query_select)
    return cur.fetchall()


def select_by_id(id, cur):
    sql_query_select = ''' SELECT * FROM movie_info WHERE id = ?; '''
    cur.execute(sql_query_select, (id,))
    return cur.fetchall()


def create_movie_info_table(cur):
    cur.execute('''CREATE TABLE movie_info
                   (id integer primary key, title text, country text, date_release text, producer text, rate real)''')


def insert_new_info(title, country, date_release, producer, rate, cur):
    cur.execute("INSERT INTO movie_info(title, country, date_release, producer, rate)"
                "VALUES (?,?,?,?,?)", (title, country, date_release, producer, rate))


def update_title_by_id(id, new_title, cur):
    sql_query_update = ''' UPDATE movie_info SET title=? WHERE id=?; '''
    cur.execute(sql_query_update, (new_title, id,))


def delete_by_id(id, cur):
    sql_query_delete = ''' DELETE FROM movie_info WHERE (id=?); '''
    cur.execute(sql_query_delete, (id,))


def drop_movie_info_table(cur):
    cur.execute('''DROP TABLE movie_info''')


drop_movie_info_table(cur)
create_movie_info_table(cur)
insert_new_info('tip', 'UC', '12.12.1999', 'hh', 6.5, cur)
insert_new_info('avengers', 'USA', '2012-02-02', 'someone', 9.9, cur)
insert_new_info('Far', 'UK', '1666-10-12', 'someone', 5.6, cur)

delete_by_id(1, cur)
print(select_all(cur))
update_title_by_id(2, "LOL", cur)
print(select_by_id(2, cur))

con.close()
