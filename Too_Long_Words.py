test_cases=int(input())
for i in range(test_cases):
    inp_word=input()
    if not len(inp_word)>10:
        print(inp_word)
    else:
        print(inp_word[0]+str(len(inp_word)-2)+inp_word[-1])
