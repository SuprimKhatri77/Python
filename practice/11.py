def count_word_occurence(str):
    words = str.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
str = "hello world hello python"
word_count = count_word_occurence("hello world hello python")
print(word_count)
