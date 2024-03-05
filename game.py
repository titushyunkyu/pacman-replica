#David Choi vsk2re
#Titus Lee hvm4sg

#We are going to recreate Pac-Man. Pac-Man is a maze chase game where the player controls a character in a maze filled with dots.
#The objective of the game is for the player to collect every dot in the maze. While trying to collect the dots, there are 4 colored
#ghosts that try to stop Pac-Man from getting all the dots.

#Basic Features:
#1. The arrow keys will be used to control the X and Y movments for Pac-Man.
#2. If the ghosts collide with Pac-Man, the player will lose the game and the game ends.
#3. We will use Pac-Man images and ghost images.

#Additional Features:
#1. There will be a timer that counts down. The player must collect all the coins before the timer reaches zero.
#2. There will be collectibles in the game, which will be dots (coins) placed around the maze. The only way to beat each level is by collecting
#   the coins.
#3. The user will be able to restart the game after they win/lose without re-running the program.
#4. There will be enemies that try to stop the player from collecting all the dots called ghosts. If the player touches a ghost, they lose the game.

#Changes From CP2
#We decided to swap out the multiple level and the sprite animation additional features with a timer and a restart feature.
#We added coins to the game which are stored in lists. When touched by pacman, they disappear and are then converted to points.
#Enemies have been added to the game. They are visualized as ghosts that float through the maze. If pacman touches a ghost, the player loses.
#We added an image of a smiley face for pacman instead of just a yellow box.
#A timer and the number of coins collected have been added to the center of the maze. If the timer reaches 0, the player loses.
#Pacman's movements have been refined so the movements are less choppy and we removed stuttering that used to exist when hitting walls.
#The restart feature that has been added allows users to press 'r' to continue playing once the game is finished.
#The timer counts down 120 seconds. If the user has not collected all the coins in 120 seconds, the player loses.

#Instructions
#Once the program is run, the game begins. Pacman can be controlled the W A S and D keys. W and S control vertical movements and
#A and D control horizontal movments. The player must collect all the coins to win the game. Coins can be collected by touching them.
#Once a coin is touched, it will disappear and one point will be added to the score. While trying to collect the coins, there will be
#ghosts that move around the map in order to try to stop pacman. If a ghost is touched, you lose the game. The game must be completed in
#120 seconds or else the player loses. A timer can be found next to the score in the center of the maze. Once the player has won or lost,
#the user will be prompted to select 'r' to play the game again.

#importing the uvage game library
import uvage
#importing the random class
import random

#setting the size of the screen to 560 x 620
camera = uvage.Camera(800, 620)
#creating player 1. player 1 is a png file of a smiley face that starts at (280 x 550)
p1 = uvage.from_image(400, 550, "smiley.png")
#scaling the image so it fits in the maze
p1.scale_by(.026)
player_speed = 5

