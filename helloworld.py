'''test for hello world'''
def print_text (word,times):
    for _ in range(times) :
        print(word)
print_text(str(input()),int(input()))
