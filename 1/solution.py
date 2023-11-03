def solution(s):
    length = len(s)
    
    for i in range(1, length):
        substring = s[:i]
        times = length // i
        if substring * times == s:
            return times

    return 1

#Test
print(solution("abccbaabccba"))        # Output: 2
print(solution("abcabcabcabc"))        # Output: 4
print(solution("memekimemeki"))        # Output: 2
print(solution("asukontolasukontol"))  # Output: 2
print(solution("abababababab"))        # Output: 6
print(solution("zaza"))