#creation of walls that create the maze
#creation of walls that create the maze
walls = [
    uvage.from_color(400, 5, "dark blue", 1000, 10),
    uvage.from_color(400, 615, "dark blue", 1000, 10),
    uvage.from_color(125, 310, "dark blue", 10, 1000),
    uvage.from_color(675, 310, "dark blue", 10, 1000),
    uvage.from_color(200, 70, "dark blue", 60, 40),
    uvage.from_color(180, 170, "dark blue", 20, 80),
    uvage.from_color(200, 200, "dark blue", 60, 20),
    uvage.from_color(180, 290, "dark blue", 20, 80),
    uvage.from_color(200, 320, "dark blue", 60, 20),
    uvage.from_color(180, 410, "dark blue", 20, 80),
    uvage.from_color(200, 440, "dark blue", 60, 20),
    uvage.from_color(180, 530, "dark blue", 20, 80),
    uvage.from_color(200, 560, "dark blue", 60, 20),
    uvage.from_color(280, 130, "dark blue", 20, 160),
    uvage.from_color(260, 140, "dark blue", 60, 20),
    uvage.from_color(260, 260, "dark blue", 60, 20),
    uvage.from_color(280, 380, "dark blue", 20, 140),
    uvage.from_color(290, 380, "dark blue", 120, 20),
    uvage.from_color(280, 550, "dark blue", 20, 120),
    uvage.from_color(260, 500, "dark blue", 60, 20),
    uvage.from_color(400, 60, "dark blue", 140, 20),
    uvage.from_color(400, 100, "dark blue", 20, 100),
    uvage.from_color(400, 200, "dark blue", 140, 20),
    uvage.from_color(340, 160, "dark blue", 20, 100),
    uvage.from_color(460, 160, "dark blue", 20, 100),
    uvage.from_color(400, 410, "dark blue", 20, 80),
    uvage.from_color(400, 590, "dark blue", 20, 80),
    uvage.from_color(400, 440, "dark blue", 140, 20),
    uvage.from_color(400, 500, "dark blue", 140, 20),
    uvage.from_color(340, 530, "dark blue", 20, 80),
    uvage.from_color(460, 530, "dark blue", 20, 80),
    uvage.from_color(400, 290, "dark blue", 140, 80),
    uvage.from_color(400, 290, "black", 100, 40),
    uvage.from_color(600, 70, "dark blue", 60, 40),
    uvage.from_color(620, 170, "dark blue", 20, 80),
    uvage.from_color(600, 200, "dark blue", 60, 20),
    uvage.from_color(620, 290, "dark blue", 20, 80),
    uvage.from_color(600, 320, "dark blue", 60, 20),
    uvage.from_color(620, 410, "dark blue", 20, 80),
    uvage.from_color(600, 440, "dark blue", 60, 20),
    uvage.from_color(620, 530, "dark blue", 20, 80),
    uvage.from_color(600, 560, "dark blue", 60, 20),
    uvage.from_color(520, 130, "dark blue", 20, 160),
    uvage.from_color(540, 140, "dark blue", 60, 20),
    uvage.from_color(540, 260, "dark blue", 60, 20),
    uvage.from_color(520, 380, "dark blue", 20, 140),
    uvage.from_color(510, 380, "dark blue", 120, 20),
    uvage.from_color(520, 550, "dark blue", 20, 120),
    uvage.from_color(540, 500, "dark blue", 60, 20),
]

