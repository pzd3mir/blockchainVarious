from multiprocessing import Process
from threading import Thread

bn = 1
print(bn)

d = "Pirmin Can Ozdemir"
print(d)

ph = "0000000000000000000000000000000000000000000000000000000000000000"
print(ph)

tnonce = 22761
print(tnonce)

a = np.arange(0, 100001, 1)

print("base: " + hashlib.sha256(
    b"122761Pirmin Can Ozdemir0000000000000000000000000000000000000000000000000000000000000000").hexdigest()
      )


class MyThread(threading.Thread):
    def __init__(self, threadID, begin, end):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.end = end
        self.begin = begin

    def run(self):
        for val in range(self.begin, self.end):
            mine(self.threadID, val)
        print("done " + str(self.threadID))

def mine(id, x):
    hash = hashlib.sha256((str(bn) + str(x) + str(d) + str(ph)).encode('utf-8')).hexdigest()
    if hash.find("00000000", 0, 8) > -1:
        # print(id)
        print(x)
        print(hash)

#Possible Combinations 8388608000000

#pc=8388608000000

#Number of Threads:

#nt=16

#Steps

#steps=pc/nt 11915636364

for x in range (1, 704)
    thread = MyThread((x), (x-1), (x))
    thread.start()

thread2 = MyThread(2, 524288000000, 1048576000000)
thread2.start()

thread3 = MyThread(3, 1048576000000, 1572864000000)
thread3.start()

thread4 = MyThread(4, 1572864000000, 2097152000000)
thread4.start()

thread5 = MyThread(5, 2097152000000, 2621440000000)
thread5.start()

thread6 = MyThread(6, 2621440000000, 3145728000000)
thread6.start()

thread7 = MyThread(7, 3145728000000, 3670016000000)
thread7.start()

thread8 = MyThread(8, 3670016000000, 4194304000000)
thread8.start()

thread9 = MyThread(9, 4194304000000, 4718592000000)
thread9.start()

thread10 = MyThread(10, 4718592000000, 5242880000000)
thread10.start()

thread11 = MyThread(11, 5242880000000, 5767168000000)
thread11.start()

thread12 = MyThread(12, 5767168000000, 6291456000000)
thread12.start()

thread13 = MyThread(13, 6291456000000, 6815744000000)
thread13.start()

thread14 = MyThread(14, 6815744000000, 7340032000000)
thread14.start()

thread15 = MyThread(15, 7340032000000, 7864320000000)
thread15.start()

thread16 = MyThread(16, 7864320000000, 8388608000000)
thread16.start()
