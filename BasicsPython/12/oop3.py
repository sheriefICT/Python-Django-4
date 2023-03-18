class Game:

    def __init__(self):
        while True:
            print(''''
            welcome, choose one fo our game...
                1 : sentances_no_duplicates
                2 : devidedpy 
                3 : to exit  
            ''')
            user_choice = int(input('Enter your number game :'))
            if user_choice == 1:
                s = input('Enter your S : ')
                self.sentances_no_duplicates(s)
            elif user_choice == 2:
                x = int(input('Enter first number : '))
                y = int(input('Enter Second number : '))
                self.devidedpy(x, y)
            elif user_choice == 3:
                print('goodbay....')
                break
            else:
                print('please enter number between 1 :3')
            play_again = input('Enter any key to again play game , n to exit')
            if play_again == "n":
                print('goodbay....')
                break

    def sentances_no_duplicates(self, s):
        words = s.split(' ')
        new_words = []
        for w in words:
            if w not in new_words:
                new_words.append(w)

        print('_'.join(new_words))

    def devidedpy(self, x, y):
        result = []
        for n in range(1, 101):
            if n % x == 0 and n % y == 0:
                result.append(n)
        print(result)


g = Game()


