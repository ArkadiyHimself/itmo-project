def turnO():
    turn = input('Координата нолика: ')
    return turn


def turnX():
    turn = input('Координата крестика: ')
    return turn


class Field:
    def __init__(self):
        self.field = {'A1': '*', 'A2': '*', 'A3': '*', 'B1': '*', 'B2': '*', 'B3': '*', 'C1': '*', 'C2': '*', 'C3': '*'}
        self.startingfield = self.field

    def reset(self):
        self.field = self.startingfield

    def put_value(self, point, player):
        if self.field[point] == '*':
            del self.field[point]
            self.field[point] = player
        else:
            print("Клетка уже занята!")


    def render(self):
        print("   | 1 | 2 | 3 |")
        print("---|---|---|---|")
        print(" A |", self.field['A1'], "|", self.field['A2'], "|", self.field['A3'], "|")
        print("---|---|---|---|")
        print(" B |", self.field['B1'], "|", self.field['B2'], "|", self.field['B3'], "|")
        print("---|---|---|---|")
        print(" C |", self.field['C1'], "|", self.field['C2'], "|", self.field['C3'], "|")
        print("---|---|---|---|")


    def winning(self):
        coor = []
        for x, y in self.field.items():
            if y == '*':
                coor.append(y)
        if self.field['A1'] == self.field['A2'] == self.field['A3'] and self.field['A1'] != '*':
            return "end"
        elif self.field['B1'] == self.field['B2'] == self.field['B3'] and self.field['B1'] != '*':
            return "end"
        elif self.field['C1'] == self.field['C2'] == self.field['C3'] and self.field['C1'] != '*':
            return "end"
        elif self.field['A1'] == self.field['B1'] == self.field['C1'] and self.field['A1'] != '*':
            return "end"
        elif self.field['A2'] == self.field['B2'] == self.field['C2'] and self.field['A2'] != '*':
            return "end"
        elif self.field['A3'] == self.field['B3'] == self.field['C3'] and self.field['A3'] != '*':
            return "end"
        elif self.field['A1'] == self.field['B2'] == self.field['C3'] and self.field['A1'] != '*':
            return "end"
        elif self.field['A3'] == self.field['B2'] == self.field['C1'] and self.field['A3'] != '*':
            return "end"
        elif coor == []:
            return "draw"
        else:
            return "continue"


class Game():
    def __init__(self):
        self.end = False
        self.turning = 1
        self.field = Field()
        self.draw = False

    def start(self):
        self.field.reset()
        self.field.render()
        while not self.end:
            pole = self.field
            if self.turning % 2 == 0:
                symbol = 'O'
            else:
                symbol = 'X'
            if self.turning % 2 == 0:
                turned = turnO()
            else:
                turned = turnX()
            if turned == 'A1' or turned == 'A2' or turned == 'A3' or turned == 'B1' or turned == 'B2' or turned == 'B3' or turned == 'C1' or turned == 'C2' or turned == 'C3':
                self.field.put_value(turned, symbol)
                self.field.render()
            else:
                print("Такой координаты не существует!")
            if self.field.winning() == 'end':
                self.end = True
            elif self.field.winning() == 'draw':
                self.end = True
                self.draw = True
            else:
                self.turning += 1
        if self.draw == True:
            print("Ничья!")
        else:
            if self.turning % 2 == 0:
                print("Победил нолик!")
            elif self.turning % 2 != 0:
                print("Победил крестик!")


game = Game()
print("Играть?")
def playing():
    game.start()
    print("Заново?")
    if input() == 'Да':
        playing()
if input() == 'Да':
    playing()