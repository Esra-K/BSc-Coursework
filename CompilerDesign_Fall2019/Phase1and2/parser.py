#  LEXER:
import string

keywords = ["if", "else", "void", "int", "while", "break", "continue", "switch", "default", "case", "return"]
symbols = [";", ":", ",", "[", "]", "(", ")", "{", "}", "+", "-", "*", "=", "<", "=="]
whitespaces = [chr(9), chr(10), chr(11), chr(12), chr(13), chr(32)]

with open('InputProg1.txt', 'r') as content_file:
    f = content_file.read()

#blank (ASCII 32), \n (ASCII 10), \r (ASCII 13), \t (ASCII 9), \v (ASCII 11), \f (ASCII 12)

alphabet = list(string.ascii_letters)
digit = [str(i) for i in range(10)]
EOF = "EOF"
# num, id, keyword, symbol
line = 1
index = 0
tokens = ["1."]
errors = []
c = "l"
buffer = ""
flag3 = False
def get_next_token():
    global index
    global f
    global line
    global errors
    global tokens
    num_of_comments = 0
    isComment = False
    one_line_comment = 0
    global c
    global buffer
    type1 = []
    global flag3
    global EOF
    while True:
        print(buffer, end=" ")
        if index >= len(f):
            return EOF
        c = f[index]
        index += 1
        if c == "/":
            # print("COMMENT!" + str(line))
            c1 = f[index]
            index += 1
            print(c1)
            flag2 = False
            if c1 == "/":
                # print("ONe_line_COMMENT", line)
                flag2 = True
                k = f[index]
                index += 1
                while  k != chr(10):
                    k = f[index]
                    index += 1
                line += 1
                tokens.append("\n" + str(line) + ".")

            elif c1 == "*":
                # print("MUlTi_line_COMMENT" , line)
                flag2 = True
                c2 = f[index]
                index += 1
                flag = False
                while not flag:
                    c3 = c2
                    c2 = f[index]
                    index += 1
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
                        h = buffer
                        buffer = ""
                        return h.strip()
                    elif buffer in keywords:
                        tokens.append("(KEYWORD, " + buffer + ")")
                        h = buffer
                        buffer = ""
                        return h.strip()
                    else:
                        try:
                            a = int(buffer)
                            tokens.append("(NUM, " + buffer + ")")
                            buffer = ""
                            return "NUM"
                        except:
                            tokens.append("(ID, " + buffer + ")")
                            buffer = ""
                            return "ID"
                buffer = ""
            if c in symbols:
                if c == "=" and flag3:
                    tokens[len(tokens) - 1] = "(SYMBOL, " + "==" + ")"
                    flag3 = False
                    return "=="
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
                        return "NUM"
                except:
                    if buffer in symbols:
                        tokens.append("(SYMBOL, " + buffer + ")")
                        h = buffer
                        buffer = ""
                        buffer += c
                        return h
                    buffer += c
            elif c in digit:
                flag3 = False
                if buffer in symbols:
                    tokens.append("(SYMBOL, " + buffer + ")")
                    h = buffer
                    buffer = ""
                    buffer += c
                    return h
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






#   PARSER:




from collections import defaultdict

first = defaultdict(list)
follow = defaultdict(list)

