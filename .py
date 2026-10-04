import turtle
screen=turtle.Screen()
screen.bgcolor("turquoise")
screen.title("were")
board=turtle.Turtle()
board.speed("fastest")
board.hideturtle()
colors =  ["black","white","green","red","blue","orange"]
for i in range (1000):
    board.color(colors[i % len(colors)])
    board.width(7.5)
    board.forward(i * 2)
    board.left(175.31)
turtle.done()
#Please run this