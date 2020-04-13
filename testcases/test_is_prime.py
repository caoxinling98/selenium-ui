def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
        return True

# class Test_prime:
#     def test_true(self):
#         assert is_prime(13)
#
#     def test_false(self):
#         assert is_prime(4) is False
#
#     def test_special_num(self):
#         assert is_prime(1) is False


import pytest
#测试用例参数化
@pytest.mark.parametrize(
    "num,expect",
    [
        (13,True),
        (4,False),
        (1,False),
    ],
    ids = ['case1','case2','case3']
)
def test_is_prime(num,expect):
    assert is_prime(num) == expect

if __name__ == '__main__':
    pytest.main(['-v','test_is_prime.py'])
