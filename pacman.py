import uvage
import random
import lists

camera = uvage.Camera(560, 620)
p1 = uvage.from_color(280, 550, "yellow", 20, 20)
player_speed = 5
coins = None
ghosts = None
walls = lists.walls
countup = 0


def ghost_move():
    global random
    global walls
    global countup
    if (int(countup) % 30) == 0:
        for ghost in ghosts:
            for wall in walls:
                rand = random.randint(0, 3)
                if rand == 0 and not ghost.right_touches(wall):
                    ghost.xspeed = player_speed
                elif rand == 1 and not ghost.left_touches(wall):
                    ghost.xspeed = -player_speed
                elif rand == 2 and not ghost.top_touches(wall):
                    ghost.yspeed = -player_speed
                elif rand == 3 and not ghost.bottom_touches(wall):
                    ghost.yspeed = player_speed
    for ghost in ghosts:
        ghost.move_speed()
        for wall in walls:
            for ghost in ghosts:
                if ghost.touches(wall, 9):
                    ghost.move_to_stop_overlapping(wall, 10)

def player_move ():
    global walls
    if uvage.is_pressing('d'):
        p1.xspeed = player_speed
    elif uvage.is_pressing('a'):
        p1.xspeed = -player_speed
    elif uvage.is_pressing('w'):
        p1.yspeed = -player_speed
    elif uvage.is_pressing('s'):
        p1.yspeed = player_speed

    p1.move_speed()
    for wall in walls:
        if p1.touches(wall, 9):
            p1.move_to_stop_overlapping(wall, 10)

score = 0
game_on = True

def ghost_collide():
    global game_on
    for ghost in ghosts:
        if p1.touches(ghost, -5):
            game_on = False
            camera.draw(uvage.from_color(280, 295, 'black', 80, 30))
            camera.draw(uvage.from_text(280, 295, 'GAME OVER', 120, "Red", bold=True))
            camera.draw(uvage.from_text(280, 350, "Press \'R\' to restart the game", 30, 'white', bold=True))

def coin1():
    global coins
    global score
    global game_on

    for x in coins:
        if p1.touches(x, -5):
            x.y = 10000
            score += 1

    if score == len(coins):
        game_on = False

    camera.draw(uvage.from_text(280, 295, str(score), 50, "Red", bold=True))


def tick():
    global game_on
    global countup
    global coins
    global p1
    global ghosts
    global lists
    if game_on:
        coins = lists.coins
        ghosts = lists.ghosts

        camera.clear('black')
        camera.draw(p1)
        for wall in walls:
            camera.draw(wall)
        for coin in coins:
            camera.draw(coin)
        for ghost in ghosts:
            camera.draw(ghost)
        player_move()
        coin1()
        ghost_move()
        countup += 2
        ghost_collide()

    else:
        if uvage.is_pressing('r'):
            coins = lists.coins
            p1 = uvage.from_color(280, 550, "yellow", 20, 20)
            ghosts = lists.ghosts
            for coin in coins:
                camera.draw(coin)
            for ghost in ghosts:
                camera.draw(ghost)
            game_on = True
    camera.display()

uvage.timer_loop(30, tick)