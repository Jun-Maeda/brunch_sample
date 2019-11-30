class delete:
    def __init__(self,user_name):
        self.user_name = user_name
    def delete_data(self):
        print(f'{self.user_name}を消しました。')


myname = delete(user_name='myname')
myname.delete_data()