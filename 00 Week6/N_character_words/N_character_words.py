# number of n words in a string
def N_character_words(string,N):
    words = string.split()
    number_of_n_words = 0
    for this_word in words:
        #print("this word is: ", this_word,len(this_word))
        if len(this_word) == N:
            #print("found one: ",this_word)
            number_of_n_words = number_of_n_words + 1
    return number_of_n_words

# driver code test for this function
string = input("what is your string? ")
for N in range(10):
    result = N_character_words(string,N)
    print("i found ",result, "words that have",N,"characters")