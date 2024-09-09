class Draw:
    def drawCircle(self, x, y, radius):
        pass


class Drawing1(Draw):
    def drawCircle(self, x, y, color):
        print(f"Draw circle at: ({x}; {y}), color: {color}")


class Drawing2(Draw):
    def drawCircle(self, x, y, color):
        print(f"Draw circle at: ({x}; {y}), color: {color}")


class Shape:
    def draw(self):
        pass

    def reDraw(self, pct):
        pass


class Circle(Shape):
    def __init__(self, x, y, color, draw):
        self.__x = x
        self.__y = y
        self.__color = color
        self.__draw = draw

    def draw(self):
        self.__draw.drawCircle(self.__x, self.__y, self.__color)

    def reDraw(self, newColor):
        self.__color = newColor


def main():
    shapes = [
        Circle(1, 2, 'green', Drawing1()),
        Circle(5, 7, 'red', Drawing2())
    ]
    print('Before:')
    for shape in shapes:
        shape.draw()
    print('After:')
    for shape in shapes:
        shape.reDraw('blue')
        shape.draw()

if __name__ == "__main__":
    main()