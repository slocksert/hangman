import hangman

def main():
    welcome = input(f'{hangman.dashs}\nDo you want to play hangman? y/n\n{hangman.dashs}\n\n')
    if welcome != 'y':
        quit('\nOkay Bye!')
    else:
        hangman.Game().call_class()

if __name__ == '__main__':
    main()