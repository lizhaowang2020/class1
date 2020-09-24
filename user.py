from werkzeug import generate_password_hash, check_password_hash

class User:
    ''' ??????????
    '''

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = self.save_password(password)

    def check_email(self, email):
        return self.email == email

    def save_password(self, password):
        '''?? hash ?????
        '''
        return generate_password_hash(password)

    def check_password(self, password):
        '''?? hash ???????????
        '''
        return check_password_hash(self.password_hash,password)
        

def main():
    userList = [] #??????
    print('?????????? ?? ??????????')
    while 1:
        choose = int(input('''
        ????
        1. ??
        2. ??
        3. ??
        '''))
        if choose == 1:
            # ??????
            print(' ???:')

            # ??????
            name = input('name:')
            email = input('email:')
            password = input('password:')

            # ??????????
            # 1. ?????
            # 2. ?? hash ??
            # 3. ?????????
            # 
            newUser= User(name,email,password) 
            userList.append(newUser)
        if choose == 2:
            # ??????
            print(' ???:')
            email = input('email:')
            password = input('password:')
            inList = False
            # ?????????email???????
            for user in userList:
               if user.check_email(email):
                   inList = True
                   if user.check_password(password):
                       print('登录成功')
                   else:
                       print('用户名或密码错误')
                       break
            if inList == False:
                print('请输入正确的email')

        if choose == 3:
            break

if __name__ == '__main__':
    main()
