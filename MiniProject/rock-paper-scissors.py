from game import Game
def get_user_menu_choice():
    want_play = input("A.Play a new game\n B. Show scores \n C.Quit \n").upper()
    return want_play
def print_results(results):
    print(results)
def main():
    game= Game()
    results = {'lose' : 0, 'win' : 0, 'draw' : 0}
    choice = get_user_menu_choice()
    while choice != "C":
        if choice == "A":
            result = game.play()
            if result == 'lose':
                results['lose'] += 1
            if result == 'win':
                results['win'] +=  1
            if result == 'draw':
                results['draw'] += 1
        elif choice == 'B':
            print_results(results)
        choice = get_user_menu_choice()
    print_results(results)
main()