first["program"] = ["EOF" , "int" , "void"]
first["declaration-list"] = ["landa", "int", "void"]
first["tmp"] = [";" , "[" , "("]
first["declaration"] = ["int" , "void"]
first["var-declaration"] = [";" , "["]
first["vd"] = ["landa" , "ID"]
first["type-specifier"] = ["int" , "void"]
first["fun-declaration"] = ["("]
first["params"] = ["void" , "int"]
first["param-list"] = ["ID"]
first["pl"] = ["landa" , "ID"]
first["param"] = ["ID"]
first["pr"] = ["landa" , "["]
first["compound-stmt"] = ["{"]
first["statement-list"] = ["landa","ID","+","-","(","NUM","continue","break",";","{","if","while","return","switch"]
first["statement"] = ["{","if","while","return","switch","continue","break",";","ID","+","-","(","NUM"]
first["expression-stmt"] = ["continue","break",";","ID","+","-","(","NUM"]
first["selection-stmt"] = ["if"]
first["iteration-stmt"] = ["while"]
first["return-stmt"] = ["return"]
first["rs"] = [";","ID","+","-","(","NUM"]
first["switch-stmt"] = ["switch"]
first["case-stmts"] = ["landa","case"]
first["case-stmt"] = ["case"]
first["default-stmt"] = ["landa","default"]
first["expression"] = ["ID","+","-","(","NUM"]
first["text"] = ["landa","[","(","+","-"]
first["vr"] = ["landa", "["]
first["context"] = ["=","+","-"]
first["simple-expression"] = ["+","-","(","NUM"]
first["se"] = ["landa","<","=="]
first["relop"] = ["<","=="]
first["addictive-expression"] = ["+","-","(","NUM"]
first["ae"] = ["landa","+","-"]
first["addop"] = ["+","-"]
first["term"] = ["+","-","(","NUM"]
first["tr"] = ["*","landa"]
first["signed-factor"] = ["+","-","(","NUM"]
first["factor"] = ["(","NUM"]
first["args"] = ["landa","ID","+","-","(","NUM"]
first["arg-list"] = ["ID","+","-","(","NUM"]
first["al"] = [",","landa"]
first["id-exp"] = ["(","+","-"]
first["ie"] = ["landa","<","=="]
first["id-addic-exp"] = ["(","+","-"]
first["it"] = ["landa","+","-"]
first["it-term"] = ["(","+","-"]
first["ir"] = ["landa","*"]
first["id-signed-factor"] = ["(","+","-"]
first["none"] = ["+","-"]
first["ne"] = ["<","==","landa"]
first["none-addic-exp"] = ["+","-"]
first["nt"] = ["+","-","landa"]
first["none-term"] = ["+","-"]
first["nm"] = ["landa","*"]
first["none-signed-factor"] = ["+","-"]


follow["program"] = ["$"]
follow["declaration-list"] = ["EOF","{","if","while","return","switch","continue","break","+","-","(","ID","NUM"]
follow["vd"] = [")"]
follow["pl"] = [")"]
follow["pr"] = ["ID",")"]
follow["statement-list"] = ["}"]
follow["case-stmts"] = ["default","}"]
follow["default-stmts"] = ["}"]
follow["vr"] = ["=","+","-"]
follow["se"] = [";",")"]
follow["ae"] = [";",")","<","=="]
follow["tr"] = ["+","-",";",")","<","=="]
follow["args"] = [")"]
follow["al"] = [")"]
follow["text"] = [";",")"]
follow["ie"] = [";",")"]
follow["it"] = ["<","==",";",")"]
follow["ir"] = ["+","-","<","==",":",")"]
follow["ne"] = [";",")"]
follow["nt"] = [";",")","<","=="]
follow["nm"] = ["+","-","<","==",";",")"]


class non_terminal:
    def __init__(self, name="", first=[], follow=[], d={},accept=1000):
        self.name = name
        self.first = first
        self.follow = follow
        self.d = d
        self.accept = accept


d_var_declaration = {0: [("[", 1),(";", 3)], 1: [("NUM", 2)], 2: [("]", 3)]}
d_type_specifier = {0: [("int", 1),("void",1)]}
d_addop = {0: [("+", 1),("-",1)]}
d_relop = {0: [("==", 1),("<",1)]}
addop = non_terminal("addop", first["addop"], [""], d_addop, 1)
d_none_signed_factor = {0: [(addop, 1)]}
none_signed_factor = non_terminal("none-signed-factor", first["none-signed-factor"], [""], d_none_signed_factor, 1)
d_nm = {0: [("*",1),("landa",2)], 1: [(none_signed_factor,0)]}
nm = non_terminal("nm", first["nm"], follow["nm"], d_nm, 2)
d_none_term = {0: [(none_signed_factor,1)], 1: [(nm,2)]}
none_term = non_terminal("none-term", first["none-term"], [""], d_none_term, 2)
d_nt = {0: [(addop,1),("landa",2)], 1: [(none_term,0)]}
nt = non_terminal("nt", first["nt"], follow["nt"], d_nt, 2)

