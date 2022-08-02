from textblob import TextBlob

def Convert(string):
    li = list(string.split())
    return li
str = input('enter text to check')

words = Convert(str)
corrected_words = []

for i in words:
    corrected_words.append(TextBlob(i))

print('Wrong words: ', words)
print('Correct words: ')
for i in corrected_words:
    print(i.correct(), end=' ')
