alphabet = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':1,'M':3,'N':1,'O':3,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}

items = alphabet.items()
again = ''

while again != 'N':
    wordEntry = input('Word: ').upper()


    def pointsCounter(word):
        points = 0
        for i in range(len(word)):
            if word[i].isalpha():
                points = points + alphabet[word[i]]
        return points

    total = pointsCounter(wordEntry)

    print('The word is worth {} points'.format(total))

    again = input('Type ENTER to continue, N to quit : ').upper()

