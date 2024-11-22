def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for word in other_words:
        if root_word in word.lower() or word.lower() in root_word:
            same_words.append(word)
    return same_words


print(single_root_words('Чай', 'чайНИк', 'чАЙка', 'круЖка', 'поНчиК'))
print(single_root_words('КаБалА', 'бАл', 'арБАлет', 'картОн', 'КАБ'))