import wikipedia


def article(title):
    result = wikipedia.summary(title)
    print(result)
    return result


def write(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(data)


wikipedia.set_lang('en')
# apple =  article('apple company')
# write('apple.txt',apple)

# apple =  article('Tesla')
# write('tesla.txt',tesla)

# words_company = ['Tesla Inc', 'Apple Inc', 'Google Inc', 'Microsoft Inc']
with open('search-word.txt','r', encoding='utf-8') as file:
    lines = file.readlines()
    
words_company = []
for l in lines:
    words_company.append(l.strip())
    
print(words_company)


for w in words_company:
    try:
        data = article(w)
        write('{}.txt'.format(w), data)
    except:
        print(w, 'Error')