#all the coins in the game that are spread out throughout the maze
coins = [
    uvage.from_color(650, 30, "yellow", 5, 5),
    uvage.from_color(650, 70, "yellow", 5, 5),
    uvage.from_color(650, 110, "yellow", 5, 5),
    uvage.from_color(650, 150, "yellow", 5, 5),
    uvage.from_color(650, 190, "yellow", 5, 5),
    uvage.from_color(650, 230, "yellow", 5, 5),
    uvage.from_color(650, 270, "yellow", 5, 5),
    uvage.from_color(650, 310, "yellow", 5, 5),
    uvage.from_color(650, 350, "yellow", 5, 5),
    uvage.from_color(650, 390, "yellow", 5, 5),
    uvage.from_color(650, 430, "yellow", 5, 5),
    uvage.from_color(650, 470, "yellow", 5, 5),
    uvage.from_color(650, 510, "yellow", 5, 5),
    uvage.from_color(650, 550, "yellow", 5, 5),
    uvage.from_color(650, 590, "yellow", 5, 5),
    uvage.from_color(620, 30, "yellow", 5, 5),
    uvage.from_color(620, 110, "yellow", 5, 5),
    uvage.from_color(620, 230, "yellow", 5, 5),
    uvage.from_color(620, 350, "yellow", 5, 5),
    uvage.from_color(620, 470, "yellow", 5, 5),
    uvage.from_color(620, 590, "yellow", 5, 5),
    uvage.from_color(590, 30, "yellow", 5, 5),
    uvage.from_color(590, 110, "yellow", 5, 5),
    uvage.from_color(590, 170, "yellow", 5, 5),
    uvage.from_color(590, 230, "yellow", 5, 5),
    uvage.from_color(590, 290, "yellow", 5, 5),
    uvage.from_color(590, 350, "yellow", 5, 5),
    uvage.from_color(590, 390, "yellow", 5, 5),
    uvage.from_color(590, 470, "yellow", 5, 5),
    uvage.from_color(590, 530, "yellow", 5, 5),
    uvage.from_color(590, 590, "yellow", 5, 5),
    uvage.from_color(550, 30, "yellow", 5, 5),
    uvage.from_color(550, 70, "yellow", 5, 5),
    uvage.from_color(550, 110, "yellow", 5, 5),
    uvage.from_color(550, 170, "yellow", 5, 5),
    uvage.from_color(550, 230, "yellow", 5, 5),
    uvage.from_color(550, 290, "yellow", 5, 5),
    uvage.from_color(550, 350, "yellow", 5, 5),
    uvage.from_color(550, 410, "yellow", 5, 5),
    uvage.from_color(550, 470, "yellow", 5, 5),
    uvage.from_color(550, 530, "yellow", 5, 5),
    uvage.from_color(550, 590, "yellow", 5, 5),

    uvage.from_color(520, 30, "yellow", 5, 5),
    uvage.from_color(520, 230, "yellow", 5, 5),
    uvage.from_color(520, 290, "yellow", 5, 5),
    uvage.from_color(520, 470, "yellow", 5, 5),
    uvage.from_color(490, 30, "yellow", 5, 5),
    uvage.from_color(490, 70, "yellow", 5, 5),
    uvage.from_color(490, 110, "yellow", 5, 5),
    uvage.from_color(490, 150, "yellow", 5, 5),
    uvage.from_color(490, 190, "yellow", 5, 5),
    uvage.from_color(490, 230, "yellow", 5, 5),
    uvage.from_color(490, 270, "yellow", 5, 5),
    uvage.from_color(490, 310, "yellow", 5, 5),
    uvage.from_color(490, 350, "yellow", 5, 5),
    uvage.from_color(490, 410, "yellow", 5, 5),
    uvage.from_color(490, 470, "yellow", 5, 5),
    uvage.from_color(490, 510, "yellow", 5, 5),
    uvage.from_color(490, 550, "yellow", 5, 5),
    uvage.from_color(490, 590, "yellow", 5, 5),
    uvage.from_color(460, 30, "yellow", 5, 5),
    uvage.from_color(460, 90, "yellow", 5, 5),
    uvage.from_color(460, 230, "yellow", 5, 5),
    uvage.from_color(460, 350, "yellow", 5, 5),
    uvage.from_color(460, 410, "yellow", 5, 5),
    uvage.from_color(460, 470, "yellow", 5, 5),
    uvage.from_color(460, 590, "yellow", 5, 5),
    uvage.from_color(430, 30, "yellow", 5, 5),
    uvage.from_color(430, 90, "yellow", 5, 5),
    uvage.from_color(430, 130, "yellow", 5, 5),
    uvage.from_color(430, 170, "yellow", 5, 5),
    uvage.from_color(430, 230, "yellow", 5, 5),
    uvage.from_color(430, 350, "yellow", 5, 5),
    uvage.from_color(430, 410, "yellow", 5, 5),
    uvage.from_color(430, 470, "yellow", 5, 5),
    uvage.from_color(430, 530, "yellow", 5, 5),
    uvage.from_color(430, 590, "yellow", 5, 5),

    uvage.from_color(310, 30, "yellow", 5, 5),
    uvage.from_color(310, 70, "yellow", 5, 5),
    uvage.from_color(310, 110, "yellow", 5, 5),
    uvage.from_color(310, 150, "yellow", 5, 5),
    uvage.from_color(310, 190, "yellow", 5, 5),
    uvage.from_color(310, 230, "yellow", 5, 5),
    uvage.from_color(310, 270, "yellow", 5, 5),
    uvage.from_color(310, 310, "yellow", 5, 5),
    uvage.from_color(310, 350, "yellow", 5, 5),
    uvage.from_color(310, 410, "yellow", 5, 5),
    uvage.from_color(310, 470, "yellow", 5, 5),
    uvage.from_color(310, 510, "yellow", 5, 5),
    uvage.from_color(310, 550, "yellow", 5, 5),
    uvage.from_color(310, 590, "yellow", 5, 5),
    uvage.from_color(340, 30, "yellow", 5, 5),
    uvage.from_color(340, 90, "yellow", 5, 5),
    uvage.from_color(340, 230, "yellow", 5, 5),
    uvage.from_color(340, 350, "yellow", 5, 5),
    uvage.from_color(340, 410, "yellow", 5, 5),
    uvage.from_color(340, 470, "yellow", 5, 5),
    uvage.from_color(340, 590, "yellow", 5, 5),
    uvage.from_color(370, 30, "yellow", 5, 5),
    uvage.from_color(370, 90, "yellow", 5, 5),
    uvage.from_color(370, 130, "yellow", 5, 5),
    uvage.from_color(370, 170, "yellow", 5, 5),
    uvage.from_color(370, 230, "yellow", 5, 5),
    uvage.from_color(370, 350, "yellow", 5, 5),
    uvage.from_color(370, 410, "yellow", 5, 5),
    uvage.from_color(370, 470, "yellow", 5, 5),
    uvage.from_color(370, 530, "yellow", 5, 5),
    uvage.from_color(370, 590, "yellow", 5, 5),

    uvage.from_color(150, 30, "yellow", 5, 5),
    uvage.from_color(150, 70, "yellow", 5, 5),
    uvage.from_color(150, 110, "yellow", 5, 5),
    uvage.from_color(150, 150, "yellow", 5, 5),
    uvage.from_color(150, 190, "yellow", 5, 5),
    uvage.from_color(150, 230, "yellow", 5, 5),
    uvage.from_color(150, 270, "yellow", 5, 5),
    uvage.from_color(150, 310, "yellow", 5, 5),
    uvage.from_color(150, 350, "yellow", 5, 5),
    uvage.from_color(150, 390, "yellow", 5, 5),
    uvage.from_color(150, 430, "yellow", 5, 5),
    uvage.from_color(150, 470, "yellow", 5, 5),
    uvage.from_color(150, 510, "yellow", 5, 5),
    uvage.from_color(150, 550, "yellow", 5, 5),
    uvage.from_color(150, 590, "yellow", 5, 5),
    uvage.from_color(180, 30, "yellow", 5, 5),
    uvage.from_color(180, 110, "yellow", 5, 5),
    uvage.from_color(180, 230, "yellow", 5, 5),
    uvage.from_color(180, 350, "yellow", 5, 5),
    uvage.from_color(180, 470, "yellow", 5, 5),
    uvage.from_color(180, 590, "yellow", 5, 5),
    uvage.from_color(210, 30, "yellow", 5, 5),
    uvage.from_color(210, 110, "yellow", 5, 5),
    uvage.from_color(210, 170, "yellow", 5, 5),
    uvage.from_color(210, 230, "yellow", 5, 5),
    uvage.from_color(210, 290, "yellow", 5, 5),
    uvage.from_color(210, 350, "yellow", 5, 5),
    uvage.from_color(210, 390, "yellow", 5, 5),
    uvage.from_color(210, 470, "yellow", 5, 5),
    uvage.from_color(210, 530, "yellow", 5, 5),
    uvage.from_color(210, 590, "yellow", 5, 5),
    uvage.from_color(250, 30, "yellow", 5, 5),
    uvage.from_color(250, 70, "yellow", 5, 5),
    uvage.from_color(250, 110, "yellow", 5, 5),
    uvage.from_color(250, 170, "yellow", 5, 5),
    uvage.from_color(250, 230, "yellow", 5, 5),
    uvage.from_color(250, 290, "yellow", 5, 5),
    uvage.from_color(250, 350, "yellow", 5, 5),
    uvage.from_color(250, 410, "yellow", 5, 5),
    uvage.from_color(250, 470, "yellow", 5, 5),
    uvage.from_color(250, 530, "yellow", 5, 5),
    uvage.from_color(250, 590, "yellow", 5, 5),
    uvage.from_color(280, 30, "yellow", 5, 5),
    uvage.from_color(280, 230, "yellow", 5, 5),
    uvage.from_color(280, 290, "yellow", 5, 5),
    uvage.from_color(280, 470, "yellow", 5, 5),

]

