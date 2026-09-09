# ATM程序的入口，启动ATM系统(整合所有的功能)
from atm.accounts import init_accounts, read_accounts, write_accounts
from atm.auth import login
from atm.menu import main_menu


def main():
    """
    主函数，程序入口
    :return:
    """
    # 1 初始化账户信息文件
    init_accounts()
    # 2 读取账户信息
    accs = read_accounts()
    # 3 用户登录认证
    card_num = login(accs)
    # 4 登录成功进入主菜单
    if card_num:
        # 执行菜单显示
        main_menu(accs, card_num)
        # 写入修改之后的账户信息
        write_accounts(accs)


if __name__ == "__main__":
    main()












