import pytest
from project import add_transaction, query_transactions, generate_report

# 使用 pytest fixture 提供一组示例交易记录，方便多个测试复用
@pytest.fixture
def sample_transactions():
    return [
        {"date": "2025-01-01", "category": "income", "amount": 1000.0, "note": "Salary"},
        {"date": "2025-01-02", "category": "expense", "amount": 200.0, "note": "Groceries"},
        {"date": "2025-01-03", "category": "expense", "amount": 50.0, "note": "Snacks"}
    ]

def test_add_transaction_valid(sample_transactions):
    """
    测试添加交易记录时，输入合法数据是否能正确添加记录。
    """
    original_count = len(sample_transactions)
    new_tran = add_transaction(sample_transactions, "2025-01-04", "income", "500", "Bonus")
    # 检查返回的记录是否在 transactions 列表中，且列表长度增加了1
    assert new_tran in sample_transactions
    assert len(sample_transactions) == original_count + 1

def test_add_transaction_invalid_date(sample_transactions):
    """
    测试添加交易记录时，输入错误格式的日期是否会抛出 ValueError 异常。
    """
    with pytest.raises(ValueError):
        add_transaction(sample_transactions, "2025/01/04", "income", "500", "Bonus")

def test_query_transactions_by_category(sample_transactions):
    """
    测试根据类别筛选交易记录是否正确返回预期的记录。
    """
    results = query_transactions(sample_transactions, category="income")
    # 这里只有一条收入记录
    assert len(results) == 1
    for tran in results:
        assert tran['category'] == "income"

def test_query_transactions_by_date(sample_transactions):
    """
    测试根据起始日期筛选交易记录，确保返回的记录日期均大于等于指定日期。
    """
    results = query_transactions(sample_transactions, start_date="2025-01-02")
    # 从第二天开始应返回2条记录
    assert len(results) == 2
    for tran in results:
        assert tran['date'] >= "2025-01-02"

def test_generate_report(sample_transactions):
    """
    测试生成财务报表是否正确统计收入、支出和净收入。
    """
    report = generate_report(sample_transactions)
    assert report['total_income'] == 1000.0
    assert report['total_expense'] == 250.0  # 200 + 50
    assert report['net'] == 750.0
