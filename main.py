l = int(input("Введи количество строк: "))
if l == 0:
    print("Количество строк должно быть больше 0.")
    l = int(input("Введи количество строк: "))
while True:
    text = input("Введи сами строки: ")
    words = text.split()
    if len(words) <= l:
        break
    else:
        print(f"Введено больше {l} слов. Еще раз")
new = set(words)
print(text)
print(f"Количество различных слов: {len(new)}")