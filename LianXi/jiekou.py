class Pci:
    def start(self):  #定义规范
        pass

    def stop(self):
        pass

#网卡 -- 实现规范
class NetWork(Pci):
    def start(self):
        print('开始发送数据包。。。')

    def stop(self):
        print('停止发送数据包。。。')

#声卡
class Sound(Pci):
    def start(self):
        print('开始发送声音数据。。。')

    def stop(self):
        print('停止发送声音数据。。。')

network = NetWork()
network.start()
network.stop()

sound = Sound()
sound.start()
sound.stop()