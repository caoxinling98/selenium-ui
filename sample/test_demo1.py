import pytest
class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    @pytest.mark.a
    def test_two(self):
        x = 'check'
        assert hasattr(x,'check')

    @pytest.mark.b
    def test_a(self):
        assert 1 == 2
