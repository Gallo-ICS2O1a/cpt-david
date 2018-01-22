set1_speed = 75
set2_speed = -525
horizontal_move = 200
player_movement = 5
vertical_jump = 100
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
store_score = [0]
screen = 0


def setup():
    size(700, 675)


def keyReleased():
    global set1_speed
    global set2_speed
    global vertical_jump
    global score
    if keyCode == 38:
        set1_speed += vertical_jump
        set2_speed += vertical_jump
        if vertical_jump == 100:
            score += 1
            store_score.append(score)


def keyPressed():
    global horizontal_move
    global player_movement
    if keyCode == 37:
        horizontal_move -= player_movement
    if keyCode == 39:
        horizontal_move += player_movement


def draw():
    global set1_speed
    global set2_speed
    global horizontal_move
    global player_movement
    global vertical_jump
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
    global score
    global screen
    noStroke()

# MAIN MENU
    if screen == 0:
        background(0, 160, 129)
        fill(255)
        ellipse(350, 178, 225, 225)
        stroke(0)
        ellipse(315, 150, 50, 75)
        ellipse(385, 150, 50, 75)
        fill(0)
        ellipse(315, 150, 30, 45)
        ellipse(385, 150, 30, 45)
        arc(350, 215, 80, 80, 0, PI, CHORD)

        noStroke()
        # TITLE
        fill(255)
        textSize(100)
        textAlign(CENTER)
        text("BALL JUMP", 350, 400)

        # PLAY BUTTON
        fill(4, 98, 107)
        rect(250, 450, 200, 50)
        fill(255)
        textSize(35)
        textAlign(CENTER)
        text("PLAY", 350, 485)
        if 250 <= pmouseX <= 450 and 450 <= pmouseY <= 500 and screen == 0:
            if mousePressed:
                screen = 1

        # INSTRUCTIONS BUTTON
        fill(4, 98, 107)
        rect(250, 550, 200, 50)
        fill(255)
        textSize(27)
        textAlign(CENTER)
        text("INSTRUCTIONS", 350, 585)
        if 250 <= pmouseX <= 450 and 550 <= pmouseY <= 600 and screen == 0:
            if mousePressed:
                screen = 2

