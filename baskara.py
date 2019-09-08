import math
a = float (input())
b = float (input())
c = float (input())
R1 = 0
R2 = 0
delta = (b**2)- (4 * a * c)
if (delta < 0 or a == 0):
    print ( " Impossível calcular " )
else :
    calc = math.sqrt (delta)
    R1 = ( - b + delta) / ( 2 * a)
    R2 = ( - b - delta) / ( 2 * a)
    print ( f' R1 ={R1:.5f} ')
    print (f' R2 ={R2:.5f}')
