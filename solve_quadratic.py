def solve_quadratic(a,b,c):

    if a == 0:
        print ('No solution')
    else:
        import math

        d = (b**2) - (4*a*c)

        sol1 = (-b-math.sqrt(d))/(2*a)
        sol2 = (-b+math.sqrt(d))/(2*a)

        print ('The solution:')

        try:
            tmp = int(sol1)
            print(sol1)
        except:
            print('The variable is not a number')

        try:
            tmp = int(sol2)
            print(sol2)
        except:
            print('The variable is not a number')


solve_quadratic(1,-5,6)    
