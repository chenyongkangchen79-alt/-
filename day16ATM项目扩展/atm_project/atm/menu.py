# 负责显示主菜单和处理用户输入
# 使用相对导入之后就不能直接运行了
from .operations import check_balance, deposit, withdraw, transfer
from .auth import change_password


def main_menu(accounts, card_num):
    """
    显示ATM主菜单并处理用户输入
    :param accounts: 账户信息
    :param card_num: 当前登录的卡号
    :return:
    """
    while True:
        # 菜单显示部分
        print("\n========= ATM菜单 ==========")
        print("1.查询余额")
        print("2.存款")
        print("3.取款")
        print("4.修改密码")
        print("5.转账")
        print("6.退出")

        # 菜单选择并处理
        choice = input("请选择想要的操作(序号):").strip()
        if choice == "1":
            balance = check_balance(accounts, card_num)
            print(f"当前的余额为: {balance}")
        elif choice == "2":
            deposit(accounts, card_num)
        elif choice == "3":
            withdraw(accounts, card_num)
        elif choice == "4":
            change_password(accounts, card_num)
        elif choice == "5":
            transfer(accounts, card_num)
        elif choice == "6":
            print("感谢使用ATM，再见👋")
            # 跳出本层循环
            break
        else:
            print("无效的选择，请重新输入")


if __name__ == '__main__':
    from accounts import read_accounts, init_accounts
    from auth import login
    # 初始化账户信息
    init_accounts()
    # 读取账户信息
    accounts = read_accounts()
    # 登录
    card_num = login(accounts)
    # 显示主菜单
    main_menu(accounts, card_num)





