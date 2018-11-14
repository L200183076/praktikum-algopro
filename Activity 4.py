Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama='Indraswari Wahyu Pertiwi'
>>> NIM=1076
>>> Tinggi=165
>>> Berat=60
>>> TahunLahir=2000
>>> Aku=(TahunLahir,Berat,Tinggi,NIM,Nama)
>>> Data=[TahunLahir,Berat,Tinggi,NIM,Nama]
>>> type(Aku)
<class 'tuple'>
>>> #this command is find the class (data type) of variable "aku". And the data type is tuple
>>> Aku[0]
2000
>>> #this command is used to return value of the first data of "Aku" tuple.
>>> a=NIM%4;Aku[a]
2000
>>> #This value of NIM%4 is 0. The command "Aku[a]" is to looking for data in the "Aku" variable with index a. a equal 0, and the data in the "Aku" variable with index 0 is 2000 (TahunLahir)
>>> type(Aku[a])
<class 'int'>
>>> #this command is used to find the data type of variable "Aku[a]". the data type of "Aku[a]" variable is integer
>>> Aku[a:4]
(2000, 60, 165, 1076)
>>> #this command is used to slice the tuple "Aku" from "a" index until 4th index. The value of "a" variable is 0. So, it will slice data from the index 0 until index 4.
>>> type(Aku[4])
<class 'str'>
>>> #this command is used to find the data type of variable "Aku[]" variable is string
>>> Aku[0]='ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0]='ok'
TypeError: 'tuple' object does not support item assignment
>>> #because "Aku" is tuple, so it is non mutable, can't be edited.
>>> type(Data)
<class 'list'>
>>> #This command is used to find the data type of variable "Data". And the data type of variable "Data" is List. List is a group data that is mutable, it is can be edited.
>>> type(Data[4])
<class 'str'>
>>> #this command is used to find the data type of variable "Data[4]". the data type of "Data[4]" variable is string
>>> Data[4][5]
's'
>>> #the 4th index of "Data" list is "Nama" variable, the command used to return the 5th index value of the "Nama" variable. Then the value is "s"
>>> Data[4][a:6]
'Indras'
>>> #the 4th index of "Data" list is "Nama" variable, index of "a" is 0. This command used to slice the "Nama" variable from the index 0 until 6th index.
>>> Data[0]='ok';Data
['ok', 60, 165, 1076, 'Indraswari Wahyu Pertiwi']
>>> #this command is used to change the 0 index of "Data" list with the "ok" value. Then, the command will return the list of "Data"
>>> Data[-a]
'ok'
>>> #this command is used to return the -a index (-0) of the "Data" list
>>> range(a)
range(0, 0)
>>> #this command is used to make range at range a (0).
>>> 
