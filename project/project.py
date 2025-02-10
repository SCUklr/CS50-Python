import re
import json
from datetime import datetime

DATA_FILE = 'transactions.json'

def load_transactions():
    """从 JSON 文件加载交易记录，如果文件不存在则返回空列表。"""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            transactions = json.load(f)
    except FileNotFoundError:
        transactions = []
    return transactions

def save_transactions(transactions):
    """将交易记录保存到 JSON 文件中。"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(transactions, f, indent=4)

def add_transaction(transactions, date_str, category, amount, note):
    """
    添加一条新的交易记录。
    使用正则表达式验证日期格式 (YYYY-MM-DD) 以及转换金额为浮点数。
    """
    # 验证日期格式是否符合 YYYY-MM-DD
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        raise ValueError("日期格式错误，必须为 YYYY-MM-DD")
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("无效的日期")

    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("金额必须为数字")

    transaction = {
        "date": date_str,
        "category": category.lower(),  # 例如：income 或 expense
        "amount": amount,
        "note": note
    }
    transactions.append(transaction)
    return transaction

def query_transactions(transactions, start_date=None, end_date=None, category=None):
    """
    根据可选的起始日期、结束日期和类别筛选交易记录。
    """
    result = []
    for t in transactions:
        include = True
        if start_date and t['date'] < start_date:
            include = False
        if end_date and t['date'] > end_date:
            include = False
        if category and t['category'] != category.lower():
            include = False
        if include:
            result.append(t)
    return result

def generate_report(transactions):
    """
    根据所有交易记录生成报表，统计总收入、总支出及净收入。
    假定 category 为 'income' 或 'expense'
    """
    total_income = 0.0
    total_expense = 0.0
    for t in transactions:
        if t['category'] == 'income':
            total_income += t['amount']
        elif t['category'] == 'expense':
            total_expense += t['amount']
    report = {
        "total_income": total_income,
        "total_expense": total_expense,
        "net": total_income - total_expense
    }
    return report

def main():
    """程序主入口，提供简单的命令行交互菜单。"""
    transactions = load_transactions()

    while True:
        print("\n个人财务管理系统")
        print("1. 添加交易记录")
        print("2. 查询交易记录")
        print("3. 生成财务报表")
        print("4. 退出")
        choice = input("请选择操作：").strip()

        if choice == '1':
            date_str = input("请输入日期 (YYYY-MM-DD)：").strip()
            category = input("请输入类别 (income/expense)：").strip()
            amount = input("请输入金额：").strip()
            note = input("请输入备注：").strip()
            try:
                transaction = add_transaction(transactions, date_str, category, amount, note)
                print("成功添加交易记录：", transaction)
            except ValueError as e:
                print("错误：", e)
        elif choice == '2':
            start_date = input("请输入起始日期 (YYYY-MM-DD)，可留空：").strip() or None
            end_date = input("请输入结束日期 (YYYY-MM-DD)，可留空：").strip() or None
            category = input("请输入类别 (income/expense)，可留空：").strip() or None
            results = query_transactions(transactions, start_date, end_date, category)
            print("查询结果：")
            for t in results:
                print(t)
        elif choice == '3':
            report = generate_report(transactions)
            print("财务报表：")
            print("总收入：", report['total_income'])
            print("总支出：", report['total_expense'])
            print("净收入：", report['net'])
        elif choice == '4':
            save_transactions(transactions)
            print("交易记录已保存，程序退出。")
            break
        else:
            print("无效的选项，请重试。")

if __name__ == '__main__':
    main()
