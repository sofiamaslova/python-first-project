n = int(input())
# if n < 0: 
#    print('vvedite naturalnoe chislo')
# else: 
    if n >= 0 and n <= 1:
        print('factorial chisla', n, '=1')
    else:  
        
        
        def factorial(n):
            sp = range(2,n+1)
            result = 1
            for i in sp:
                result = result*i
            return result

        print(factorial(n))