#creation of the6 ghosts in the game. the ghosts are a png file of a pacman ghost.
ghost1 = uvage.from_image(400, 230, "ghost.png")
#scaling the image so it fits in the  maze.
ghost1.scale_by(.034)

#creation of the6 ghosts in the game. the ghosts are a png file of a pacman ghost.
ghost2 = uvage.from_image(400, 230, "ghost.png")
#scaling the image so it fits in the  maze.
ghost2.scale_by(.034)

#creation of the6 ghosts in the game. the ghosts are a png file of a pacman ghost.
ghost3 = uvage.from_image(400, 230, "ghost.png")
#scaling the image so it fits in the  maze.
ghost3.scale_by(.034)

#creation of the6 ghosts in the game. the ghosts are a png file of a pacman ghost.
ghost4 = uvage.from_image(400, 230, "ghost.png")
#scaling the image so it fits in the  maze.
ghost4.scale_by(.034)

#creation of the6 ghosts in the game. the ghosts are a png file of a pacman ghost.
ghost5 = uvage.from_image(400, 230, "ghost.png")
#scaling the image so it fits in the  maze.
ghost5.scale_by(.034)

#creation of the6 ghosts in the game. the ghosts are a png file of a pacman ghost.
ghost6 = uvage.from_image(400, 230, "ghost.png")
#scaling the image so it fits in the  maze.
ghost6.scale_by(.034)

