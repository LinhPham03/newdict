dictionary = {
    "sad" : "buồn",
    "spring" : "mùa xuân",
    "summer": "mùa hạ",
    "autumn": "mùa thu",
    "winter": "mùa đông"
}
def translate(word):
    for word in dictionary:
        if word == input_word:
            return dictionary[word]

            
input_word = input('Nhập từ cần dịch: ')
translated_word = translate(input_word)
if translated_word:
    print(input_word, ' : ', translated_word)
else:
    print(input_word, "doesn't exist")