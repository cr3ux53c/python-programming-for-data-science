sentence = list("Hello Gachon")
while (len(sentence) + 1):
    try:
        print(sentence.pop(0))
    except Exception as e:
        print(e)
        break
