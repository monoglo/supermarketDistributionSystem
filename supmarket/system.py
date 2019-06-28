import module.User
import module.SupermarketDB
import re
import json

logined_identity = 'logout'


class System:
    administrator = 0
    customer = 0
    courier = 0
    logined = 0
    mysql = module.SupermarketDB.SupermarketDB('localhost', 'root', 'ying8rui',
                                               'supermarket')

    def permission_detect(permission_node):
        global logined_identity

        def wrapper(func, *args):
            def inner_wrpaper(*args):
                jsonfile = json.load(open("supmarket/group.json"))
                string = jsonfile[logined_identity]['permission_node']
                if string is None:
                    raise Exception('No such GROUP！')
                c = 0
                for item in string:
                    a = item[0:1]
                    b = item[1:]
                    if re.match(b, permission_node) is not None:
                        if a == '+':
                            c = 1
                            break
                        else:
                            raise Exception('Permission denied!')
                if c == 0:
                    raise Exception('Permission denied!')
                return func(*args)

            return inner_wrpaper

        return wrapper

    @permission_detect(permission_node='admin.create')
    def create_account_administrator(self, name, screenName, email, phone,
                                     adress, password):
        self.mysql.add_administrator(name, screenName, email, phone, adress,
                                     password)

    @permission_detect(permission_node='admin.delete')
    def delete_account_administrator(self, aid):
        self.mysql.delete_administrator(aid)

    @permission_detect(permission_node='admin.update')
    def update_account_administrator(self, aid, name, screenName, email, phone,
                                     adress, password, group):
        self.mysql.update_administrator(aid, name, screenName, email, phone,
                                        adress, password, group)

    @permission_detect(permission_node='admin.search')
    def search_account_administrator(self, method, value, is_singal):
        if is_singal == 1:
            admin = self.mysql.select_administrator_singal(method, value)
            if admin == []:
                raise Exception('Error:No such ' + method + '!')
            self.administrator = module.User.Administrator(
                admin['aid'], admin['name'], admin['screenName'],
                admin['email'], admin['phone'], admin['adress'],
                admin['password'], admin['group'])
            return admin
        else:
            admin = self.mysql.select_administrator_multi(method, value)
            if admin == []:
                raise Exception('Error:No find such ' + method + '!')
            return admin

    @permission_detect(permission_node='customer.create')
    def create_account_customer(self, name, screenName, email, phone, adress,
                                password):
        self.mysql.add_customer(name, screenName, email, phone, adress,
                                password)

    @permission_detect(permission_node='customer.delete')
    def delete_account_customer(self, cuid):
        self.mysql.delete_customer(cuid)

    @permission_detect(permission_node='customer.update')
    def update_account_customer(self, cuid, name, screenName, email, phone,
                                adress, password):
        self.mysql.update_customer(cuid, name, screenName, email, phone,
                                   adress, password)

    @permission_detect(permission_node='customer.search')
    def search_account_customer(self, method, value, is_singal):
        if is_singal == 1:
            cus = self.mysql.select_customer_singal(method, value)
            if cus == []:
                raise Exception('Error:No such ' + method + '!')
            self.customer = module.User.customer(cus['cuid'], cus['name'],
                                                 cus['screenName'],
                                                 cus['email'], cus['phone'],
                                                 cus['adress'],
                                                 cus['password'], cus['group'],
                                                 cus['balance'])
            return cus
        else:
            cus = self.mysql.select_customer_multi(method, value)
            if cus == []:
                raise Exception('Error:No find such ' + method + '!')
            return cus

    @permission_detect(permission_node='courier.create')
    def create_account_courier(self, name, screenName, email, phone, adress,
                               password):
        self.mysql.add_courier(name, screenName, email, phone, adress,
                               password)

    @permission_detect(permission_node='courier.delete')
    def delete_account_courier(self, coid):
        self.mysql.delete_courier(coid)

    @permission_detect(permission_node='courier.update')
    def update_account_courier(self, coid, name, screenName, email, phone,
                               adress, password):
        self.mysql.update_courier(coid, name, screenName, email, phone, adress,
                                  password)

    @permission_detect(permission_node='courier.search')
    def search_account_courier(self, method, value, is_singal):
        if is_singal == 1:
            cou = self.mysql.select_courier_singal(method, value)
            if cou == []:
                raise Exception('Error:No such ' + method + '!')
            self.courier = module.User.courier(cou['coid'], cou['name'],
                                               cou['screenName'], cou['email'],
                                               cou['phone'], cou['adress'],
                                               cou['password'], cou['group'],
                                               cou['deliveryTimes'],
                                               cou['salary'])
            return cou
        else:
            cou = self.mysql.select_courier_multi(method, value)
            if cou == []:
                raise Exception('Error:No find such ' + method + '!')
            return cou

    @permission_detect(permission_node='good.create')
    def create_good(self, productNumber, name, type, expireDate, unit,
                    quantity, price, cost):
        self.mysql.add_good(productNumber, name, type, expireDate, unit,
                            quantity, price, cost)

    @permission_detect(permission_node='good.delete')
    def delete_good(self, gid):
        self.mysql.delete_good(gid)

    @permission_detect(permission_node='good.search')
    def search_good(self, method, value, is_singal):
        if is_singal == 1:
            goo = self.mysql.select_good_singal(method, value)
            if goo == []:
                raise Exception('Error:No such ' + method + '!')
            return goo
        else:
            goo = self.mysql.select_good_multi(method, value)
            if goo == []:
                raise Exception('Error:No find such ' + method + '!')
            return goo

    @permission_detect(permission_node='good.search')
    def search_outdate_good(self):
        goo = self.mysql.select_outdate_good_multi('all', '1')
        if goo == []:
            raise Exception('Error:No find outdate goods !')
        return goo

    @permission_detect(permission_node='order.create')
    @permission_detect(permission_node='order.create')
    def create_order(self, cuid):
        return self.mysql.add_order(cuid)

    @permission_detect(permission_node='order.add')
    def add_order_item(self, oid, gid, productNumber, unit, quantity, price,
                       amount):
        self.mysql.add_order_item(oid, gid, productNumber, unit, quantity,
                                  price, amount)

    @permission_detect(permission_node='order.search')
    def search_order(self, method, value, is_singal):
        if is_singal == 1:
            orde = self.mysql.select_order_singal(method, value)
            if orde == []:
                raise Exception('Error:No such ' + method + '!')
            return orde
        else:
            orde = self.mysql.select_order_multi(method, value)
            if orde == []:
                raise Exception('Error:No find such ' + method + '!')
            return orde

    @permission_detect(permission_node='order.delete')
    def delete_order(self, oid):
        self.mysql.delete_order(oid)

    @permission_detect(permission_node='system.base.login')
    def login(self, username, password, identity):
        global logined_identity
        if identity == 'administrator':
            admin = self.search_account_administrator('name', username, 1)
            if admin is not None and admin['password'] == password:
                self.logined = admin
                logined_identity = admin['group']
                self.administrator = module.User.Administrator(
                    admin['aid'], admin['name'], admin['screenName'],
                    admin['email'], admin['phone'], admin['adress'],
                    admin['password'], admin['group'])
                return logined_identity
            else:
                raise Exception('Error:Password wrong!')
        elif identity == 'customer':
            pass
        elif identity == 'courier':
            pass
        else:
            raise Exception('Error:Undefined indntity!')

    @permission_detect(permission_node='system.base.logout')
    def logout(self):
        self.logined = 0
        self.logined_identity = 'logout'
        self.mysql.close_conn()


def test():
    sy = System()

    sy.login('yingrui', 'password', 'administrator')

    sy.logout()


if __name__ == "__main__":
    test()
