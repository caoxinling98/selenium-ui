class A():
    def testA(self):
        print('a------------')

class B():
    def testB(self):
        print('b-----------')

class C(A,B):
    def testC(self):
        print('c-----------')

c = C()
c.testA()
c.testB()
c.testC()