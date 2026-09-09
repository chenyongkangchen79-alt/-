# 负责用户认证


def login(accounts):
    """
    用户登录功能
    :param accounts: 账户信息字典，包含所有用户信息的

    :return: 登录成功的卡号，如果登录失败无返回值
    """
    # 获取用户输入的卡号
    card_num = input("请输入您的卡号:")
    # 获取用户输入的密码
    password = input("请输入您的密码:")
    """
    dic = {
        '123456': 
            {'password': '1111', 'balance': 1000.0}, 
        '654321': 
            {'password': '2222', 'balance': 500.0}
    }
    """
    # 验证卡号是否存在且密码正确
    if card_num in accounts and accounts[card_num]["password"] == password:
        print("登录成功！")
        return card_num
    else:
        print("卡号或者密码错误")
        return None


if __name__ == '__main__':
    # ================ 测试登录 ==================
    from accounts import read_accounts
    # 读取账户信息
    accs = read_accounts()
    # 登录
    login(accs)