#list that stores all of the ghosts
ghosts = [
    ghost1,
    ghost2,
    ghost3,
    ghost4,
    ghost5,
    ghost6
]
countup = 0

#function for ghost movements
def ghost_move():
    global random
    global walls
    global countup
    # change ghost direction every 1 second since countup += 1 is called 30 times each second
    if (int(countup) % 30) == 0:
        for ghost in ghosts:
            for wall in walls:
                # randomize ghost direction except the direction that the ghost is already touching the wall
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
        # move the ghosts given a random direction from above
        ghost.move_speed()
        # make sure the ghosts stay within the map and the trail
        for wall in walls:
            for ghost in ghosts:
                if ghost.touches(wall, 9):
                    ghost.move_to_stop_overlapping(wall, 10)

#method for player movements
def player_move ():
    global walls
    #each of the W A S D keys are assigned a negative or positive x or y value speed
    if uvage.is_pressing('d'):
        p1.xspeed = player_speed
    elif uvage.is_pressing('a'):
        p1.xspeed = -player_speed
    elif uvage.is_pressing('w'):
        p1.yspeed = -player_speed
    elif uvage.is_pressing('s'):
        p1.yspeed = player_speed

    p1.move_speed()

    # make sure the player stays within the map and the given trail
    for wall in walls:
        if p1.touches(wall, 9):
            p1.move_to_stop_overlapping(wall, 10)

score = 0
game_on = True

# end game when user collides with ghost and show game over screen with option to restart the game
def ghost_collide():
    global game_on
    for ghost in ghosts:
        if p1.touches(ghost, -5):
            game_on = False
            camera.draw(uvage.from_color(400, 295, 'black', 80, 30))
            camera.draw(uvage.from_text(400, 295, 'GAME OVER', 120, "Red", bold=True))
            camera.draw(uvage.from_text(400,350, "Press \'R\' to restart the game", 30, 'white', bold=True))
def coin1():
    global coins
    global score
    global game_on

    #if the player touches a coin, the coin is removed from the maze and the player is awarded a point
    for x in coins:
        if p1.touches(x, -5):
            x.y = 10000
            score += 1
    #once the score reaches the number of total coins, the player wins and text is displayed congratulating the player and
    #prompting them to play again
    if score == len(coins):
        game_on = False
        camera.draw(uvage.from_color(400, 295, 'black', 80, 30))
        camera.draw(uvage.from_text(400, 320, "You Won!", 30, 'white', bold=True))
        camera.draw(uvage.from_text(400, 350, "Press \'R\' to restart the game", 30, 'white', bold=True))
    #the total number of coins collected is displayed
    camera.draw(uvage.from_text(730, 265, "score", 30, "Red", bold=True))
    camera.draw(uvage.from_text(730, 295, str(score), 30, "Red", bold=True))

#120 seconds
timer = 120

