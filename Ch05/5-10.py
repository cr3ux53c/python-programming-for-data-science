def return_sentence(sentence, n):
    sentence += str(n)
    n -= 1
    if n < 0:
        return sentence
    else:
        return(return_sentence(sentence, n))

sentence = "I Love You"
print(return_sentence(sentence, 5))
