
print('program menentukan nilai maksimum tiga bilangan')
 
a = int(input('masukan bilangan ke-1: '))
b = int(input('masukan bilangan ke-2: '))
c = int(input('masukan bilangan ke-3: '))
 
if a > b:
        if a > c:
            maks = a
else:
        if b > c:
            maks = b
        else:
            maks = c
print('Nilai yang terbesar adalah: %s' %maks)
         