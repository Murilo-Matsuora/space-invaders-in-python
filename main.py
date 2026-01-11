from turtle import Screen, Turtle
from crab import Crab, CRAB_GIF_FILES, CRAB_SIZE
from explosion import Explosion
from player import Player
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
ENEMIES_PER_ROW = 10
ENEMIES_SPACING = 10
PADDING_TOP = 70
ENEMIES_MOVEMENT_SIDE = 10
ENEMIES_MOVEMENT_DOWN = 30
PLAYER_SPEED = 10
SCORE_FONT = ('Courier', 36, 'bold')
GAME_OVER_FONT = ('Arial', 48, 'bold')

def detect_game_over():
    global game_over

    if player.score >= 30:
            score_turtle.clear()
            score_turtle.goto(0, 20)
            score_turtle.color("green")
            score_turtle.write("You win", align="center", font=GAME_OVER_FONT)
            game_over = True

    for enemy in enemies:
        if enemy.ycor() < -SCREEN_HEIGHT / 2 + 50:
            score_turtle.clear()
            score_turtle.goto(0, 20)
            score_turtle.color("red")
            score_turtle.write("Game Over", align="center", font=GAME_OVER_FONT)
            game_over = True

            break
    
    if game_over:
        score_turtle.goto(0, -20)
        score_turtle.color("white")
        score_turtle.write(f"Final Score: {player.score}", align="center", font=SCORE_FONT)

def update_scoreboard():
    score_turtle.clear()
    score_turtle.write(player.score, align="center", font=SCORE_FONT)

def player_shoot():
    shot = Turtle(visible=False)
    shot.pu()
    shot.seth(90)
    shot.color("white")
    shot.goto(player.xcor(), player.ycor())
    shot.pensize(8)
    shot.pd()
    
    shots.append(shot)
    
def detect_shot_collision(curr_shot):
    for enemy in enemies:
        if curr_shot.distance(enemy.xcor(), enemy.ycor()) < enemy.size - 20:
            enemies.remove(enemy)
            enemy.hideturtle()
            e = Explosion(enemy.xcor(), enemy.ycor())
            explosions.append(e)

            shots.remove(curr_shot)
            curr_shot.clear()

            player.score += 1
            update_scoreboard()

def end_explosions():
    for explosion in explosions:
        if explosion.end_after_duration():
            explosions.remove(explosion)

screen = Screen()
screen.title("Space invaders")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
for frame in CRAB_GIF_FILES:
    screen.register_shape(frame)
screen.register_shape("explosion.gif")
screen.bgcolor("black")
screen.tracer(0)
screen.listen()
screen.onkeypress(key='space', fun=player_shoot)

player = Player()
screen.onkeypress(key='a', fun=player.move_player_left)
screen.onkeypress(key='d', fun=player.move_player_right)

shots = []

enemies = []

explosions = []

crabs_row_length = ENEMIES_PER_ROW * (CRAB_SIZE + ENEMIES_SPACING) - ENEMIES_SPACING
crabs_row_start_x = - crabs_row_length / 2
for i in range(3):
    crabs_row_start_y = (SCREEN_HEIGHT / 2 - PADDING_TOP) - i * (CRAB_SIZE + ENEMIES_SPACING)

    c = Crab(crabs_row_start_x, crabs_row_start_y)
    enemies.append(c)
    for j in range(1, ENEMIES_PER_ROW):
        c = Crab(crabs_row_start_x + j * (CRAB_SIZE + ENEMIES_SPACING), crabs_row_start_y)
        enemies.append(c)

start_time = time.time()
current_crab_frame = 0
direction = 1
reached_end = False

score_turtle = Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, SCREEN_HEIGHT / 2 - 50)
score_turtle.color("white")
score_turtle.write("0", align="center", font=SCORE_FONT)

game_over = False

while not game_over:
    time.sleep(0.01)
    if current_crab_frame != int((start_time - time.time()) % 6):
        current_crab_frame = int((start_time - time.time()) % 6)
        reached_end = False

        for crab in enemies:
            crab.change_shape(CRAB_GIF_FILES[current_crab_frame])
            crab.move_side(ENEMIES_MOVEMENT_SIDE * direction)

            if not reached_end and abs(crab.xcor() + CRAB_SIZE/2 * direction) > SCREEN_WIDTH / 2:
                reached_end = True
                
        if reached_end:
            direction *= -1
            for crab in enemies:
                crab.move_down(ENEMIES_MOVEMENT_DOWN)

    
    for shot in shots:
        if shot.ycor() < SCREEN_HEIGHT/2 + 15:
            shot.clear()
            shot.forward(8)
            
            detect_shot_collision(shot)
            
        else:
            shots.remove(shot)

    end_explosions()
    detect_game_over()

    screen.update()

screen.mainloop()