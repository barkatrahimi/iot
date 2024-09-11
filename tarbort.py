def ta_bort_vokaler(text):
    vokaler = "aeiouåäöAEIOUÅÄÖ"  
    # din kod här
    n_text = ""  
    
    for tecken in text:  
        if tecken not in vokaler:  
            n_text += tecken
    
    return n_text 

user_input = input("Skriv en text: ")

print("Texten utan vokaler: {}".format (ta_bort_vokaler(user_input)))