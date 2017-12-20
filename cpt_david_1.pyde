rec_speed = 100
horizontal_move = 200
movement = 5
mons_size = 50
mons1_move = random(1, 5)
mons2_move = random(1, 5)
mons3_move = random(1, 5)
mons1_spawn = random(mons_size/2, 400 - mons_size/2)
mons2_spawn = random(mons_size/2, 400 - mons_size/2)
mons3_spawn = random(mons_size/2, 400 - mons_size/2)


def setup():
    size(400, 700)


def keyReleased():
    global rec_speed
    if keyCode == 38:
        rec_speed += 100


def keyPressed():
    global horizontal_move
    global movement
    if keyCode == 37:
        horizontal_move -= movement
    if keyCode == 39:
        horizontal_move += movement


def draw():
    global rec_speed
    global horizontal_move
    global movement
    global mons_size
    global mons1_move
    global mons2_move
    global mons3_move
    global mons1_spawn
    global mons2_spawn
    global mons3_spawn

    rec1_y = rec_speed
    rec2_y = 100 + rec_speed
    rec3_y = 200 + rec_speed
    rec4_y = 300 + rec_speed
    rec5_y = 400 + rec_speed
    rec6_y = 500 + rec_speed

    background(0)

# PLAYER
    fill(255)
    ellipse(horizontal_move, 575, 50, 50)

# LEVELS
    fill(255, 0, 0)
    rect(10, rec1_y, 380, 25)
    rect(10, rec3_y, 380, 25)
    rect(10, rec5_y, 380, 25)

    fill(0, 255, 0)
    rect(10, rec2_y, 380, 25)
    rect(10, rec4_y, 380, 25)
    rect(10, rec6_y, 380, 25)

# LOOP LEVELS


# MONSTERS
    rect(mons1_spawn, rec1_y - mons_size, mons_size, mons_size)
    mons1_spawn += mons1_move
    if mons1_spawn >= width - mons_size:
        mons1_move = -mons1_move
        mons1_spawn += mons1_move
    elif mons1_spawn <= 0:
        mons1_move = - mons1_move
        mons1_spawn += mons1_move

    rect(mons2_spawn, rec3_y - mons_size, mons_size, mons_size)
    mons2_spawn += mons2_move
    if mons2_spawn >= width - mons_size:
        mons2_move = -mons2_move
        mons2_spawn += mons2_move
    elif mons2_spawn <= 0:
        mons2_move = -mons2_move
        mons2_spawn += mons2_move

    rect(mons3_spawn, rec5_y - mons_size, mons_size, mons_size)
    mons3_spawn += mons3_move
    if mons3_spawn >= width - mons_size:
        mons3_move = -mons3_move
        mons3_spawn += mons3_move
    elif mons3_spawn <= 0:
        mons3_move = -mons3_move
        mons3_spawn += mons3_move