d_none_addic_exp = {0: [(none_term,1)], 1:[(nt,2)]}
relop = non_terminal("relop", first["relop"], [""], d_relop, 1)
none_addic_exp = non_terminal("none-addic-exp", first["none-addic-exp"], [""], d_none_addic_exp, 2)
d_ne = {0: [(relop,1),("landa",2)], 1:[(none_addic_exp,2)]}
ne = non_terminal("ne", first["ne"], follow["ne"], d_ne, 2)
d_factor = {0: [("(",1),("NUM",3)], 1: [(expression,2)], 2: [(")",3)]}
factor = non_terminal("factor", first["factor"], [""], d_factor, 3)
d_signed_factor = {0: [("+",1),("-",2),(factor,3)], 1: [(factor,3)], 2: [(factor,3)]}

signed_factor = non_terminal("signed-factor", first["signed-factor"], [""], d_signed_factor, 3)
d_tr = {0: [("*",1),("landa",2)], 1: [(signed_factor,0)]}
tr = non_terminal("tr", first["tr"], follow["tr"], d_tr, 2)

d_term = {0: [(signed_factor,1)], 1: [(tr,2)]}

term = non_terminal("term", first["term"], [""], d_term, 2)
d_ae = {0: [(addop,1),("landa",2)], 1: [(term,0)]}
ae = non_terminal("ae", first["ae"], follow["ae"], d_ae, 2)
d_addictive_expression = {0: [(term,1)], 1: [(ae,2)]}

addictive_expression = non_terminal("addictive-expression", first["addictive-expression"], [""], d_addictive_expression, 2)

d_simple_expression = {0: [(addictive_expression,1)], 1: [(se,2)]}

simple_expression = non_terminal("simple-expression", first["simple-expression"], [""], d_simple_expression, 2)

d_context = {0: [("=",1),(none,2)], 1: [(expression,2)]}
d_vr = {0: [("[",1),("landa",3)], 1: [(expression,2)], 2:[("]",3)]}
vr = non_terminal("vr", first["vr"], follow["vr"], d_vr, 3)
context = non_terminal("context", first["context"], [""], d_context, 2)
d_id_addic_exp = {0: [(id_term,1)], 1: [(it,2)]}
id_addic_exp = non_terminal("id-addic-exp", first["id-addic-exp"], [""], d_id_addic_exp, 2)
d_ie = {0: [(relop,1),("landa",2)], 1: [(id_addic_exp,2)]}
d_id_exp = {0: [(id_addic_exp,1)], 1: [(ie,2)]}
id_exp = non_terminal("id-exp", first["id-exp"], [""], d_id_exp, 2)
d_text = {0: [(vr,1),(id_exp,2)], 1: [(context,2)]}
text = non_terminal("text", first["text"], follow["text"], d_text, 2)


d_expression = {0: [("ID",1),(simple_expression,2)], 1: [(text,2)]}
expression = non_terminal("expression", first["expression"], [""], d_expression, 2)






d_none = {0: [(none_addic_exp,1)], 1: [(ne,2)]}
d_arg_list = {0: [expression,1], 1: [(al,2)]}
arg_list = non_terminal("arg-list", first["arg-list"], [""], d_arg_list, 2)
d_args = {0: [(arg_list,1),("landa",1)]}
args = non_terminal("args", first["args"], follow["args"], d_args, 1)


d_id_signed_factor = {0: [("(",1),("+",2),("-",3)], 1: [(args,4)], 2:[("(",5)], 3:[("(",6)], 4: [(")",9)], 5: [(args,7)], 6: [(args,8)], 7: [(")",9)], 8:[(")",9)]}
d_ir = {0: [("*",1),("landa",2)], 1: [(id_signed_factor,0)]}
d_it_term = {0: [id_signed_factor,1], 1: [(ir,2)]}
d_it = {0: [(addop,1),("landa",2)], 1: [(id_term,0)]}
d_al = {0: [(",",1),("landa",2)], 1: [(expression,0)]}


