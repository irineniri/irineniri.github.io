def solve_quadratic(a,b,c):

    if a == 0:
        print ('No solution')
    else:
        import math

        d = (b**2) - (4*a*c)

        sol1 = (-b-math.sqrt(d))/(2*a)
        sol2 = (-b+math.sqrt(d))/(2*a)

        print ('The solution:') 
        print (sol1)
        print (sol2)

solve_quadratic(1,-5,6)
