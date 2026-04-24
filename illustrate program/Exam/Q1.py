# You have two strings: s1 and s2. You need to build a new string s3 such that: Take the first character
# of s1, then the last character of s2. Then the second character of s1, then the second-last character of s2.
# Continue this pattern until one string runs out. Any leftover characters from the longer string should be 
# appended at the end.
def mix_strings(s1, s2):
    result = []
    min_len = min(len(s1), len(s2))
    
    for i in range(min_len):
        result.append(s1[i])
        result.append(s2[-(i+1)])
    
    # leftover
    result.append(s1[min_len:])
    result.append(s2[:len(s2)-min_len])
    
    return "".join(result)

print(mix_strings("HELLO", "WORLD"))