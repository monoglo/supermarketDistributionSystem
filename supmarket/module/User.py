class User:
    name = ''
    screenName = ''  # User Displayed Name
    email = ''
    phone = ''
    adress = ''
    group = 'default'
    _password = ''

    def __init__(self, name, screenName, email, phone, adress, password):
        self.name = name
        self.screenName = screenName
        self.email = email
        self.phone = phone
        self.adress = adress
        self._password = password

    def show_id(self):
        return self.id

    def show_name(self):
        return self.name

    def show_screenName(self):
        return self.screenName

    def show_email(self):
        return self.email

    def show_phone(self):
        return self.phone

    def show_adress(self):
        return self.adress

    def show_group(self):
        return self.group

    def show_password(self):
        return self._password

# ↑ show ↑  ↓ set ↓

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_screenName(self, screenName):
        self.screenName = screenName

    def set_email(self, email):
        self.email = email

    def set_phone(self, phone):
        self.phone = phone

    def set_adress(self, adress):
        self.adress = adress

    def set_password(self, password):
        self._password = password

    def set_group(self, group):
        self.group = group


class Courier(User):
    def __init__(self, coid, name, screenName, email, phone, adress, password,
                 group, times_delivery, salary):
        User.__init__(self, name, screenName, email, phone, adress, password)
        self.group = group
        self.times_delivery = times_delivery
        self.salary = salary
        self.coid = coid
    # 配送员接单

    def courier_order(self, id_order):
        pass

    # 配送员完成订单

    def courier_order_finish():
        pass


class Customer(User):
    def __init__(self, cuid, name, screenName, email, phone, adress, password,
                 group, balance):
        User.__init__(self, name, screenName, email, phone, adress, password)
        self.group = group
        self.balance = balance
        self.cuid = cuid


class Administrator(User):
    def __init__(self, aid, name, screenName, email, phone, adress, password,
                 group):
        User.__init__(self, name, screenName, email, phone, adress, password)
        self.group = group
        self.aid = aid


if __name__ == '__main__':
    u1 = Customer('yingrui', 'matrix', '123@gmail.com', '138', 'YSU',
                  'password')
    print(u1.show_group())
