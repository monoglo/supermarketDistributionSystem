import module.User
import module.SupermarketDB


class System:
    administrator = 0
    customer = 0
    courier = 0
    logined = 0
    logined_identity = 'logout'
    user = module.User.User('yingrui', 'matrix', '123@gmail.com', '138', 'YSU',
                            'password')
    user_group = 'default'
    mysql = module.SupermarketDB.SupermarketDB('localhost', 'root', 'ying8rui',
                                               'supermarket')

    def create_account_administrator(self, name, screenName, email, phone,
                                     adress, password):
        self.mysql.add_administrator(name, screenName, email, phone, adress,
                                     password)

    def delete_account_administrator(self, aid):
        self.mysql.delete_administrator(aid)

    def update_account_administrator(self, aid, name, screenName, email, phone,
                                     adress, password):
        self.mysql.update_administrator(aid, name, screenName, email, phone,
                                        adress, password)

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

    def create_account_customer(self, name, screenName, email, phone, adress,
                                password):
        self.mysql.add_customer(name, screenName, email, phone, adress,
                                password)

    def delete_account_customer(self, cuid):
        self.mysql.delete_customer(cuid)

    def update_account_customer(self, cuid, name, screenName, email, phone,
                                adress, password):
        self.mysql.update_customer(cuid, name, screenName, email, phone,
                                   adress, password)

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

    def create_account_courier(self, name, screenName, email, phone, adress,
                               password):
        self.mysql.add_courier(name, screenName, email, phone, adress,
                               password)

    def delete_account_courier(self, coid):
        self.mysql.delete_courier(coid)

    def update_account_courier(self, coid, name, screenName, email, phone,
                               adress, password):
        self.mysql.update_courier(coid, name, screenName, email, phone, adress,
                                  password)

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

    def login(self, username, password, identity):
        if identity == 'administrator':
            admin = self.search_account_administrator('name', username, 1)
            if admin['password'] == password:
                self.logined = admin
                self.logined_identity = admin['group']
                self.administrator = module.User.Administrator(
                    admin['aid'], admin['name'], admin['screenName'],
                    admin['email'], admin['phone'], admin['adress'],
                    admin['password'], admin['group'])
                return self.logined_identity
            else:
                raise Exception('Error:Password wrong!')
        elif identity == 'customer':
            pass
        elif identity == 'courier':
            pass
        else:
            raise Exception('Error:Undefined indntity!')

    def logout(self):
        self.logined = None
        self.logined_identity = 'logout'


if __name__ == "__main__":
    sy = System()
    try:
        a = sy.create_account_courier('htr', 'hhh', '@qq', '133', 'YSU', 'qwerty')
        print(a)
    except Exception as e:
        print(e)
    sy.logout()
