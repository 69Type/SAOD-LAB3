




#Алгоритм Кнута-Морриса-Пратта
def search(string, word):
    def prefix(string):
        array = [0] * len(string)
        for i in range(1, len(string)):
            k = array[i - 1]
            while k > 0 and string[k] != string[i]:
                k = array[k - 1]
            if string[k] == string[i]:
                k += 1
            array[i] = k
        return array
    array = []
    k = 0
    p = prefix(string)
    for i in range(len(string)):
        while k > 0 and string[i] != word[k]:
            k = p[k - 1]
        if string[i] == word[k]:
            k += 1
        if k == len(word):
            array.append((i - len(word) + 1, i + 1))
            k = p[k - 1]
    return array


#Алгоритм Бойера-Мура
def search2(string, word):
    def preprocess(w):
        array = [len(w)] * 256
        for i in range(len(w) - 1):
            array[ord(w[i])] = len(w) - 1 - i
        return array

    array = []
    T = preprocess(word)
    skip = 0
    while len(string) - skip >= len(word):
        if string[skip:skip + len(word)] == word:
            array.append((skip, skip + len(word)))
        skip += T[ord(string[skip + len(word) - 1])]
    return array


# Функция подсчёта времени
def count_time(func, count, accuracy, *args):
    import time
    t = 0
    for i in range(accuracy):
        start = time.time()

        for k in range(count): func(*args)

        t += time.time() - start
    return t / accuracy

# нативный поиск
def native_search(string, word):
    return string.find(word)

def randomword(length):
    import random, string
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

text = randomword(10000)
short_word = text[5000:5009]
long_word = text[5000:6000]


print("Алгоритм Кнута-Морриса-Пратта: ", count_time(search, 100, 1, text, short_word))
print("Алгоритм Кнута-Морриса-Пратта: ", count_time(search, 100, 1, text, long_word))

print("Алгоритм Бойера-Мура: ", count_time(search2, 100, 1, text, short_word))
print("Алгоритм Бойера-Мура: ", count_time(search2, 100, 1, text, long_word))

print("нативный поиск: ", count_time(native_search, 100, 1, text, short_word))
print("нативный поиск: ", count_time(native_search, 100, 1, text, long_word))