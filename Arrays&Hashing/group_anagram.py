from collections import defaultdict
strs = ["act","pots","tops","cat","stop","hat"]

res = defaultdict(list)
char_hash = [0] * 26

for word in strs:
    char_hash = [0] * 26
    for letter in word:
        char_hash[ord(letter) - ord('a')] +=1

    res[tuple(char_hash)].append(word)
    

print(list(res.values()))
