def reverse_words_order_and_swap_cases(sentence):
    
    a=sentence.swapcase()
    words=a.split(' ')
    words = list(reversed(words))
    return ' '.join(words) 
    
    
print(reverse_words_order_and_swap_cases('Coding Is aWsome'))
