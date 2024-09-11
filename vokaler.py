def rakna_vokaler(text):
    vokaler = "aeiouåäöAEIOUÅÄÖ"  
    antal_vokaler = 0  
    
    for tecken in text: 
        if tecken in vokaler:  
            antal_vokaler += 1 
    
    return antal_vokaler  

user_input = input("Skriv en text: ")

print("Antal vokaler i texten: {}".format(rakna_vokaler(user_input)))
