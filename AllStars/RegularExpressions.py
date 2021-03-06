def main():
    with open("RegularExpressions.txt") as f:
        myInput = [line.rstrip() for line in f]
        for i in range(len(myInput)):
            currInput = myInput[i].split(", ")
            print(match(currInput[0], currInput[1]))

# split regex into sections eg ['0', '1', '1', '0*', '(01)*']
# try to match first regex to first text
# if not match, return false
# if repeat, find the longest match possible, then recur using that match, then smaller matches (including 0) using a for loop
# if match cut off first regex + matching text and call same method
# when complete, return the array of text matches

# can handle Kleene star, no parentheses
def match(regex, text):
    # longest substring of the text that can be matched
    matched = ""
    regIndex = 0
    textIndex = 0
    done = False
    while regIndex < len(regex):
        if textIndex > len(text) - 1:
            break
        repeat = False
        if regIndex < len(regex) - 1:
            if regex[regIndex + 1] == "*":
                repeat = True
        print("Curr regex: " + str(regex[regIndex]))
        print("Repeat: " + str(repeat))
        if repeat:
            while textIndex < len(text):
                print("Parameter 1: " + str(regex[regIndex:regIndex + 1]))
                print("Parameter 2: " + str(text[textIndex:]))
                result = match(regex[regIndex:regIndex + 1], text[textIndex:])
                print("Result of repeat: " + str(result))
                if result == "YES" or result > 0:
                    try:
                        textIndex += match(regex[regIndex:regIndex + 1], text[textIndex:])
                        matched += regex[regIndex:regIndex + 1]
                    except:
                        textIndex = len(text)
                        matched = text
                else:
                    break
            print("Text Index after repeating: " + str(textIndex))
            regIndex += 2
        if textIndex < len(text) and regIndex < len(regex):
            if regex[regIndex] == text[textIndex]:
                matched += regex[regIndex]
                textIndex += 1
                if regIndex == len(regex) - 1:
                    done = True
                else:
                    regIndex += 1
            else:
                break

    if matched == text and done:
        return "YES"
    else:
        return textIndex
    return [regex, text]
main()

# import re

# def main():
#     number = 1
#     with open("RegularExpressions.txt") as f:
#         myInput = [line.rstrip() for line in f]
#         for i in range(len(myInput)):
#             currInput = myInput[i].split(", ")
#             # print("Pattern: " + currInput[0])
#             pattern = list(currInput[0])
#             finished = False
#             while not finished:
#                 finished = True
#                 for j in range(len(pattern)):
#                     if pattern[j] == " ":
#                         del pattern[j]
#                         finished = False
#                         break
#                     elif pattern[j] == "U":
#                         pattern[j] = "|"
#             currInput[0] = "".join(pattern)
#             s = re.compile(currInput[0])
#             # print("String: " + currInput[1])
#             m = s.match(currInput[1])
#             # print(m)
#             if m != None and m.group() == currInput[1]:
#                 print(str(number) + ". Yes")
#                 number += 1
#             else:
#                 if m != None and m.start() == 0:
#                     print(str(number) + ". No, ", end = "")
#                     number += 1
#                     temp = currInput[0][:-1]
#                     index = []
#                     index.append(m.end())
#                     while len(temp) > 0:
#                         try:
#                             s = re.compile(temp)
#                             m = s.match(currInput[1])
#                             if m != None and m.start() == 0:
#                                 index.append(m.end())
#                             temp = temp[:-1]
#                         except:
#                             temp = temp[:-1]
#                     s = re.compile(currInput[0])
#                     print(s)
#                     m = s.match(currInput[1])
#                     temp = currInput[1][:-1]
#                     while len(temp) > 0:
#                         m = s.match(temp)
#                         if m != None and m.start() == 0:
#                             print(m)
#                             index.append(m.end())
#                         temp = temp[:-1]
#                     print(max(index))
#                 else:
#                     print(str(number) + ". No, ", end = "")
#                     number += 1
#                     temp = currInput[0][:-1]
#                     index = []
#                     while len(temp) > 0:
#                         s = re.compile(temp)
#                         m = s.match(currInput[1])
#                         if m != None and m.start() == 0:
#                             index.append(m.end())
#                         temp = temp[:-1]
#                     s = re.compile(currInput[0])
#                     m = s.match(currInput[1])
#                     temp = currInput[1][:-1]
#                     while len(temp) > 0:
#                         m = s.match(temp)
#                         if m != None and m.start() == 0:
#                             index.append(m.end())
#                         temp = temp[:-1]
#                     print(max(index))
#             # may need to cut down regular expression to find max number of characters that can be generated
#             # s = re.compile("(01)*|(1*0)")
#             # m = s.match("10")



# main()

# Works
# s = re.compile("1(1|0)*")
# m = s.match("10100000111")

# Does not work
# s = re.compile("(01)*|(1*0)") # doesn't match second condition
# m = s.match("11110")

# https://docs.python.org/3.5/howto/regex.html

# Sample Input
# 1*110*, 10110
# (10)*1*, 1010100
# (01)*U(1*0), 0101110

# Test Input
# 10*1, 101
# 1*0*, 110001
# (0*101*)*, 0010110101
# 11*10*, 110110
# 0*1, 0000011
# 1*0*1, 1110001001
# (1*0)*0, 1111001100
# (010*)*, 0101000110001 # incorrect end index
# (01*) U (0*1), 10110 # how the hell is this one actually right?
# ((00*1) U (101) U1*)*, 1010111111111010 # how the hell is THIS one actually right??????
