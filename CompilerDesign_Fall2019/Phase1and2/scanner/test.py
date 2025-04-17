import string

keywords = ["if", "else", "void", "int", "while", "break", "continue", "switch", "default", "case", "return"]
symbols = [";", ":", ",", "[", "]", "(", ")", "{", "}", "+", "-", "*", "=", "<", "=="]
whitespaces = [chr(9), chr(10), chr(11), chr(12), chr(13), chr(32)]

#blank (ASCII 32), \n (ASCII 10), \r (ASCII 13), \t (ASCII 9), \v (ASCII 11), \f (ASCII 12)

alphabet = list(string.ascii_letters)
digit = [str(i) for i in range(10)]

# num, id, keyword, symbol

with open("InputProg1.txt") as f:
    num_of_comments = 0
    isComment = False
    one_line_comment = 0
    line = 1
    tokens = ["1."]
    errors = []
    c = f.read(1)
    buffer = ""
    type1 = []
    flag3 = False
    while c:
        print(buffer, end="##")
        if c == "/":
            # print("COMMENT!" + str(line))
            c1 = f.read(1)
            print(c1)
            flag2 = False
            if c1 == "/":
                # print("ONe_line_COMMENT", line)
                flag2 = True
                k = f.read(1)
                while  k != chr(10):
                    k = f.read(1)
                line += 1
                tokens.append("\n" + str(line) + ".")

            elif c1 == "*":
                # print("MUlTi_line_COMMENT" , line)
                flag2 = True
                c2 = f.read(1)
                flag = False
                while not flag:
                    c3 = c2
                    c2 = f.read(1)
                    if c3 == chr(10):
                        line +=1
                        tokens.append("\n" + str(line) + ".")

                    if c3 == "*" and c2 == "/":
                        flag = True
            elif (c1 != "/") and (c1 != "*"):
                print(c1)
                errors.append(str(line) + ". (" + c + ", invalid input)")
        else:
            if c in symbols or c in whitespaces:
                if len(buffer) > 0:
                    if buffer in symbols:
                        if buffer == "=":
                            flag3 = True
                        tokens.append("(SYMBOL, " + buffer + ")")
                    elif buffer in keywords:
                        tokens.append("(KEYWORD, " + buffer + ")")
                    else:
                        try:
                            a = int(buffer)
                            tokens.append("(NUM, " + buffer + ")")
                        except:
                            tokens.append("(ID, " + buffer + ")")
                buffer = ""
            if c in symbols:
                if c == "=" and flag3:
                    tokens[len(tokens) - 1] = "(SYMBOL, " + "==" + ")"
                    flag3 = False
                else:
                    buffer += c


            elif c in alphabet:
                flag3 = False
                try:
                    a = int(buffer)
                    if len(buffer) > 0:
                        tokens.append("(NUM, " + buffer + ")")
                        buffer = ""
                        buffer += c
                except:
                    if buffer in symbols:
                        tokens.append("(SYMBOL, " + buffer + ")")
                        buffer = ""
                    buffer += c
            elif c in digit:
                flag3 = False
                if buffer in symbols:
                    tokens.append("(SYMBOL, " + buffer + ")")
                    buffer = ""
                buffer += c

            if not (c in alphabet or c in symbols or c in whitespaces or c in digit):
                flag3 = False
                if len(buffer) > 0:
                    errors.append(str(line) + ". (" + buffer + c + ", invalid input)")
                    buffer = ""
                else:
                    errors.append(str(line) + ". (" + c + " , invalid input)")
                    buffer = ""
            if c == chr(10):
                flag3 = False
                line += 1
                tokens.append("\n" + str(line) + ".")
                buffer = ""
                print()

            #print(type(c))

            #print(c)

        c = f.read(1)

        #tokens.append("")
        #errors.append(c)
with open("tokens.txt", "w") as t:
    for index in range(len(tokens) - 1):
        if tokens[index][0] != "(" and index < len(tokens) - 2 and tokens[index + 1][0] != "(":
            pass
        else:
            t.write("{} ".format(tokens[index]))
    t.write("\0")

with open("errors.txt", "w") as t:
    for word in errors:
        t.write("{}\n".format(word))
    t.write("\0")