d_se = {0: [(relop,1),("landa",2)], 1: [(addictive_expression,2)] }
d_default_stmt = {0: [("default",1),("landa",3)], 1: [(":",2)], 2: [(statement_list,3)]}
d_case_stmt = {0: [("case", 1)], 1: [("NUM",2)], 2: [(":",3)], 3: [(statement_list,4)]}
d_case_stmts = {0: [(case_stmt,0),("landa",1)]}
d_switch_stmt = {0: [("switch",1)], 1: [("(",2)], 2: [(expression,3)], 3: [(")",4)], 4: [("{",5)], 5: [(case_stmts,6)], 6: [(default_stmt,7)], 7: [("}",8)]}
d_rs = {0: [(expression,1),(";",2)], 1: [(";",2)] }
d_return_stmt = {0: [("return",1)], 1: [(rs,2)]}
d_iteration_stmt = {0: [("while",1)], 1:[("(",2)], 2: [(expression,3)], 3: [(")",4)], 4: [(statement,5)]}
d_selection_stmt = {0: [("if",1)], 1: [("(",2)], 2: [(expression,3)], 3: [(")",4)], 4: [(statement,5)], 5: [("else",6)], 6: [(statement,7)] }
d_expression_stmt = {0: [(expression,1),("continue",2),("break",3),(";",4)], 1: [(";",4)], 2: [(";",4)], 3: [(";",4)]}
d_statement = {0: [(expression_stmt,1),(compound_stmt,1),(selection_stmt,1),(iteration_stmt,1),(return_stmt,1),(switch_stmt,1)]}
d_statement_list = {0: [(statement,0),("landa",1)]}
d_compound_stmt = {0: [("{",1)], 1: [(declaration_list,2)], 2: [(statement_list,3)], 3: [("}",4)]}
d_pr = {0: [("[",1),("landa",2)], 1: [("]",2)]}
d_param = {0: [("ID",1)], 1: [(pr,2)]}
d_pl = {0: [(param,0),("landa",1)]}
d_param_list = {0: [(param,1)], 1: [(pl,2)]}
d_vd = {0: [(param_list,1),("landa",1)]}
d_params = {0: [("void",1),("int",2)], 1: [(vd,3)], 2: [(param_list,3)]}
params = non_terminal("params", first["params"], [""], d_params,3)
compound_stmt = non_terminal("compound-stmt", first["compound-stmt"], [""], d_compound_stmt, 4)

d_fun_declaration = {0: [("(",1)], 1: [(params,2)], 2: [(")",3)], 3: [(compound_stmt,4)]}
var_declaration = non_terminal("var-declaration", first["var-declaration"], [""], d_var_declaration, 3)
fun_declaration = non_terminal("fun-declaration", first["fun-declaration"], [""], d_fun_declaration, 4)
d_tmp = {0: [(var_declaration,1),(fun_declaration,1)]}
tmp = non_terminal("tmp", first["tmp"], [""], d_tmp, 1)
type_specifier = non_terminal("type-specifier", first["type-specifier"], [""], d_type_specifier, 1)
d_declaration = {0: [(type_specifier,1)], 1: [("ID",2)], 2: [(tmp,3)]}
declaration = non_terminal("declaration", first["declaration"], [""], d_declaration, 3)
d_declaration_list = {0: [(declaration,0),("landa",1)]}

declaration_list = non_terminal("declaration-list", first["declaration-list"], follow["declaration-list"], d_declaration_list, 1)
d_program = {0: [(declaration_list,1)], 1: [("EOF",2)]}




