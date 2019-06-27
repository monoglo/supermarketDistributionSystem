import pymysql
import time


class SupermarketDB(object):
    def __init__(self, ip, username, passwd, database):
        self.get_conn(ip, username, passwd, database)
        self.today = time.strftime("%Y-%m-%d")

    def get_conn(self, ip, username, passwd, database):
        try:
            self.conn = pymysql.connect(ip, username, passwd, database)
        except pymysql.Error as e:
            print('SQLError:%s' % e)

    def close_conn(self):
        try:
            if self.conn:
                self.conn.close()
        except pymysql.Error as e:
            print('SQLError:%s' % e)

    def do_sql(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            rest = cursor.fetchone()
            cursor.close()
            return rest
        except pymysql.Error as e:
            print('SQLError:%s' % e)
            raise e

    def do_sql_one(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            fet = cursor.fetchone()
            if fet is not None:
                rest = dict(zip([k[0] for k in cursor.description], fet))
                cursor.close()
                return rest
            else:
                cursor.close()
                return []
        except pymysql.Error as e:
            print('SQLError:%s' % e)
            raise e

    def do_sql_multi(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
            self.conn.commit()
            rest = [
                dict(zip([k[0] for k in cursor.description], row))
                for row in cursor.fetchall()
            ]
            cursor.close()
            return rest
        except pymysql.Error as e:
            print('SQLError:%s' % e)
            raise e

    def add_administrator(self, name, screenName, email, phone, adress,
                          password):
        # 添加一条管理员
        sql = '''
                INSERT INTO `administrators`
                (`name`,`screenName`,`email`,`phone`,`adress`,`password`)
                VALUE ('%s', '%s', '%s', '%s', '%s', '%s')
            ''' % (name, screenName, email, phone, adress, password)
        return self.do_sql(sql)

    def delete_administrator(self, aid):
        sql = '''
            UPDATE `administrators`
            SET `status` = 'deleted'
            WHERE `aid` = '%s'
            ''' % (aid)
        return self.do_sql(sql)

    def update_administrator(self, aid, name, screenName, email, phone, adress,
                             password):
        sql = '''
            UPDATE `administrators`
            SET `name` = '%s',
            `screenName` = '%s',
            `email` = '%s',
            `phone` = '%s',
            `adress` = '%s',
            `password` = '%s'
            WHERE `aid` = '%s'
            ''' % (name, screenName, email, phone, adress, password, aid)
        return self.do_sql(sql)

    def select_administrator_singal(self, method, value):
        sql = '''
            SELECT *
            FROM `administrators`
            WHERE `%s` = '%s'
            AND `status` = 'normal'
            ''' % (method, value)
        return self.do_sql_one(sql)

    def select_administrator_multi(self, method, value):
        sql = '''
            SELECT *
            FROM `administrators`
            WHERE `%s` = '%s'
            AND `status` != 'deleted'
            ORDER BY `aid`
            DESC
            ''' % (method, value)
        return self.do_sql_multi(sql)

    def add_customer(self, name, screenName, email, phone, adress, password):
        # 添加一位客户
        sql = '''
                INSERT INTO `customers`
                (`name`,`screenName`,`email`,`phone`,`adress`,`password`)
                VALUE ('%s', '%s', '%s', '%s', '%s', '%s')
            ''' % (name, screenName, email, phone, adress, password)
        self.do_sql(sql)

    def delete_customer(self, cuid):
        sql = '''
            UPDATE `customers`
            SET `status` = 'deleted'
            WHERE `cuid` = '%s'
            ''' % (cuid)
        return self.do_sql(sql)

    def update_customer(self, cuid, name, screenName, email, phone, adress,
                        password):
        sql = '''
            UPDATE `customers`
            SET `name` = '%s',
            `screenName` = '%s',
            `email` = '%s',
            `phone` = '%s',
            `adress` = '%s',
            `password` = '%s'
            WHERE `cuid` = '%s'
            ''' % (name, screenName, email, phone, adress, password, cuid)
        return self.do_sql(sql)

    def select_customer_singal(self, method, value):
        sql = '''
            SELECT *
            FROM `customers`
            WHERE `%s` = '%s'
            AND `status` = 'normal'
            ''' % (method, value)
        return self.do_sql_one(sql)

    def select_customer_multi(self, method, value):
        sql = '''
            SELECT *
            FROM `customers`
            WHERE `%s` = '%s'
            AND `status` != 'deleted'
            ORDER BY `cuid`
            DESC
            ''' % (method, value)
        return self.do_sql_multi(sql)

    def add_courier(self, name, screenName, email, phone, adress, password):
        # 添加一条配送员
        sql = '''
                INSERT INTO `couriers`
                (`name`,`screenName`,`email`,`phone`,`adress`,`password`)
                VALUE ('%s', '%s', '%s', '%s', '%s', '%s')
            ''' % (name, screenName, email, phone, adress, password)
        return self.do_sql(sql)

    def delete_courier(self, coid):
        sql = '''
            UPDATE `couriers`
            SET `status` = 'deleted'
            WHERE `coid` = '%s'
            ''' % (coid)
        return self.do_sql(sql)

    def update_courier(self, coid, name, screenName, email, phone, adress,
                       password):
        sql = '''
            UPDATE `couriers`
            SET `name` = '%s',
            `screenName` = '%s',
            `email` = '%s',
            `phone` = '%s',
            `adress` = '%s',
            `password` = '%s'
            WHERE `coid` = '%s'
            ''' % (name, screenName, email, phone, adress, password, coid)
        return self.do_sql(sql)

    def select_courier_singal(self, method, value):
        sql = '''
            SELECT *
            FROM `couriers`
            WHERE `%s` = '%s'
            AND `status` = 'normal'
            ''' % (method, value)
        return self.do_sql_one(sql)

    def select_courier_multi(self, method, value):
        sql = '''
            SELECT *
            FROM `couriers`
            WHERE `%s` = '%s'
            AND `status` != 'deleted'
            ORDER BY `coid`
            DESC
            ''' % (method, value)
        return self.do_sql_multi(sql)

    def add_good(self, productNumber, name, type, expireDate, unit, quantity,
                 price, cost):
        # 添加一条管理员
        sql = '''
                INSERT INTO `goods`
                (`productNumber`,`name`,`type`,`expireDate`,`unit`,`quantity`,`price`,`cost`)
                VALUE ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
            ''' % (productNumber, name, type, expireDate, unit, quantity,
                   price, cost)
        return self.do_sql(sql)

    def delete_good(self, gid):
        sql = '''
            UPDATE `goods`
            SET `quantity` = '0'
            WHERE `gid` = '%s'
            ''' % (gid)
        return self.do_sql(sql)

    def update_good(self, gid, productNumber, name, type, expireDate, unit,
                    quantity, price, cost):
        sql = '''
                UPDATE `goods`
                SET `productNumber` = '%s',
                `name` = '%s',
                `type` = '%s',
                `expireDate` = '%s',
                `unit` = '%s',
                `quantity` = '%s',
                `price` = '%s',
                `cost` = '%s'
                WHERE `gid` = '%s'
                ''' % (productNumber, name, type, expireDate, unit, quantity,
                       price, cost, gid)
        return self.do_sql(sql)

    def select_good_singal(self, method, value):
        sql = '''
            SELECT *
            FROM `goods`
            WHERE `%s` = '%s'
            AND `quantity` >= '0'
            ''' % (method, value)
        return self.do_sql_one(sql)

    def select_good_multi(self, method, value):
        sql = '''
            SELECT *
            FROM `goods`
            WHERE `%s` = '%s'
            AND `quantity` > '0'
            ORDER BY `gid`
            DESC
            ''' % (method, value)
        return self.do_sql_multi(sql)

    def select_outdate_good_multi(self, method, value):
        sql = '''
            SELECT *
            FROM `goods`
            WHERE `%s` = '%s'
            AND `expireDate` <= '%s'
            AND `quantity` > '0'
            ORDER BY `gid`
            DESC
            ''' % (method, value, self.today)
        return self.do_sql_multi(sql)

    def add_order(self, cuid):
        sql = '''
                INSERT INTO `orders`
                (`cuid`)
                VALUE ('%s')
            ''' % (cuid)
        self.do_sql(sql)
        sql2 = 'SELECT LAST_INSERT_ID()'
        oid = self.do_sql_one(sql2)['LAST_INSERT_ID()']
        return self.select_order_singal('oid', oid)

    def add_order_item(self, oid, gid, productNumber, unit, quantity, price,
                       amount):
        sql = '''
                INSERT INTO `orderitems`
                (`oid`,`gid`,`productNumber`,`unit`,`quantity`,`price`,`amount`)
                VALUE ('%s', '%s', '%s', '%s', '%s', '%s', '%s')
            ''' % (oid, gid, productNumber, unit, quantity, price, amount)
        return self.do_sql(sql)

    def select_order_singal(self, method, value):
        sql = '''
            SELECT *
            FROM `orders`
            WHERE `%s` = '%s'
            AND `status` != 'deleted'
            ''' % (method, value)
        return self.do_sql_one(sql)

    def select_order_multi(self, method, value):
        sql = '''
            SELECT *
            FROM `orders`
            WHERE `%s` = '%s'
            AND `status` != 'deleted'
            ORDER BY `oid`
            DESC
            ''' % (method, value)
        return self.do_sql_multi(sql)

    def delete_order(self, oid):
        sql = '''
            UPDATE `orders`
            SET `status` = 'deleted'
            WHERE `oid` = '%s'
            ''' % (oid)
        return self.do_sql(sql)

########################################################

    def add_comment(self, reader_id, news_id, content, status):
        # 举个栗子， 添加一条评论
        sql = '''
                INSERT INTO `comments`
                (`reader_id`,`id`,`content`,`status`)
                VALUE ('%s', '%s', '%s', '%s')
            ''' % (reader_id, news_id, content, status)
        self.do_sql(sql)

    def add_author(self, author_name, author_type, status, passwd, email):
        # 添加一名作者
        sql = '''
                INSERT INTO `author`
                (`author_name`,`author_type`,`status`,`passwd`,`email`)
                VALUE('%s', '%s', '%s', '%s', '%s')
            ''' % (author_name, author_type, status, passwd, email)
        self.do_sql(sql)

    def add_reader(self, name, sex, status, passwd, email):
        # 添加一名读者
        sql = '''
                INSERT INTO `reader`
                (`name`,`sex`,`status`,`passwd`,`email`)
                VALUE('%s', '%s', '%s', '%s', '%s')
            ''' % (name, sex, status, passwd, email)
        self.do_sql(sql)

    def select_all_news(self):
        sql = '''
            SELECT *
            FROM `news`
            WHERE `status` = 1
            ORDER BY `id`
            DESC
            '''
        return self.do_sql_multi(sql)

    def select_one_news(self):
        sql = '''
            SELECT *
            FROM `news`
            ORDER BY `id`
            DESC
            '''
        return self.do_sql_one(sql)

    def select_all_news_author(self, author_id):
        sql = '''
            SELECT *
            FROM `news`
            WHERE `author_id` = '%s'
            AND `status` = 1
            ORDER BY `id`
            DESC
            ''' % (author_id)
        return self.do_sql_multi(sql)

    def select_news_id(self, news_id):
        sql = '''
            SELECT *
            FROM `news`
            WHERE `id` = '%s'
            AND `status` = 1
            ORDER BY `id`
            DESC
            ''' % (news_id)
        return self.do_sql_multi(sql)

    def select_all_user(self):
        sql = '''
            SELECT *
            FROM `reader`
            WHERE `status` = 1
            ORDER BY `reader_id`
            DESC
            '''
        return self.do_sql_multi(sql)

    def select_all_comment(self):
        sql = '''
            SELECT *
            FROM `comments`
            WHERE `status` = 1
            ORDER BY `comment_id`
            DESC
            '''
        return self.do_sql_multi(sql)

    def select_all_author(self):
        sql = '''
            SELECT *
            FROM `author`
            WHERE `status` = 1
            ORDER BY `author_id`
            DESC
            '''
        return self.do_sql_multi(sql)

    def select_user_name(self, name):
        sql = '''
            SELECT *
            FROM `reader`
            WHERE `status` = 1
            AND `name` = '%s'
            ORDER BY `reader_id`
            DESC
            ''' % name
        return self.do_sql_multi(sql)

    def select_user_id(self, id):
        sql = '''
            SELECT *
            FROM `reader`
            WHERE `status` = 1
            AND `reader_id` = '%s'
            ORDER BY `reader_id`
            DESC
            ''' % id
        return self.do_sql_one(sql)

    def select_comment_news(self, news_id):
        sql = '''
            SELECT *
            FROM `comments`
            WHERE `status` = 1
            AND `id` = '%s'
            ORDER BY `comment_id`
            DESC
            ''' % news_id
        return self.do_sql_multi(sql)

    def select_comment_user(self, user_id):
        sql = '''
            SELECT *
            FROM `comments`
            WHERE `status` = 1
            AND `id` = '%s'
            ORDER BY `comment_id`
            DESC
            ''' % user_id
        return self.do_sql_multi(sql)

    def select_author_id(self, author_id):
        sql = '''
            SELECT *
            FROM `author`
            WHERE `status` = 1
            AND `author_id` = '%s'
            ORDER BY `author_id`
            DESC
            ''' % author_id
        return self.do_sql_multi(sql)

    def select_author_name(self, name):
        sql = '''
            SELECT *
            FROM `author`
            WHERE `status` = 1
            AND `author_name` = '%s'
            ORDER BY `author_id`
            DESC
            ''' % name
        return self.do_sql_multi(sql)

    def author_name(self, author_id):
        sql = '''
            SELECT author_name
            FROM `author`
            WHERE `author_id` = '%s'
            AND `status` = 1
            ''' % (author_id)
        return self.do_sql(sql)

    def author_id(self, author_name):
        sql = '''
            SELECT author_id
            FROM `author`
            WHERE `author_name` = '%s'
            AND `status` = 1
            ''' % (author_name)
        rest = self.do_sql_one(sql)
        return rest['author_id']

    def update_news_view(self, id):
        sql = '''
            UPDATE `news`
            SET `view_count` = `view_count+1`
            WHERE `id` = '%s'
            AND `status` = 1
            ''' % (id)
        rest = self.do_sql(sql)
        return rest

    def update_user(self, id, name, sex, passwd, email):
        sql = '''
            UPDATE `reader`
            SET `name` = '%s',
            `sex` = '%s',
            `passwd` = '%s',
            `email` = '%s'
            WHERE `reader_id` = '%s'
            AND `status` = 1
            ''' % (name, sex, passwd, email, id)
        rest = self.do_sql(sql)
        return rest

    def update_author(self, id, name, type, passwd, email):
        sql = '''
            UPDATE `author`
            SET `author_name` = '%s',
            `author_type` = '%s',
            `passwd` = '%s',
            `email` = '%s'
            WHERE `author_id` = '%s'
            AND `status` = 1
            ''' % (name, type, passwd, email, id)
        rest = self.do_sql(sql)
        return rest

    def update_comment(self, commentid, readerid, newsid, content):
        sql = '''
            UPDATE `comments`
            SET `reader_id` = '%s',
            `id` = '%s',
            `content` = '%s'
            WHERE `comment_id` = '%s'
            AND `status` = 1
            ''' % (readerid, newsid, content, commentid)
        rest = self.do_sql(sql)
        return rest

    def delete_user(self, id):
        sql = '''
            UPDATE `reader`
            SET `status` = 0
            WHERE `reader_id` = '%s'
            AND `status` = 1
            ''' % (id)
        rest = self.do_sql(sql)
        return rest

    def delete_comment(self, id):
        sql = '''
            UPDATE `comments`
            SET `status` = 0
            WHERE `comment_id` = '%s'
            AND `status` = 1
            ''' % (id)
        rest = self.do_sql(sql)
        return rest

    def delete_author(self, id):
        sql = '''
            UPDATE `author`
            SET `status` = 0
            WHERE `author_id` = '%s'
            AND `status` = 1
            ''' % (id)
        rest = self.do_sql(sql)
        return rest

    def select_fans(self, author_id):
        sql = '''
            SELECT `reader_id`
            FROM `subscription`
            WHERE `author_id` = '%s'
            ''' % author_id
        rest = self.do_sql_multi(sql)
        return rest

    def select_subs(self, reader_id):
        sql = '''
            SELECT `author_id`
            FROM `subscription`
            WHERE `reader_id` = '%s'
            ''' % reader_id
        rest = self.do_sql_multi(sql)
        return rest