# GAME SCREEN
    if screen == 1:
        # LEVELS
        noStroke()
        rec1_y = set1_speed
        rec2_y = 100 + set1_speed
        rec3_y = 200 + set1_speed
        rec4_y = 300 + set1_speed
        rec5_y = 400 + set1_speed
        rec6_y = 500 + set1_speed

    # CHARACTER
        rec7_y = set2_speed
        rec8_y = 100 + set2_speed
        rec9_y = 200 + set2_speed
        rec10_y = 300 + set2_speed
        rec11_y = 400 + set2_speed
        rec12_y = 500 + set2_speed
        background(251, 99, 0)

    # INFO SCREEN

        fill(0, 160, 129)
        rect(400, 0, 300, 675)
        textSize(40)
        textAlign(CENTER)
        text("BALL JUMP", 550, 300)
        textSize(30)
        text("Score:", 550, 350)

        fill(255)
        ellipse(550, 128, 225, 225)
        stroke(0)
        ellipse(515, 100, 50, 75)
        ellipse(585, 100, 50, 75)
        fill(0)
        ellipse(515, 100, 30, 45)
        ellipse(585, 100, 30, 45)
        arc(550, 165, 80, 80, 0, PI, CHORD)

    # PLAYER
        noStroke()
        fill(255)
        horizontal_move = constrain(horizontal_move, 25, 375)
        ellipse(horizontal_move, 550, 50, 50)

    # LEVELS
        fill(4, 98, 107)
        rect(10, rec1_y, 380, 25)
        rect(10, rec3_y, 380, 25)
        rect(10, rec5_y, 380, 25)
        rect(10, rec7_y, 380, 25)
        rect(10, rec9_y, 380, 25)
        rect(10, rec11_y, 380, 25)

        fill(66, 162, 171)
        rect(10, rec2_y, 380, 25)
        rect(10, rec4_y, 380, 25)
        rect(10, rec6_y, 380, 25)
        rect(10, rec8_y, 380, 25)
        rect(10, rec10_y, 380, 25)
        rect(10, rec12_y, 380, 25)

    # LOOP LEVELS
        if set1_speed >= 675:
            set1_speed = -525

        if set2_speed >= 675:
            set2_speed = -525

    # MONSTERS
        fill(0, 57, 44)
        rect(mons1_spawn, rec1_y - mons_size, mons_size, mons_size)
        mons1_spawn += mons1_move
        if mons1_spawn >= 400 - mons_size:
            mons1_move = -mons1_move
            mons1_spawn += mons1_move
        elif mons1_spawn <= 0:
            mons1_move = - mons1_move
            mons1_spawn += mons1_move

        rect(mons2_spawn, rec3_y - mons_size, mons_size, mons_size)
        mons2_spawn += mons2_move
        if mons2_spawn >= 400 - mons_size:
            mons2_move = -mons2_move
            mons2_spawn += mons2_move
        elif mons2_spawn <= 0:
            mons2_move = -mons2_move
            mons2_spawn += mons2_move

        rect(mons3_spawn, rec5_y - mons_size, mons_size, mons_size)
        mons3_spawn += mons3_move
        if mons3_spawn >= 400 - mons_size:
            mons3_move = -mons3_move
            mons3_spawn += mons3_move
        elif mons3_spawn <= 0:
            mons3_move = -mons3_move
            mons3_spawn += mons3_move

        rect(mons4_spawn, rec11_y - mons_size, mons_size, mons_size)
        mons4_spawn += mons4_move
        if mons4_spawn >= 400 - mons_size:
            mons4_move = -mons4_move
            mons4_spawn += mons4_move
        elif mons4_spawn <= 0:
            mons4_move = -mons4_move
            mons4_spawn += mons4_move

        rect(mons5_spawn, rec9_y - mons_size, mons_size, mons_size)
        mons5_spawn += mons5_move
        if mons5_spawn >= 400 - mons_size:
            mons5_move = -mons5_move
            mons5_spawn += mons5_move
        elif mons5_spawn <= 0:
            mons5_move = -mons5_move
            mons5_spawn += mons5_move
        rect(mons6_spawn, rec7_y - mons_size, mons_size, mons_size)
        mons6_spawn += mons6_move
        if mons6_spawn >= 400 - mons_size:
            mons6_move = -mons6_move
            mons6_spawn += mons6_move
        elif mons6_spawn <= 0:
            mons6_move = -mons6_move
            mons6_spawn += mons6_move

    # MONS1 COLLISION CHECK
        horizontal1_collision = mons1_spawn - horizontal_move
        height1_distance = 575 - rec1_y
        if -75 <= horizontal1_collision <= 25:
            if -25 <= height1_distance <= 75:
                mons1_move = 0
                mons2_move = 0
                mons3_move = 0
                mons4_move = 0
                mons5_move = 0
                mons6_move = 0
                vertical_jump = 0
                player_movement = 0
                text("GAME OVER", 200, 300)

    # MONS2 COLLISION CHECK
        horizontal2_collision = mons2_spawn - horizontal_move
        height2_distance = 575 - rec3_y
        if -75 <= horizontal2_collision <= 25:
            if -25 <= height2_distance <= 75:
                mons1_move = 0
                mons2_move = 0
                mons3_move = 0
                mons4_move = 0
                mons5_move = 0
                mons6_move = 0
                vertical_jump = 0
                player_movement = 0
                text("GAME OVER", 200, 300)

    # MONS3 COLLISION CHECK
        horizontal3_collision = mons3_spawn - horizontal_move
        height3_distance = 575 - rec5_y
        if -75 <= horizontal3_collision <= 25:
            if -25 <= height3_distance <= 75:
                mons1_move = 0
                mons2_move = 0
                mons3_move = 0
                mons4_move = 0
                mons5_move = 0
                mons6_move = 0
                vertical_jump = 0
                player_movement = 0
                text("GAME OVER", 200, 300)

    # MONS4 COLLISION CHECK
        horizontal4_collision = mons4_spawn - horizontal_move
        height4_distance = 575 - rec11_y
        if -75 <= horizontal4_collision <= 25:
            if -25 <= height4_distance <= 75:
                mons1_move = 0
                mons2_move = 0
                mons3_move = 0
                mons4_move = 0
                mons5_move = 0
                mons6_move = 0
                vertical_jump = 0
                player_movement = 0
                text("GAME OVER", 200, 300)

    # MONS5 COLLISION CHECK
        horizontal5_collision = mons5_spawn - horizontal_move
        height5_distance = 575 - rec9_y
        if -75 <= horizontal5_collision <= 25:
            if -25 <= height5_distance <= 75:
                mons1_move = 0
                mons2_move = 0
                mons3_move = 0
                mons4_move = 0
                mons5_move = 0
                mons6_move = 0
                vertical_jump = 0
                player_movement = 0
                text("GAME OVER", 200, 300)

    # MONS6 COLLISION CHECK
        horizontal6_collision = mons6_spawn - horizontal_move
        height6_distance = 575 - rec7_y
        if -75 <= horizontal6_collision <= 25:
            if -25 <= height6_distance <= 75:
                mons1_move = 0
                mons2_move = 0
                mons3_move = 0
                mons4_move = 0
                mons5_move = 0
                mons6_move = 0
                vertical_jump = 0
                player_movement = 0
                text("GAME OVER", 200, 300)

    # TITLE AND INFO
        textSize(40)
        textAlign(CENTER)
        text("BALL JUMP", 550, 300)
        textSize(30)
        text("Score: " + str(score), 550, 350)

    # TRY AGAIN BUTTON
        fill(4, 98, 107)
        if vertical_jump == 0 and player_movement == 0:
            rect(475, 525, 150, 50)
            fill(255)
            textSize(25)
            textAlign(CENTER)
            text("TRY AGAIN", 550, 557)

        if 475 <= mouseX <= 625 and 525 <= mouseY <= 575:
            if mousePressed and vertical_jump == 0:
                set1_speed = 75
                set2_speed = -525
                vertical_jump = 100
                player_movement = 5
                mons1_move = random(1, 5)
                mons2_move = random(1, 5)
                mons3_move = random(1, 5)
                mons4_move = random(1, 5)
                mons5_move = random(1, 5)
                mons6_move = random(1, 5)
                score = 0

    # HIGHSCORE
        if max(store_score) > 0:
            fill(0, 57, 44)
            textSize(25)
            textAlign(CENTER)
            text("HIGHSCORE: " + (str(max(store_score))), 550, 392)

    # BACK TO MAIN MENU
        fill(4, 98, 107)
        rect(450, 450, 200, 50)
        fill(255)
        textSize(25)
        textAlign(CENTER)
        text("MENU", 550, 485)
        if 450 <= pmouseX <= 650 and 450 <= pmouseY <= 500 and screen == 1:
            if mousePressed:
                screen = 0

    if screen == 2:
        background(0, 160, 129)
        fill(255)
        textSize(25)
        textAlign(CENTER)
        text("""             Welcome to Ball Jump!
             To play, use the arrow keys to move.
             Avoid the moving square monsters.
             Good Luck!""", 310, 300)
        fill(255)
        ellipse(350, 128, 225, 225)
        stroke(0)
        ellipse(315, 100, 50, 75)
        ellipse(385, 100, 50, 75)
        fill(0)
        ellipse(315, 100, 30, 45)
        ellipse(385, 100, 30, 45)
        arc(350, 165, 80, 80, 0, PI, CHORD)

        # MENU BUTTON
        noStroke()
        fill(4, 98, 107)
        rect(250, 500, 200, 50)
        fill(255)
        textSize(35)
        textAlign(CENTER)
        text("MENU", 350, 535)
        if 250 <= pmouseX <= 450 and 500 <= pmouseY <= 550 and screen == 2:
            if mousePressed:
                screen = 0
