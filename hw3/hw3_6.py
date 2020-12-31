data = 'dkufhkd kdrgh djhgk kzdhfk'
out_data = ''

def int_func(text):
    return(text.capitalize())

words_list = data.split()
for word in words_list:
    out_data += int_func(word) + ' '

print(out_data)





