Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:05:53) 
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /Users/michaelkhanda/Documents/SUMMER SEMESTER 2021/IST1025/Week 3.2 python.py
0 10000 600.0
Total Interest:  600.0
Total Principal:  10600.0
1 10600.0 636.0
Total Interest:  1236.0
Total Principal:  11236.0
2 11236.0 674.16
Total Interest:  1910.16
Total Principal:  11910.16
3 11910.16 714.61
Total Interest:  2624.77
Total Principal:  12624.77
4 12624.77 757.49
Total Interest:  3382.26
Total Principal:  13382.26
>>> X = 13382.255776
>>> # Use an f-string to format the output
>>> print(f'The amount is {x: .2f}')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(f'The amount is {x: .2f}')
NameError: name 'x' is not defined
>>> x = 13382.255776
>>> # Use an f-string to format the output
>>> print(f'The amount is {x: .2f}')
The amount is  13382.26
>>> print(f'The amount is ${x: .2f}')
The amount is $ 13382.26
>>> 