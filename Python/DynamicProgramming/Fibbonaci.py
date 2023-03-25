def fibbonaci():
    for cur in (0, 1):
        last = cur
        yield cur
    while True:
        yield cur
        last, cur = cur, last + cur
        
        