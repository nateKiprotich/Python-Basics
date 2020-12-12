def fact(n):

    if n == 0:
        return 1

    return n*fact(n-1)


x = fact(0)
print(x)


# Loop through entire text character by character
def loop_text(txt, i):

    if(i == len(txt)):
        return

    print(txt[i])
    loop_text(txt, i+1)


loop_text("Hey nate. Are you doormaker ?", 0)
