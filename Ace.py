class Ace():

    def __init__(self):
        self.value = 0

    def change_value(self):
        pick = int(input("Do you want your ace to equal 1 or 11: "))
        test = True
        while test:
            if not (pick == 1 or pick == 11):
                print("Invalid number, please pick 1 or 11")
                pick = int(input("Do you want your ace to equal 1 or 11: "))
            else:
                self.value = pick
                test = False

    def get_value(self):
        return self.value
