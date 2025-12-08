sentence = "python is great and python is simple"
split_sentence = sentence.split(' ')

result = {}
for i in split_sentence:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1
print(result)