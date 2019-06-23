def week_seven(sentence1):
    cells = set(sentence1.replace(' ','').lower())
    return cells
sentence_a = "The quick brown fox jumps over the lazy dog"
sentence_b = "I love you"
print(len(week_seven(sentence_a)-week_seven(sentence_b)))
