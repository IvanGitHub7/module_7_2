def custom_write(file_name, strings):
    file = open(file_name, 'w+', encoding = 'utf-8')
    num_str = 0
    strings_positions = {}
    for i in strings:
        byte_str = file.tell()
        file.write(i + ' ' + '\n')
        num_str +=1
        strings_positions [(num_str, byte_str)] = i
    file.close()
    return strings_positions
  

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
  