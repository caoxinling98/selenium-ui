from __future__ import print_function
import pytest

@pytest.fixture(scope='module')
def resource_a_setup(request):
    print('\nresources_a_setup()')
    def resource_a_teardown():
        print('\nresources_a_teardown()')
    request.addfinalizer(resource_a_teardown)

def test_1(resource_a_setup):
    print('test_1()')

def test_2():
    print('\ntest_2()')

def test_3(resource_a_setup):
    print('\ntest_3()')