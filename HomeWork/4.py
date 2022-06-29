my_srt = input("Введите строку из нескольких слов >>>")

my_str = my_srt.split()
l_numb = 0

for word in my_str:
    l_numb += 1
    print(f"{l_numb} {word[0:10]}")
