while True:
    num = int(input("Translate frfr: "))
    d8= d7=d6=d5=d4=d3=d2=d1=d9=d10= 0
    if num >= 512:
            num -=512
            d10 = 1
    if num >= 256:
            num -=256
            d9 = 1
    if num >= 128:
            num -=128
            d8 = 1
    if num >= 64:
            num -=64
            d7 = 1
    if num >= 32:
            num -=32
            d6 = 1
    if num >= 16:
            num -=16
            d5 = 1
    if num >= 8:
            num -=8
            d4 = 1
    if num >= 4:
            num -=4
            d3 = 1
    if num >= 2:
            num -=2
            d2 = 1
    if num >= 1:
            num -=1
            d1 = 1
    print("Real binary: ",d10,d9,d8,d7,d6,d5,d4,d3,d2,d1)