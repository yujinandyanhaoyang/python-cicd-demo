from src.calculator import add, multiply  # 从 src 包导入

def test_add():
    assert add(1, 2) == 3

def test_multiply():
    assert multiply(3, 4) == 12
