# Allows to make graphics
import turtle
import winsound

# Game window
game_window = turtle.Screen()
game_window.title("Pong")
game_window.bgcolor("black")
game_window.setup(width=800, height=600)
game_window.tracer(0) # Accelerates the game

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # Speed of animation not the bar
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Default 20px x 20px
paddle_a.penup() # Does not draw lines when moving
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # Speed of animation not the bar
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.penup() # Does not draw lines when moving
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # Speed of animation not the ball
ball.shape("circle")
ball.color("white")
ball.penup() # Does not draw lines when moving
ball.goto(0,0)
ball.dx = 0.1
ball.dy = -0.1

"""# Obstacles
obstacle_one = turtle.Turtle()
obstacle_one.speed(0) # Speed of animation not the ball
obstacle_one.shape("triangle")
obstacle_one.color("red")
obstacle_one.penup() # Does not draw lines when moving
obstacle_one.goto(150,150)

obstacle_two = turtle.Turtle()
obstacle_two.speed(0) # Speed of animation not the ball
obstacle_two.shape("triangle")
obstacle_two.color("red")
obstacle_two.penup() # Does not draw lines when moving
obstacle_two.goto(-150,-150)"""

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, 
                                                            "normal"))

# Paddle movement
def paddle_a_up():
    y = paddle_a.ycor() # Returns the y coordinate
    y += 20
    if y < 250:  # Limit the paddle's movement
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() 
    y -= 20 
    if y > -240:  # Limit the paddle's movement
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()  
    y += 20 
    if y < 250:  # Limit the paddle's movement
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() 
    y -= 20 
    if y > -240:  # Limit the paddle's movement
        paddle_b.sety(y)

# Keyboard binding
game_window.listen()
game_window.onkeypress(paddle_a_up, "w")
game_window.onkeypress(paddle_a_down, "s")
game_window.onkeypress(paddle_b_up, "Up")
game_window.onkeypress(paddle_b_down, "Down")

# Main game loop
def paddle_and_ball_collisions(paddle_a, paddle_b, ball):
    if (ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and 
    ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1
        winsound.PlaySound("fart.wav", winsound.SND_ASYNC)
    
    elif (ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and 
    ball.ycor() > paddle_b.ycor() - 50):
        ball.dx *= -1
        winsound.PlaySound("fart.wav", winsound.SND_ASYNC)

def speed_incrementer():
    if score_a == 2 and score_b == 2:
        ball.dx = 0.3
        ball.dy = -0.3
        ball.color("red")
        paddle_a.sety(40)
        paddle_b.sety(40)
        
while True:
    game_window.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("fart.wav", winsound.SND_ASYNC)
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("fart.wav", winsound.SND_ASYNC)
    
    # Left and right
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), 
                  align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound("scream.wav", winsound.SND_ASYNC)

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), 
                  align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        winsound.PlaySound("scream.wav", winsound.SND_ASYNC)

    paddle_and_ball_collisions(paddle_a, paddle_b, ball)
    speed_incrementer()   

"""    if (ball.distance(obstacle_one) < 25 or 
        ball.distance(obstacle_two) < 25):  
        ball.dx *= -1"""
