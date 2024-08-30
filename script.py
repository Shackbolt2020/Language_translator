from translate import Translator
def file():
    with open('/Users/{your_username_here}/Desktop/test.txt', mode='r') as my_file:
        return str(my_file.readline())

translator= Translator(to_lang="es")
translation = translator.translate(file())
print(translation)

with open('/Users/{your_username_here}/Desktop/test_translate.txt', mode='w') as my_file2:
    my_file2.write(translation)