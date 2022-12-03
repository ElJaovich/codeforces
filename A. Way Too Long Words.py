def word_abbreviations(n):
    i = 1
    for i in range(int(n)):
        word = input()
        if(len(list(word)) > 10 ):
            count = 0
            for letter in list(word)[1:-1]:
                count += 1
            print(word[0] + str(count) + word[-1])
        else:
            print(word)
word_abbreviations(input())