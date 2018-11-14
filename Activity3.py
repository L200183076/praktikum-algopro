Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama='Indraswari Wahyu Pertiwi'
>>> NIM='L200183076'
>>> X='1'+NIM[7:]
>>> a=int(X)
>>> b=len(Nama)
>>> type(a)
<class 'int'>
>>> #This command is used to find the class (data type) of variable "a". And the data type of variable "a" is int (Integer)
>>> type(b)
<class 'int'>
>>> #This command is used to find the class (data type) of variable "b". And the data type of variable "b" is int (Integer)
>>> a/b
44.833333333333336
>>> #This command is used to divide the variable "a" by the variable "b". and the result is in float, it is 44.833333333333336
>>> a//b
44
>>> #This command is used to divide the variable "a" by the variable "b". and the result is in integer, it is 44
>>> 10*(a-99)
9770
>>> #This command is used to find the result of mathematic opration. The variable "a" is minus by 99, and then multiplied by 10. And the result is 9770
>>> b**2
576
>>> #This command is used to find the result of variable "b" powered by 2. And the result is 576
>>> a%b
20
>>> #This command is used to find the rest of divider from the division of variable "a" by variable "b". And the result is 20
>>> c=12.5
>>> #This command is used to give value of the variable "c" by 12.5
>>> type(c)
<class 'float'>
>>> #This command is used to find the data type of the variable "c". And the data type of variable "c" is float (real number)
>>> a/c
86.08
>>> #This command is used to divide the variable "a" by the variable "c". And the result is in float, it is 86.08
>>> a//c
86.0
>>> #This command is used to divide the variable "a" by the variable "c". And the result is in float, it is 86.0
>>> a%c
1.0
>>> #This command is used to find the rest of divider from the division of variable "a" by variable "c". And the result is 1.0
>>> c>b
False
>>> #This command is used to check the result if the operation is true or false. The result from variable "c" is bigger than variable "b" is false.
>>> type(c>b)
<class 'bool'>
>>> #This command is used to find the data type of operation "variable c is bigger than variable b". And the data type is bool (Boolean).
>>> a>b and b>c
True
>>> #This command is used to check the result of the operation "variable a is bigger than variable b" and the operation "variable b is biger than variable c". And the result is true
>>> a>1100 or b<10
False
>>> #This command is used to check the result of the operation "variable a is bigger than variable 1100" and the operation "variable b is biger than variable 10". And the result is False
