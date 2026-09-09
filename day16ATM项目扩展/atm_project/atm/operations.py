# 负责ATM的各种操作(查余额、存款、取款)
from .Atmlogger import log_action
import logging

# logger
logger = logging.getLogger(__name__)


def check_balance(accounts, card_num):
    """
    查询余额
    :param accounts: 账户信息
    :param card_num: 卡号(登录之后返回的卡号)
    :return:
    """
    balance = accounts[card_num]["balance"]
    # print(f"当前余额: {balance}元")
    return balance


def deposit(accounts, card_num):
    """
    存款
    :param accounts:
    :param card_num:
    :return:
    """
    amount = float(input("请输入存款余额:"))
    if amount > 0:
        accounts[card_num]["balance"] += amount
        print(f"存款成功！当前余额: {check_balance(accounts, card_num)}元")
    else:
        print("存款金额必须大于0")


def withdraw(accounts, card_num):
    """
    取款的操作
    :param accounts:
    :param card_num:
    :return:
    """
    amount = float(input("请输入取款金额:"))
    # 校验金额合法性
    if 0 < amount <= check_balance(accounts, card_num):
        accounts[card_num]["balance"] -= amount
        print(f"取款成功!当前余额: {check_balance(accounts, card_num)}元")
    else:
        print("取款金额无效或者余额不足！")


# 新增: 转账操作
def transfer(acc_info, card_num):
    """
    转账
    :param acc_info:
    :param card_num:
    :return:
    """
    target_card_num = input("请输入对方卡号:").strip()
    if target_card_num not in acc_info:
        print("账户不存在！")
        return
    amount = float(input("请输入转账的金额:"))
    # 判断amount合法性
    if 0 < amount <= acc_info[card_num]["balance"]:
        # 转账操作
        # 1 当前登录用户余额 减去 转账的金额
        acc_info[card_num]['balance'] -= amount
        # 2 目标账户余额增加
        acc_info[target_card_num]['balance'] += amount
        print(f"转账成功！当前余额: {check_balance(acc_info, card_num)}元")
        log_action(logger, f"用户{card_num}向{target_card_num}转账{amount}元.")
    else:
        print("转账金额无效或者余额不足！")


if __name__ == '__main__':
    from accounts import read_accounts
    accs = read_accounts()
    # 查询余额
    print(check_balance(accs, "123456"))
    print(check_balance(accs, "654321"))
    # 存款
    deposit(accs, "123456")
    # 取款
    withdraw(accs, "123456")



