def countnum(chuoi):
    num_word= { }
    text_list = chuoi.split()

    for word in text_list:
        word.lower
        word.strip
        if word not in num_word:
            num_word[word] = 1
        else:
            num_word[word] +=1
    return num_word

chuoi = input('Nhập 1 chuỗi bất kì: ')
print(countnum(chuoi))