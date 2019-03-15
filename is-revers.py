def is_revers(word1, word2):
    lnw1 = len(word1)
    lnw2 = len(word2)
    i = 0
    if lnw1 != lnw2:
        return False
    while lnw2 > 0:
        if word2[lnw2 - 1] != word1[i]:
            return False
        lnw2 = lnw2-1
        i = i+1
    return True


print(is_revers("reza", "azer"))
print(is_revers("rezaei", "azxer"))
