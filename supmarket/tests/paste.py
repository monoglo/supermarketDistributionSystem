import module.User
import module.SupermarketDB


class System:
    def create_account_courier(self, name, screenName, email, phone,
                                     adress, password):
        self.mysql.add_courier(name, screenName, email, phone, adress,
                                     password)

    def delete_account_courier(self, aid):
        self.mysql.delete_courier(aid)

    def update_account_courier(self, aid, name, screenName, email, phone,
                                     adress, password):
        self.mysql.update_courier(aid, name, screenName, email, phone,
                                        adress, password)

    def search_account_courier(self, method, value, is_singal):
        if is_singal == 1:
            cou = self.mysql.select_courier_singal(method, value)
            if cou == []:
                raise Exception('Error:No such ' + method + '!')
            self.courier = module.User.courier(
                cou['aid'], cou['name'], cou['screenName'],
                cou['email'], cou['phone'], cou['adress'],
                cou['password'], cou['group'])
            return cou
        else:
            cou = self.mysql.select_courier_multi(method, value)
            if cou == []:
                raise Exception('Error:No find such ' + method + '!')
            return cou


def add_courier(self, name, screenName, email, phone, adress,
                          password):
    # 添加一条管理员
    sql = '''
            INSERT INTO `couriers`
            (`name`,`screenName`,`email`,`phone`,`adress`,`password`)
            VALUE ('%s', '%s', '%s', '%s', '%s', '%s')
        ''' % (name, screenName, email, phone, adress, password)
    return self.do_sql(sql)

def delete_courier(self, aid):
    sql = '''
        UPDATE `couriers`
        SET `status` = 'deleted'
        WHERE `aid` = '%s'
        ''' % (aid)
    return self.do_sql(sql)

def update_courier(self, aid, name, screenName, email, phone,
                            adress, password):
    sql = '''
        UPDATE `couriers`
        SET `name` = '%s',
        `screenName` = '%s',
        `email` = '%s',
        `phone` = '%s',
        `adress` = '%s',
        `password` = '%s'
        WHERE `aid` = '%s'
        ''' % (name, screenName, email, phone, adress, password, aid)
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
        ORDER BY `aid`
        DESC
        ''' % (method, value)
    return self.do_sql_multi(sql)