import turtle
import random

game_screen = turtle.Screen()
game_screen.bgcolor("Cadet Blue1")
game_screen.title("Catch The Turtle")
FONT = ("Arial", 30, "normal")
score = 0
game_over = False

turtle_list = []
score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()


def setup_score_turtle():
    top_height = game_screen.window_height() / 2
    y = top_height * 0.88

    score_turtle.hideturtle()
    score_turtle.color("dark red")
    score_turtle.penup()
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)




grid_size = 15
def make_turtle(x, y):
    x_turtle = turtle.Turtle()

    def handle_click(x, y,):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=FONT)



    x_turtle.onclick(handle_click)
    x_turtle.penup()
    x_turtle.shape("turtle")
    x_turtle.color("dark green")
    x_turtle.shapesize(2, 2)
    x_turtle.penup()
    x_turtle.goto(x * grid_size, y * grid_size)
    turtle_list.append(x_turtle)

x_coord = [-30, -20, -10, 0, 10, 20, 30]
y_coord = [20, 10, 0, -10, -20]

def setup_turtles():
    for x in x_coord:
        for y in y_coord:
            make_turtle(x, y)

def hide_turtles():
    for x_turtle in turtle_list:
        x_turtle.hideturtle()



def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        game_screen.ontimer(show_turtles_randomly, 700)

def countdown(time):
    global game_over
    top_height = game_screen.window_height() / 2
    y = top_height * 0.75

    countdown_turtle.hideturtle()
    countdown_turtle.color("black")
    countdown_turtle.penup()
    countdown_turtle.setposition(0, y)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=FONT)
        game_screen.ontimer(lambda: countdown(time - 1), 1000)

    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!".format(time), move=False, align="center", font=FONT)

turtle.tracer(0)
setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
countdown(10)
turtle.tracer(1)

game_screen.mainloop()

