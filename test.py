import dismantler

# Logo
logo = """
██████╗ ██╗███████╗███╗   ███╗ █████╗ ███╗   ██╗████████╗██╗     ███████╗██████╗ 
██╔══██╗██║██╔════╝████╗ ████║██╔══██╗████╗  ██║╚══██╔══╝██║     ██╔════╝██╔══██╗
██║  ██║██║███████╗██╔████╔██║███████║██╔██╗ ██║   ██║   ██║     █████╗  ██████╔╝
██║  ██║██║╚════██║██║╚██╔╝██║██╔══██║██║╚██╗██║   ██║   ██║     ██╔══╝  ██╔══██╗
██████╔╝██║███████║██║ ╚═╝ ██║██║  ██║██║ ╚████║   ██║   ███████╗███████╗██║  ██║
╚═════╝ ╚═╝╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝╚═╝  ╚═╝
"""

# 1. Simple expr
def simple_expr():
    inp_expr = input("[?] Type one-line Python expression > ")
    print("\n[+] Result: \n")
    print(dismantler.run_from_string(inp_expr).json(indent=1))

# 2. Simple file
def simple_file():
    inp_file_path = input("[?] Type Python code file path > ")
    print("\n[+] Result: \n")
    print(dismantler.run_from_file(inp_file_path).json(indent=1))

# 3. Expression in file
def expr_in_file():
    inp_file_path = input("[?] Type file path which contains only one line > ")
    print("\n[+] Result: \n")
    print(dismantler.run_from_file(inp_file_path, src_type="expr").json(indent=1))

# 4. Suite in str
def suite_in_str():
    inp_expr = input("[?] Type Python code file path > ")

    with open(inp_expr, "r") as f:
        src = f.read()

    print("\n[+] Result: \n")
    print(dismantler.run_from_string(src, src_type='suite').json(indent=1))

# 5. Get tokens
def get_tokens():
    inp_expr = input("[?] Type one-line Python expression > ")
    print("\n[+] Result: \n")
    print(dismantler.run_from_string(inp_expr).tokens())

# 6. Get symbols
def get_symbols():
    inp_expr = input("[?] Type one-line Python expression > ")
    print("\n[+] Result: \n")
    print(dismantler.run_from_string(inp_expr).symbols())


# Test set
MANUAL_TEST_SET = [
    {"name": "Simple expression", "func": simple_expr},
    {"name": "Simple file", "func": simple_file},
    {"name": "Expression in file", "func": expr_in_file},
    {"name": "Suite in string", "func": suite_in_str},
    {"name": "Get tokens from parse tree", "func": get_tokens},
    {"name": "Get symbols from parse tree", "func": get_symbols}
]

# Main
def main():
    while True:
        print("[+] Choose the test (-1 to quit)\n")

        count = 1
        for item in MANUAL_TEST_SET:
            print("[" + str(count) + "] " + item["name"])
            count += 1

        print()

        choice = int(input("[?] > ")) - 1

        if choice < 0:
            return
        
        if choice >= len(MANUAL_TEST_SET):
            print("[!] Unexpected number. Try again.")
            continue

        print()
        choosed_func = MANUAL_TEST_SET[choice]["func"]
        choosed_func()
        print()

if __name__ == "__main__":
    print(logo)
    print("\n[+] Dismantler test & usage script\n")
    main()