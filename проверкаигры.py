print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Введите целое число => ")))#abs-модуль числа(вводишь отрицательное число оно становится положительным)
        break
    except ValueError:
         print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Нет смысла ничего делать с нулём")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
    c=b=a
    paaris =0
    paaritu = 0
    while b > 0:
            if b % 2 == 0:#остаток от деления =0 значит оно положительное
                paaris += 1
            else:
                paaritu += 1
            b = b // 10
    
    print("Чётных цифр:",paaris)
    print("Нечётных цифр:",paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b+=number 
    print("*Перевёрнутое* число", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз:")
    print()
    if c % 2==0:
        print(c ,"- чётное число. Делим на 2.")
    else:
        print(c ,"-нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c != 1:
            if c % 2 ==0:
                    c = c / 2
            else:
                    c = (3*c + 1) / 2
            print(c,end=" ")
    print()
    print("Гипотеза вернa")