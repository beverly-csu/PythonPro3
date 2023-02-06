# напиши код для выполнения заданий здесь
count = 0
with open('my_file.txt') as file:
    for string in file:
        string = string.split()
        count += string.count('1')

print('Количество единиц:', count)

with open('my_file.txt') as file:
    lines = file.readlines()
    items = lines[13].split()
    print('8 элемент 14 строки:', items[7])

from time import time

start = time()
summ = 0
with open('my_file.txt') as file:
    for string in file:
        items = string.split()
        for i in items:
            summ += int(i)

print('Сумма всех элементов:', summ)
end = time()
print('First:', res1:=end-start)

start = time()
with open('my_file.txt') as file:
    data = file.read()
    data = data.split()
    data = list(map(int, data))
    print(sum(data))
end = time()
print('Second:', res2:=end-start)
print(res1 // res2)