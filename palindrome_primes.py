def is_prime(n):

    if n > 1:

        for i in range(2, int(n/2)+1):
    
            if (n % i) == 0:
                return False
               
        return True
  
    else:
         return False

def palindrome(num):
    return str(num) == str(num)[::-1]

a=[]

for i in range(9999,99999):
    if palindrome(i) and is_prime(i):
        a.append(i)
print(a)
