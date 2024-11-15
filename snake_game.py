import turtle
import time
import random

# Initial game settings
delay = 0.1
score = 0
high_score = 0

# Set up the screen
window = turtle.Screen()
window.title("Snake Game by Roki Ghosh")
window.bgcolor("black")
window.setup(width=600, height=600)
window.tracer(0)  # Turns off the screen updates for smoother performance

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randint(-290, 290), random.randint(-290, 290))

# List to store snake body segments
segments = []

# Scoreboard setup
score_display = turtle.Turtle()
score_display.speed(0)
score_display.shape("square")
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions to control the snake's direction
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

# Function to move the snake's head
def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings
window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")

# Main game loop
while True:
    window.update()

    # Check for collision with the border
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide segments after a collision
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # Reset score and update display
        score = 0
        delay = 0.1  # Reset the speed
        score_display.clear()
        score_display.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for collision with food
    if head.distance(food) < 20:
        # Move food to a random position
        food.goto(random.randint(-290, 290), random.randint(-290, 290))

        # Add new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Increase the score and update high score if necessary
        score += 10
        if score > high_score:
            high_score = score
        score_display.clear()
        score_display.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

        # Speed up the game slightly with each food consumed
        delay = max(0.05, delay - 0.001)

    # Move the snake body segments in reverse order
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    # Move the first segment to the head position
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    # Move the snake's head
    move()

    # Check for collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide segments after a collision
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # Reset score and update display
            score = 0
            delay = 0.1  # Reset the speed
            score_display.clear()
            score_display.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Short pause to control the snake speed
    time.sleep(delay)

window.mainloop()
