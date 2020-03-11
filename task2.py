def shortestWord():
    string_before = list(input(' :'))
    string_before.sort(key=len)
    string_before.reverse()
    string_after = ''.join(string_before)
    print(str(string_after))
shortestWord()