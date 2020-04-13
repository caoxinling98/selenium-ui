import abc
class Pci(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    def test1(self):
        print('test1---')

#网卡
class NetWork(Pci):
    def start(self):
        print('开始发送网络数据')

    def stop(self):
        print('停止发送网络数据')

    def test1(self):
        print('test1---NetWork')

#声卡
class Sound(Pci):
    def start(self):
        print('开始发送声音数据')

    def stop(self):
        print('停止发送声音数据')
#抽象类有抽象方法不能被实例化
# pci = Pci()
# pci.test1()
net = NetWork()
net.start()
net.stop()
net.test1()