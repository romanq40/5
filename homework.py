from random import choice

WORDS = ("python", "игра", "программирование")  

word = choice(WORDS)  
text  = "_" * len(word)  
wrong = 0  

while wrong < 3 and text != word:
    print(text)
    guess = input("\n\nВведите свое предположение: ")    
    
    
    if guess in word:  
        print("\nДа!", guess, "есть в слове!")
        new_text = ""
        for i in range(len(word)):  
            if guess == word[i]:
                new_text += guess
            else:
                new_text += text [i]
        text  = new_text

    else:
        print(  guess + " нет в слове.")  
        wrong += 1

if wrong == 3:  
    print("Вы проиграли")
else:  
    print("\nВы угадали слово!")

print("\nЗагаданное слово было \"" + word + '\"')