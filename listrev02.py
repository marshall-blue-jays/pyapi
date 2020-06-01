#!/usr/bin/python3

def main():
    anotheremptylist = []

    ## This will throw an Error
    ## the extend methoid expects exactly one argument
    anotheremptylist.extend('10.0.0.1', 'retro_game_server')

    print(anotheremptylist)

if __name__ == "__main__":
    main()
