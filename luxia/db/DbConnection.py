import pymysql


class db_control:

    # init
    def __init__(self, host, user_id, pw, db_name):
        self.conn = pymysql.connect(host, user_id, pw, db_name)

    def is_member(self, user_id):
        # new cursor
        curs = self.conn.cursor()

        # sql query
        sql = "SELECT * FROM user WHERE id=\"%s\""
        curs.execute(sql, (user_id,))

        rows = curs.fetchall()
        curs.close()
        self.conn.commit()

        if rows == ():
            return False

        return True

    def add_user(self, user_id: int, user_name: str):
        curs = self.conn.cursor()
        sql = "INSERT INTO user(id, user_name) values('%s', %s)"
        curs.execute(sql, (user_id, user_name))
        self.conn.commit()
        curs.close()

    def search_link_add(self, author, key, val):
        curs = self.conn.cursor()
        sql = "INSERT INTO link(author, search_key, search_val, search_time) values(%s,%s, %s, 0)"
        curs.execute(sql, (author, key, val))
        self.conn.commit()
        curs.close()

    def search_link_time(self, id):
        curs = self.conn.cursor()
        sql = "UPDATE link SET search_time=search_time + 1 WHERE id = %s"
        curs.execute(sql, (id,))
        self.conn.commit()
        curs.close()

    def search_link_get(self, search_val):
        # new cursor
        curs = self.conn.cursor(pymysql.cursors.DictCursor)

        # sql query
        sql = "SELECT * FROM link WHERE search_key LIKE %s"

        like_val = f'%{search_val}%'

        curs.execute(sql, (like_val,))

        rows = curs.fetchall()
        self.conn.commit()
        curs.close()

        if rows == ():
            return None

        for i in range(len(rows)):
            self.search_link_time(id=rows[i]["Id"])

        return rows

    def user_update(self, name, id):
        curs = self.conn.cursor()
        sql = "UPDATE user SET user_name=%s WHERE id = '%s'"
        curs.execute(sql, (name, id,))
        self.conn.commit()
        curs.close()
