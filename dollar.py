word=input("enter a word:")
if word:
    first_char = word[0]
    modified = first_char + word[1:] .replace(first_char,'$')
    print("modified string:",modified)
else:
        print("no repitation of word")
