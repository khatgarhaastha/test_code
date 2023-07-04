def mergeStringAlt(word1, word2):
    merged = ""
    
    if len(word1) == len(word2):
        for i in range(len(word1)):
            merged += word1[i] + word2[i]
        
    
    if len(word2) > len(word1):
        for i in range(len(word1)):
            merged += word1[i] + word2[i]    
        merged += word2[len(word1) : ]
        
    
    if len(word1) > len(word2):
        for i in range(len(word2)):
            merged += word1[i] + word2[i]
        merged += word1[len(word2) : ]
    
    return merged

word1 = str(input("enter the first sting: "))
word2 = str(input("enter the second string: "))

print(f"the merged string is: {mergeStringAlt(word1, word2)}")