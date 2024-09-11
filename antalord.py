def count_words():
    sentence = input("say something: ")
   
    text = sentence.split()
    
    return len(text)

print("amount of words in your text :", count_words())