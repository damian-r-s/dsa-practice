def isHappyNumber(n: int) -> bool:
    sett = set()
    
    while n != 1:
        n = sum(int(digit) ** 2 for digit in str(n))
        
        if n in sett:
            return False
        sett.add(n)
        
    return True