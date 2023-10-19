import turtle

# Set up the screen
window = turtle.Screen()
window.title("Breakout Game")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = -1

# Blocks
blocks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for y in range(5):
    for x in range(-7, 8):
        block = turtle.Turtle()
        block.shape("square")
        block.color(colors[y])
        block.penup()
        block.goto(x * 50, 200 - y * 25)
        blocks.append(block)

# Score
score = 0
scoreboard = turtle.Turtle()
scoreboard.hideturtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.goto(0, 260)
scoreboard.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Lives
lives = 5
livesboard = turtle.Turtle()
livesboard.hideturtle()
livesboard.color("white")
livesboard.penup()
livesboard.goto(-380, 260)
livesboard.write("Lives: 5", align="left", font=("Courier", 24, "normal"))

# Start Button
start_button = turtle.Turtle()
start_button.hideturtle()
start_button.shape("square")
start_button.color("white")
start_button.penup()
start_button.goto(0, 0)
start_button.write("Click to Start", align="center", font=("Courier", 24, "normal"))

# Functions
def start_game(x, y):
    start_button.clear()
    window.onclick(None)  # Disable the click event handler
    game_loop()

def paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 20
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 20
    paddle.setx(x)

# Keyboard bindings
window.listen()
window.onkeypress(paddle_left, "Left")
window.onkeypress(paddle_right, "Right")

# Main game loop
def game_loop():
    global score, lives

    while lives > 0:
        window.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Check for wall collisions
        if ball.xcor() > 390 or ball.xcor() < -390:
            ball.dx *= -1
        if ball.ycor() > 290:
            ball.dy *= -1

        # Check for paddle collision
        if (ball.ycor() < -240) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
            ball.dy *= -1
            ball.dx = (ball.xcor() - paddle.xcor()) / 10

        # Check for block collisions
        for block in blocks:
            if block.distance(ball) < 30:
                block.goto(1000, 1000)  # Move the block off the screen
                blocks.remove(block)
                score += 1
                scoreboard.clear()
                scoreboard.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

                # Check if all blocks are cleared
                if len(blocks) == 0:
                    scoreboard.goto(0, 0)
                    scoreboard.write("You Win!", align="center", font=("Courier", 48, "normal"))
                    ball.goto(1000, 1000)  # Move the ball off the screen
                    break

                # Bounce the ball in the opposite direction
                ball.dy *= -1

        # Check if the ball passes through the paddle
        if ball.ycor() < -290:
            lives -= 1
            livesboard.clear()
            livesboard.write(f"Lives: {lives}", align="left", font=("Courier", 24, "normal"))
            if lives == 0:
                scoreboard.goto(0, 0)
                scoreboard.write(f"Game Over\nFinal Score: {score}", align="center", font=("Courier", 48, "normal"))
            ball.goto(0, 0)
            ball.dy *= -1

# Click event handler for the start button```python
window.onclick(start_game)

# Slow down the animation speed
window.delay(10)

# Start the game
window.mainloop()