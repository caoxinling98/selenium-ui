import pytest

@pytest.fixture()
def test1():
    print('\n开始执行function')

@pytest.mark.usefixtures('test1')
def test_a():
    print('---用例a执行---')

@pytest.mark.usefixtures('test1')
class TestClass():

    def test_b(self):
        print('---用例b执行---')

    def test_c(self):
        print('---用例c执行---')

if __name__ == '__main__':
    pytest.main(['-s','test_demo3.py'])