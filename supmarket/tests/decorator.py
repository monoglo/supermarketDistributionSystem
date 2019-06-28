import re
string = {'+*'}


def permission_detect(permission_node):
    global string

    def wrapper(func):
        c = False
        for item in string:
            a = item[0:1]
            b = item[1:]
            if re.match('.*', permission_node):
                if a == '+':
                    c = True
                    break
                else:
                    raise Exception('Error')
        if c is False:
            raise Exception('Error')
        func()
    return wrapper


@permission_detect(permission_node='speak.read')
def main():
    print('middle')
