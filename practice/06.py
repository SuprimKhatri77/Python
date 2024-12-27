def vowel_count(str):
    vowel = "aeiouAEIOU"
    count = 0
    for i in str :
        if i in vowel:
            print(i)
            count += 1
            print(count)

vowel_count("slash")