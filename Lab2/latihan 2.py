print ('program untuk mengurutkan bilangan dari yang terkecil ke terbesar')

def pengulangan():
    print ('masukkan 3 bilangan yang diinginkan!')
    a=int(input('bilangan 1 = '))
    b=int(input('bilangan 2 = '))
    c=int(input('bilangan w3 = '))

    if a<b and a<c:
        if b<c:
            print(a, b, c)
        else:
            print(a, c, b)
    elif b<a and b<c:
        if a<c:
            print(b, a, c)
        else:
            print(b, c, a)
    else:
        if a<b:
            print(c, a, b)
        else:
            print(c, b, a)

    print("")
    print('ingin coba lagi? (ya/tidak)')
    x=input()
    if x=='ya':
        return pengulangan()
    if x=='tidak':
        print('terima kasih telah menggunakan program ini.')
pengulangan()