program = non_terminal("program", first["program"], follow["program"], d_program ,2)
vd = non_terminal("vd", first["vd"], follow["vd"], d_vd, 1)
param_list = non_terminal("param-list", first["param-list"], [""], d_param_list, 2)
pl = non_terminal("pl", first["pl"], follow["pl"], d_pl, 1)
param = non_terminal("param", first["param"], [""], d_param, 2)
pr = non_terminal("pr", first["pr"], follow["pr"], d_pr, 2)
statement_list = non_terminal("statement-list", first["statement-list"], follow["statement-list"], d_statement_list, 1)
statement = non_terminal("statement", first["statement"], [""], d_statement, 1)
expression_stmt = non_terminal("expression-stmt", first["expression-stmt"], [""], d_expression_stmt, 4)
selection_stmt = non_terminal("selection-stmt", first["selection-stmt"], [""], d_selection_stmt, 7)
iteration_stmt = non_terminal("iteration-stmt", first["iteration-stmt"], [""], d_iteration_stmt, 5)
return_stmt = non_terminal("return-stmt", first["return-stmt"], [""], d_return_stmt, 2)
rs = non_terminal("rs", first["rs"], [""], d_rs, 2)
switch_stmt = non_terminal("switch-stmt", first["switch-stmt"], [""], d_switch_stmt, 8)
case_stmts = non_terminal("case-stmts", first["case-stmts"], follow["case-stmts"], d_case_stmts, 1)
case_stmt = non_terminal("case-stmt", first["case-stmt"], [""], d_case_stmt, 4)
default_stmt = non_terminal("default-stmt", first["default-stmt"], follow["default-stmts"], d_default_stmt, 3)

se = non_terminal("se", first["se"], follow["se"], d_se, 2)


al = non_terminal("al", first["al"], follow["al"], d_al, 2)

ie = non_terminal("ie", first["ie"], follow["ie"], d_ie, 2)
it = non_terminal("it", first["it"], follow["it"], d_it, 2)
it_term = non_terminal("it-term", first["it-term"], [""], d_it_term, 2)
ir = non_terminal("ir", first["ir"], follow["ir"], d_ir, 2)
id_signed_factor = non_terminal("id-signed-factor", first["id-signed-factor"], [], d_id_signed_factor, 9)
none = non_terminal("none", first["none"], [""], d_none, 2)





epsilon = "landa"
ts = []
nts = []
tree = []
stack = []
parse_arr = ""
def parse(non_T, tree_indent):
    global parse_arr
    global a
    global line
    state = 0
    while state != non_T.accept and not (a == EOF and non_T.d[state][0][0] != "EOF"):
        if state == 0:
            for edge in non_T.d[state]:
                label = edge[0]
                if label in ts and a == label:
                    state = edge[1]
                    print("|\t"*(tree_indent - 1) + a)
                    parse_arr += "|\t"*(tree_indent - 1) + a + "\n"
                    a = get_next_token()
                    break
                elif label in nts and (a in label.first or (epsilon in label.first and a in label.follow)):
                    print("|\t" * (tree_indent - 1) + label.name)
                    parse_arr += "|\t" * (tree_indent - 1) + label.name + "\n"
                    if parse(label, tree_indent + 1):
                        state = edge[1]
                    else:
                        return False
                    break
                elif label == epsilon and a in label.follow:
                    state = edge[1]
                    break
        else:
            next = non_T.d[state][0]
            if next[0] in ts:
                if next[0] == EOF and not a == EOF:
                    print("#" + line + " : Syntax Error! Malformed Input")
                    return False
                else:
                    if not a == next[0]:
                        print("#" + str(line) + " : Syntax Error! Missing " + next[0])
                    state = next[1]
                    print("|\t" * (tree_indent - 1) + a)
                    parse_arr += "|\t" * (tree_indent - 1) + a + "\n"
                    a = get_next_token()
            elif next[0] in nts:
                if not a in next[0].first and (not epsilon in next[0].first):
                    while not a in next[0].first and (not epsilon in next[0].first):
                        if a in next[0].follow:
                            print("#" + str(line) + " : Syntax Error! Missing " + non_T.name)
                            break
                        else:
                            print("#" + str(line) + " : Syntax Error! Unexpected " + a)
                            a = get_next_token()
                print("|\t" * (tree_indent - 1) + next[0].name)
                parse_arr += "|\t" * (tree_indent - 1) + next[0].name + "\n"
                if parse(next[0], tree_indent + 1):
                    state = next[1]
                else:
                    return False
                break
            else:
                print("impossible is nothing :D")
    if a == EOF and not non_T.d[state][0][0] == EOF:
        print("#" + str(line) + " : Syntax Error! Unexpected EndOfFile")
        return False
    return True





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
