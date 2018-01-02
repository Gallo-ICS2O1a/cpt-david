rec1_speed = 75
rec2_speed = -525
horizontal_move = 200
movement = 5
mons_size = 50
mons1_move = random(1, 5)
mons2_move = random(1, 5)
mons3_move = random(1, 5)
mons4_move = random(1, 5)
mons5_move = random(1, 5)
mons6_move = random(1, 5)
mons1_spawn = random(mons_size, 400 - mons_size)
mons2_spawn = random(mons_size, 400 - mons_size)
mons3_spawn = random(mons_size, 400 - mons_size)
mons4_spawn = random(mons_size, 400 - mons_size)
mons5_spawn = random(mons_size, 400 - mons_size)
mons6_spawn = random(mons_size, 400 - mons_size)
score = 0
store_score = ""


def setup():
    size(400, 675)


def keyReleased():
    global rec1_speed
    global rec2_speed
    if keyCode == 38:
        rec1_speed += 100
        rec2_speed += 100


def keyPressed():
    global horizontal_move
    global movement
    if keyCode == 37:
        horizontal_move -= movement
    if keyCode == 39:
        horizontal_move += movement


def draw():
    global rec1_speed
    global rec2_speed
    global horizontal_move
    global movement
    global mons_size
    global mons1_move
    global mons2_move
    global mons3_move
    global mons4_move
    global mons5_move
    global mons6_move
    global mons1_spawn
    global mons2_spawn
    global mons3_spawn
    global mons4_spawn
    global mons5_spawn
    global mons6_spawn

# LEVELS
    rec1_y = rec1_speed
    rec2_y = 100 + rec1_speed
    rec3_y = 200 + rec1_speed
    rec4_y = 300 + rec1_speed
    rec5_y = 400 + rec1_speed
    rec6_y = 500 + rec1_speed

    rec7_y = rec2_speed
    rec8_y = 100 + rec2_speed
    rec9_y = 200 + rec2_speed
    rec10_y = 300 + rec2_speed
    rec11_y = 400 + rec2_speed
    rec12_y = 500 + rec2_speed
    background(0)

# PLAYER
    fill(255)
    ellipse(horizontal_move, 550, 50, 50)

# LEVELS
    fill(255, 0, 0)
    rect(10, rec1_y, 380, 25)
    rect(10, rec3_y, 380, 25)
    rect(10, rec5_y, 380, 25)
    rect(10, rec7_y, 380, 25)
    rect(10, rec9_y, 380, 25)
    rect(10, rec11_y, 380, 25)

    fill(0, 255, 0)
    rect(10, rec2_y, 380, 25)
    rect(10, rec4_y, 380, 25)
    rect(10, rec6_y, 380, 25)
    rect(10, rec8_y, 380, 25)
    rect(10, rec10_y, 380, 25)
    rect(10, rec12_y, 380, 25)

# LOOP LEVELS
    if rec1_speed >= 675:
        rec1_speed = -525
    if rec2_speed >= 675:
        rec2_speed = -525

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

    rect(mons4_spawn, rec11_y - mons_size, mons_size, mons_size)
    mons4_spawn += mons4_move
    if mons4_spawn >= width - mons_size:
        mons4_move = -mons4_move
        mons4_spawn += mons4_move
    elif mons4_spawn <= 0:
        mons4_move = -mons4_move
        mons4_spawn += mons4_move

    rect(mons5_spawn, rec9_y - mons_size, mons_size, mons_size)
    mons5_spawn += mons5_move
    if mons5_spawn >= width - mons_size:
        mons5_move = -mons5_move
        mons5_spawn += mons5_move
    elif mons5_spawn <= 0:
        mons5_move = -mons5_move
        mons5_spawn += mons5_move

    rect(mons6_spawn, rec7_y - mons_size, mons_size, mons_size)
    mons6_spawn += mons6_move
    if mons6_spawn >= width - mons_size:
        mons6_move = -mons6_move
        mons6_spawn += mons6_move
    elif mons6_spawn <= 0:
        mons6_move = -mons6_move
        mons6_spawn += mons6_move


# MONS1 COLLISION CHECK
    horizontal1_collision = mons1_spawn - horizontal_move
    height1_distance = 575 - rec1_y

# MONS2 COLLISION CHECK
    horizontal2_collision = mons2_spawn - horizontal_move
    height2_distance = 575 - rec3_y

# MONS3 COLLISION CHECK
    horizontal3_collision = mons3_spawn - horizontal_move
    height3_distance = 575 - rec5_y
