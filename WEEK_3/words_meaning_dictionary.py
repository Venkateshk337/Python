word = {
    'Ubiquitous': ['present, appearing, or found everywhere'],
    'Sycophant': ['a person who acts obsequiously towards someone important'],
    'Cacophony': ['harsh mixture of sounds'],
    'Enigma': ['a mystery'],
}


def add_new_entry(dictionary, key, values):
    if key not in dictionary:
        val = [values]
        dictionary[key] = val
    elif values not in dictionary[key]:
        dictionary[key].append(values)
    else:
        print("Word and meaning are present")


def search_meaning(dictionary, meaning):
    if meaning in dictionary:
        print(f"{meaning}:{dictionary[meaning]}")
        return
    flag = 1
    for keys, values in dictionary.items():
        if meaning in values:
            val = values[:] + [keys]
            val.remove(meaning)
            print(f"{meaning}:{val}")
            flag = 0
            break
    if flag:
        print("Meaning not found")


def remove_entry(dictionary, key):
    if key in dictionary:
        print(f"removed entry:{key}:{dictionary[key]}")
        dictionary.pop(key)


def word_sorted(dictionary):
    list1 = list(dictionary.keys())
    list1.sort(key=str.lower)
    dictionary1 = {}
    for i in list1:
        dictionary1.setdefault(i, dictionary[i])
    return dictionary1


add_new_entry(word, 'Hapless', 'unlucky')
add_new_entry(word, 'Enigma', 'something hard to understand')
add_new_entry(word, 'Enigma', 'something hard to understand')
search_meaning(word, 'Enigma')
search_meaning(word, 'unlucky')

remove_entry(word, 'Enigma')

word = word_sorted(word)
print(word)
