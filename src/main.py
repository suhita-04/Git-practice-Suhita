import datetime 
from utils import add, subtract, multiply, divide 
 
print('Name: Suhita') 
print(f'Date: {datetime.date.today()}') 
print('5 + 3 =', add(5, 3)) 
print('10 - 4 =', subtract(10, 4)) 
print('4 * 2 =', multiply(4, 2)) 
 
try: 
    print('10 / 0 =', divide(10, 0)) 
except ValueError as e: 
    print('Error:', e) 
