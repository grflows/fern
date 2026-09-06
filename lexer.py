from syntax import *
from cng import * # context and grammar
import err_triage

lexer_errs = []

def lex(file_name):
    tokens = []
    line_number = 0
    start_of_line = True
    with open(file_name) as f:
        source = f.read().split("\n")
        
    for line in source:
        scope_context = SCPCNX_NONE
        line_context = 0 
        line = line.strip()
        line_number += 1
        fchar = line[0] if line != "" else "empty"
        if start_of_line:
            if fchar == "|":
                line_context = LNCNX_PIPE
            elif fchar == "?":
                scope_context = SCPCNX_EVAL
                line_context = LNCNX_TYPECHECK
                if ">>" not in line:
                    print(f"line[{line_number}]:", "use '>>' to pipe eval")
            elif fchar == "#":
                line_context = LNCNX_DEFIMPRT
                line = line.split(" ")

                if (line[0] == "#import") and (len(line) != 1): 
                    tokens.append([scope_context, line_context, DIR_IMPORT, line[1:]])
                    continue
                else:
                    print(f"line[{line_number}]:", "improper #import use", line)
                    continue
            elif fchar == "@":
                pass
            elif fchar == "/":
                continue
            # ===================== words ==========================
            elif 'a' <= fchar <= 'z':
                line = line.split(" ")
                fword = line[0]
                pass
            # invalids
            elif '0' <= fchar <= '9':
                lexer_errs.append(("GRM001", "SEM", 1, [f"line[{line_number}]: expected line to start with a reserved keyword or symbol", f"{line}"]))
            else :
                lexer_errs.append(("GRM001", "SEM", 1, [f"line[{line_number}]: expected line to start with a reserved keyword or symbol", f"{line}"]))
               
        tokens.append([scope_context, line_context])
    if lexer_errs == []:
        return [] #tokens
    else:
        print(f"Exited with {len(lexer_errs)} errors(s)")
        for err in lexer_errs:
            err_triage.tof(err[0], err[1], err[2], err[3])
        exit()
