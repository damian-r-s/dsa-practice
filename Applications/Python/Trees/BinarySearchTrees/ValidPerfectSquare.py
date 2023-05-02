def isPerfectSquare(num):        
        i = 1
        j = num        
                      
        while i <= j:
            mid = (i + j) // 2
            mul = mid * mid            
            
            if mul == num:
                return True
            
            if mul < num:
                i = mid + 1
            else:
                j = mid - 1               
                
        return False
                
                
print(isPerfectSquare(14))
print(isPerfectSquare(16))