def order_words(words):
    return sorted(words, key=lambda x: (len(x), x))

length = int(input())
words = list(set([str(input()) for _ in range(length)]))

for i in order_words(words):
    print(i)
