"fun with recursion "

letter_s = []

def letter_score(letter):
    """ your docstring goes here """
    assert(len(letter) == 1)
    if 'a'<=letter<='z':
        if letter =='a' or letter == 'o' or letter == 'i' or letter == 'l' or letter== 'e' or letter == 's'or letter== 't' or letter == 'r'or letter == 'u' or letter =='l' or letter =='n':
            return 1
        elif letter =='d' or letter == 'g':
            return 2
        elif letter =='b' or letter == 'c' or letter =='m' or letter == 'p':
            return 3
        elif letter =='h' or letter == 'w' or letter =='y':
            return 4
        elif letter =='k':
            return 5
        elif letter =='b' or letter =='x':
            return 8
        elif letter =='z' or letter =='q':
            return 10
        else:
            return 0
        

def scrabble_score(word):
    
    if word =="":
        return 0
    else:
        rest_word = scrabble_score(word[1:])
        num = letter_score(word[0])
        rest_word += num
        return rest_word

print(scrabble_score('python'))



def index(elem, seq):
    if  seq=="" or seq==[]:
        return 0
    else:
        rest = index(elem, seq[1:])
        if elem ==seq[0]:
            return rest-1
        else:
            return rest + 1
        


print(index("we", ['well','wm','23','we', 112 ]))

def test():
    test1=index('b', 'banana')
    print("the test1 test returns", text1)
    
