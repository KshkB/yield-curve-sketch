import return_ylds, df_parse
import os, sys

def ylds(*args):
    "pass year-month or year, e.g., 202201 or 2022"
    param = ''.join(map(str, args))
    if len(args) == 4 or len(args) == 6:

        if len(args) == 4:
            df = return_ylds.return_yields_yr(param)
            return df_parse.parse_df(df)

        if len(args) == 6:
            df = return_ylds.return_yields_month(param)
            return df_parse.parse_df(df)
    else:
        print("Invalid input")
        return

def curr_ylds():

    df = return_ylds.return_yields_latest()
    return df_parse.parse_curr(df)

def input_menu_historical():

    print(
        "Enter year-then-month or year, e.g., '202201' for year 2022, Jan or '2022' for year 2022.\n"
    )

    inpt = int(input().strip())
    return inpt

def input_menu():

    print(
        "Choose one:\n"
        "[1] Get historical yield graph.\n"
        "[2] Current bond yield curve.\n"
        "[3] Exit.\n"
    )

    inpt = int(input().strip())
    if inpt == 1:
        return input_menu_historical()

    if inpt == 2:
        return inpt

    if inpt == 3:
        os.system('clear')
        sys.exit(0)

    else:
        print('Incorrect input. Try again.')
        return input_menu()

if __name__ == '__main__':
    os.system('clear')
    user_input = input_menu()
    os.system('clear')

    if user_input == 2:
        curr_ylds()

    else:
        param = user_input
        param_list = [int(digit) for digit in str(param)]
        ylds(*param_list)

