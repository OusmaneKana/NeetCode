s = "Was it a car or a cat I saw"


def is_alpha_num(c):

    return (
        ord("Z")>=ord(c)>=ord("A") or
        ord("z")>=ord(c)>=ord("a") or
        ord("9")>=ord(c)>=ord("0")
    )


l, r = 0, len(s) -1

while True:
    while l < r and not is_alpha_num(s[l]):
        l+=1
    while r > l and not is_alpha_num(s[r]):
        r-=1
    
    if s[l].lower() != s[r].lower():
        print(False)
        break
