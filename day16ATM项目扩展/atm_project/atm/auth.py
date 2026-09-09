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


# 新增: 修改密码
def change_password(acc_info, card_num):
    """
    修改密码
    :param acc_info: 信息字典
    :param card_num: 卡号
    :return:
    """
    old_password = input("请输入密码").strip()
    if old_password != acc_info[card_num]["password"]:
        print("旧密码错误！")
        return
    new_password = input("请输入新密码:").strip()
    confirm_password = input("请再次输入新密码:").strip()
    if new_password == confirm_password:
        acc_info[card_num]['password'] = new_password
        print("密码修改成功！")
    else:
        print("两次密码输入不一致！")


if __name__ == '__main__':
    # ================ 测试登录 ==================
    from accounts import read_accounts
    # 读取账户信息
    accs = read_accounts()
    # 登录
    login(accs)