#function that manages the timer
def game_timer():
    global timer
    global game_on

    #subtracting 1/30 from 120 because there are 30 frames in a second, which results in 1 being subtracted from 120 every second
    timer -= 1 / 30
    #once the timer reaches 0, the game ends and a gameover screen is shown which prompts the user to click 'r' to play again
    if timer < 0:
        game_on = False
        camera.draw(uvage.from_color(400, 295, 'black', 80, 30))
        camera.draw(uvage.from_text(400, 295, 'GAME OVER', 120, "Red", bold=True))
        camera.draw(uvage.from_text(400, 350, "Press \'R\' to restart the game", 30, 'white', bold=True))

    #timer is displayed for the user
    camera.draw(uvage.from_text(60, 265, "timer", 30, "Red", bold=True))
    camera.draw(uvage.from_text(60, 295, str(int(timer)), 30, "Red", bold=True))

def tick():
    global game_on
    global countup
    global coins
    global p1
    global ghosts
    global lists
    global timer
    global score


    if game_on:
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
        game_timer()
        countup += 2
        ghost_collide()
    else:
        # if game ends, user has the option to restart the game. Once restarted, everything goes back to original set up.
        if uvage.is_pressing('r'):
            timer = 120
            score = 0
            coins = [
                uvage.from_color(650, 30, "yellow", 5, 5),
                uvage.from_color(650, 70, "yellow", 5, 5),
                uvage.from_color(650, 110, "yellow", 5, 5),
                uvage.from_color(650, 150, "yellow", 5, 5),
                uvage.from_color(650, 190, "yellow", 5, 5),
                uvage.from_color(650, 230, "yellow", 5, 5),
                uvage.from_color(650, 270, "yellow", 5, 5),
                uvage.from_color(650, 310, "yellow", 5, 5),
                uvage.from_color(650, 350, "yellow", 5, 5),
                uvage.from_color(650, 390, "yellow", 5, 5),
                uvage.from_color(650, 430, "yellow", 5, 5),
                uvage.from_color(650, 470, "yellow", 5, 5),
                uvage.from_color(650, 510, "yellow", 5, 5),
                uvage.from_color(650, 550, "yellow", 5, 5),
                uvage.from_color(650, 590, "yellow", 5, 5),
                uvage.from_color(620, 30, "yellow", 5, 5),
                uvage.from_color(620, 110, "yellow", 5, 5),
                uvage.from_color(620, 230, "yellow", 5, 5),
                uvage.from_color(620, 350, "yellow", 5, 5),
                uvage.from_color(620, 470, "yellow", 5, 5),
                uvage.from_color(620, 590, "yellow", 5, 5),
                uvage.from_color(590, 30, "yellow", 5, 5),
                uvage.from_color(590, 110, "yellow", 5, 5),
                uvage.from_color(590, 170, "yellow", 5, 5),
                uvage.from_color(590, 230, "yellow", 5, 5),
                uvage.from_color(590, 290, "yellow", 5, 5),
                uvage.from_color(590, 350, "yellow", 5, 5),
                uvage.from_color(590, 390, "yellow", 5, 5),
                uvage.from_color(590, 470, "yellow", 5, 5),
                uvage.from_color(590, 530, "yellow", 5, 5),
                uvage.from_color(590, 590, "yellow", 5, 5),
                uvage.from_color(550, 30, "yellow", 5, 5),
                uvage.from_color(550, 70, "yellow", 5, 5),
                uvage.from_color(550, 110, "yellow", 5, 5),
                uvage.from_color(550, 170, "yellow", 5, 5),
                uvage.from_color(550, 230, "yellow", 5, 5),
                uvage.from_color(550, 290, "yellow", 5, 5),
                uvage.from_color(550, 350, "yellow", 5, 5),
                uvage.from_color(550, 410, "yellow", 5, 5),
                uvage.from_color(550, 470, "yellow", 5, 5),
                uvage.from_color(550, 530, "yellow", 5, 5),
                uvage.from_color(550, 590, "yellow", 5, 5),

                uvage.from_color(520, 30, "yellow", 5, 5),
                uvage.from_color(520, 230, "yellow", 5, 5),
                uvage.from_color(520, 290, "yellow", 5, 5),
                uvage.from_color(520, 470, "yellow", 5, 5),
                uvage.from_color(490, 30, "yellow", 5, 5),
                uvage.from_color(490, 70, "yellow", 5, 5),
                uvage.from_color(490, 110, "yellow", 5, 5),
                uvage.from_color(490, 150, "yellow", 5, 5),
                uvage.from_color(490, 190, "yellow", 5, 5),
                uvage.from_color(490, 230, "yellow", 5, 5),
                uvage.from_color(490, 270, "yellow", 5, 5),
                uvage.from_color(490, 310, "yellow", 5, 5),
                uvage.from_color(490, 350, "yellow", 5, 5),
                uvage.from_color(490, 410, "yellow", 5, 5),
                uvage.from_color(490, 470, "yellow", 5, 5),
                uvage.from_color(490, 510, "yellow", 5, 5),
                uvage.from_color(490, 550, "yellow", 5, 5),
                uvage.from_color(490, 590, "yellow", 5, 5),
                uvage.from_color(460, 30, "yellow", 5, 5),
                uvage.from_color(460, 90, "yellow", 5, 5),
                uvage.from_color(460, 230, "yellow", 5, 5),
                uvage.from_color(460, 350, "yellow", 5, 5),
                uvage.from_color(460, 410, "yellow", 5, 5),
                uvage.from_color(460, 470, "yellow", 5, 5),
                uvage.from_color(460, 590, "yellow", 5, 5),
                uvage.from_color(430, 30, "yellow", 5, 5),
                uvage.from_color(430, 90, "yellow", 5, 5),
                uvage.from_color(430, 130, "yellow", 5, 5),
                uvage.from_color(430, 170, "yellow", 5, 5),
                uvage.from_color(430, 230, "yellow", 5, 5),
                uvage.from_color(430, 350, "yellow", 5, 5),
                uvage.from_color(430, 410, "yellow", 5, 5),
                uvage.from_color(430, 470, "yellow", 5, 5),
                uvage.from_color(430, 530, "yellow", 5, 5),
                uvage.from_color(430, 590, "yellow", 5, 5),

                uvage.from_color(310, 30, "yellow", 5, 5),
                uvage.from_color(310, 70, "yellow", 5, 5),
                uvage.from_color(310, 110, "yellow", 5, 5),
                uvage.from_color(310, 150, "yellow", 5, 5),
                uvage.from_color(310, 190, "yellow", 5, 5),
                uvage.from_color(310, 230, "yellow", 5, 5),
                uvage.from_color(310, 270, "yellow", 5, 5),
                uvage.from_color(310, 310, "yellow", 5, 5),
                uvage.from_color(310, 350, "yellow", 5, 5),
                uvage.from_color(310, 410, "yellow", 5, 5),
                uvage.from_color(310, 470, "yellow", 5, 5),
                uvage.from_color(310, 510, "yellow", 5, 5),
                uvage.from_color(310, 550, "yellow", 5, 5),
                uvage.from_color(310, 590, "yellow", 5, 5),
                uvage.from_color(340, 30, "yellow", 5, 5),
                uvage.from_color(340, 90, "yellow", 5, 5),
                uvage.from_color(340, 230, "yellow", 5, 5),
                uvage.from_color(340, 350, "yellow", 5, 5),
                uvage.from_color(340, 410, "yellow", 5, 5),
                uvage.from_color(340, 470, "yellow", 5, 5),
                uvage.from_color(340, 590, "yellow", 5, 5),
                uvage.from_color(370, 30, "yellow", 5, 5),
                uvage.from_color(370, 90, "yellow", 5, 5),
                uvage.from_color(370, 130, "yellow", 5, 5),
                uvage.from_color(370, 170, "yellow", 5, 5),
                uvage.from_color(370, 230, "yellow", 5, 5),
                uvage.from_color(370, 350, "yellow", 5, 5),
                uvage.from_color(370, 410, "yellow", 5, 5),
                uvage.from_color(370, 470, "yellow", 5, 5),
                uvage.from_color(370, 530, "yellow", 5, 5),
                uvage.from_color(370, 590, "yellow", 5, 5),

                uvage.from_color(150, 30, "yellow", 5, 5),
                uvage.from_color(150, 70, "yellow", 5, 5),
                uvage.from_color(150, 110, "yellow", 5, 5),
                uvage.from_color(150, 150, "yellow", 5, 5),
                uvage.from_color(150, 190, "yellow", 5, 5),
                uvage.from_color(150, 230, "yellow", 5, 5),
                uvage.from_color(150, 270, "yellow", 5, 5),
                uvage.from_color(150, 310, "yellow", 5, 5),
                uvage.from_color(150, 350, "yellow", 5, 5),
                uvage.from_color(150, 390, "yellow", 5, 5),
                uvage.from_color(150, 430, "yellow", 5, 5),
                uvage.from_color(150, 470, "yellow", 5, 5),
                uvage.from_color(150, 510, "yellow", 5, 5),
                uvage.from_color(150, 550, "yellow", 5, 5),
                uvage.from_color(150, 590, "yellow", 5, 5),
                uvage.from_color(180, 30, "yellow", 5, 5),
                uvage.from_color(180, 110, "yellow", 5, 5),
                uvage.from_color(180, 230, "yellow", 5, 5),
                uvage.from_color(180, 350, "yellow", 5, 5),
                uvage.from_color(180, 470, "yellow", 5, 5),
                uvage.from_color(180, 590, "yellow", 5, 5),
                uvage.from_color(210, 30, "yellow", 5, 5),
                uvage.from_color(210, 110, "yellow", 5, 5),
                uvage.from_color(210, 170, "yellow", 5, 5),
                uvage.from_color(210, 230, "yellow", 5, 5),
                uvage.from_color(210, 290, "yellow", 5, 5),
                uvage.from_color(210, 350, "yellow", 5, 5),
                uvage.from_color(210, 390, "yellow", 5, 5),
                uvage.from_color(210, 470, "yellow", 5, 5),
                uvage.from_color(210, 530, "yellow", 5, 5),
                uvage.from_color(210, 590, "yellow", 5, 5),
                uvage.from_color(250, 30, "yellow", 5, 5),
                uvage.from_color(250, 70, "yellow", 5, 5),
                uvage.from_color(250, 110, "yellow", 5, 5),
                uvage.from_color(250, 170, "yellow", 5, 5),
                uvage.from_color(250, 230, "yellow", 5, 5),
                uvage.from_color(250, 290, "yellow", 5, 5),
                uvage.from_color(250, 350, "yellow", 5, 5),
                uvage.from_color(250, 410, "yellow", 5, 5),
                uvage.from_color(250, 470, "yellow", 5, 5),
                uvage.from_color(250, 530, "yellow", 5, 5),
                uvage.from_color(250, 590, "yellow", 5, 5),
                uvage.from_color(280, 30, "yellow", 5, 5),
                uvage.from_color(280, 230, "yellow", 5, 5),
                uvage.from_color(280, 290, "yellow", 5, 5),
                uvage.from_color(280, 470, "yellow", 5, 5),

            ]
            p1 = uvage.from_image(400, 550, "smiley.png")
            p1.scale_by(.026)

            ghost1 = uvage.from_image(400, 230, "ghost.png")
            ghost1.scale_by(.034)

            ghost2 = uvage.from_image(400, 230, "ghost.png")
            ghost2.scale_by(.034)

            ghost3 = uvage.from_image(400, 230, "ghost.png")
            ghost3.scale_by(.034)

            ghost4 = uvage.from_image(400, 230, "ghost.png")
            ghost4.scale_by(.034)

            ghost5 = uvage.from_image(400, 230, "ghost.png")
            ghost5.scale_by(.034)

            ghost6 = uvage.from_image(400, 230, "ghost.png")
            ghost6.scale_by(.034)

            ghosts = [
                ghost1,
                ghost2,
                ghost3,
                ghost4,
                ghost5,
                ghost6
            ]
            for coin in coins:
                camera.draw(coin)
            for ghost in ghosts:
                camera.draw(ghost)
            game_on = True

    camera.display()



uvage.timer_loop(30, tick)