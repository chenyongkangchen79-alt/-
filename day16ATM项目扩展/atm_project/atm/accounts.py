# 负责账户信息的读取和初始化
ACCOUNT_FILE = "accounts.txt"  # 常量，存储账户信息的文件


def init_accounts():
    """
    初始化账户信息
    :return:
    """
    # 存储形式: 卡号 密码 余额
    # 123456 1111 1000
    with open(ACCOUNT_FILE, "w", encoding="utf-8") as f:
        # 初始化两个账户信息
        f.write("123456 1111 1000\n")
        f.write("654321 2222 500\n")


def read_accounts():
    """
    读取账户信息
    :return: 字典 accounts
    """
    accounts = {}
    with open(ACCOUNT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            # 读取一行拆分赋值
            card_num, password, balance = line.strip().split()  # ["123456", "1111", "1000"]
            # 组成信息字典
            accounts[card_num] = {"password": password, "balance": float(balance)}
    return accounts


# 新增: 写入账户信息
def write_accounts(acc_info):
    """
    写入账户信息
    :param acc_info: 一直被改动的那个字典(账户信息)
    :return:
    """
    with open(ACCOUNT_FILE, "w", encoding="utf-8") as f:
        for card_num, info in acc_info.items():
            f.write(f"{card_num} {info['password']} {info['balance']}\n")


if __name__ == '__main__':
    # ============== 模块测试: 初始化账户信息 =====================
    init_accounts()
    # ============== 模块测试: 读取账户信息 =====================
    res = read_accounts()
    print(res, type(res))
    """
    dic = {
        '123456': 
            {'password': '1111', 'balance': 1000.0}, 
        '654321': 
            {'password': '2222', 'balance': 500.0}
    }
    """
