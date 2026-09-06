import sys
import os
import lexer
import err_triage

def main():
    if len(sys.argv) != 2:
        err_triage.tof("CLI001", "SEM", 0, "usage: loom.py <file_name.lm>")
        exit()
    file_name = sys.argv[1]
    if os.path.exists(file_name):
        ext = os.path.splitext(file_name)[1]
        if ext == ".frn":
            tokens = lexer.lex(file_name)
            print(tokens)
        else:
            file_name = file_name.replace(ext, f"{ext}")
            err_triage.tof("CLI003", "SEM", 1, [f"given: {file_name}", "expected: files ending in .lm"])
    else:
        err_triage.tof("CLI002", "SEM", 0, f"given: {file_name}")

main()
