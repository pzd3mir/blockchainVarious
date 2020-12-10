import random
import hashlib

start = random.randint(0, 8388608000000)
print("starting at nonce", start)

for x in range(start, 8388608000000):
    hash = hashlib.sha256(("1" + str(x) + "Pirmin Can Ozdemir0000000000000000000000000000000000000000000000000000000000000000").encode('utf-8')).hexdigest()
    if hash.find("0000000000", 0, 10) > -1:
        print(x)
        print(hash)
        f = open("Nonce Found!.txt", "w+")
        f.write("--Nonce:")
        f.write(str(x))
        f.write("--Hash:")
        f.write(str(hash))
        f.write("--")
        f.close()