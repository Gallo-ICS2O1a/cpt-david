rec_speed = 100
horizontal_move = 200
movement = 5
mons_size = 50
mons1_move = random(1, 5)
mons2_move = random(1, 5)
mons3_move = random(1, 5)
mons1_spawn = random (mons_size/2, 400-mons_size/2)
mons2_spawn = random (mons_size/2, 400-mons_size/2)
mons3_spawn = random (mons_size/2, 400-mons_size/2)

def setup():
    size(400, 700)
def keyReleased():
    global rec_speed
    if keyCode==38:
        rec_speed+=100
    if keyCode==40:
        rec_speed-=100
    

def keyPressed(): 
    global horizontal_move
    global movement
    if keyCode==37:rec_speed=100
2
horizontal_move=200
3
movement=5
4
​
5
def setup():
6
    size(400, 700)
7
def keyReleased():
8
    global rec_speed
9
    if keyCode==38:
10
        rec_speed+=100
11
​
12
def keyPressed(): 
13
    global horizontal_move
14
    global movement
15
    if keyCode==37:
16
        horizontal_move-=movement
17
    if keyCode==39:
18
        horizontal_move+=movement
19
    
20
        
21
def draw():
22
    global rec_speed
23
    global horizontal_move
24
    global movement
25
    
26
    rec1_y=rec_speed
27
    rec2_y=100+rec_speed
28
    rec3_y=200+rec_speed
29
    rec4_y=300+rec_speed
30
    rec5_y=400+rec_speed
31
    rec6_y=500+rec_speed
32
    
33
    background(0)
34
        
35
    #PLAYER
36
    fill(255)
37
    ellipse(horizontal_move,575, 50, 50)
38
​
39
    #LEVELS
40
    fill(255, 0, 0)
41
    rect (10, rec1_y, 380, 25)
42
    rect (10, rec3_y, 380, 25)
43
    rect (10, rec5_y, 380, 25)
44
    
45
    fill(0, 255, 0)
46
    rect (10, rec2_y, 380, 25)
47
    rect (10, rec4_y, 380, 25)
48
    rect (10, rec6_y, 380, 25)
        horizontal_move-=movement
    if keyCode==39:
        horizontal_move+=movement
    
        
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
    
    rec1_y=rec_speed
    rec2_y=100+rec_speed
    rec3_y=200+rec_speed
    rec4_y=300+rec_speed
    rec5_y=400+rec_speed
    rec6_y=500+rec_speed
    
    background(0)
        
    #PLAYER
    fill(255)
    ellipse(horizontal_move,575, 50, 50)

    #LEVELS
    fill(255, 0, 0)
    rect (10, rec1_y, 380, 25)
    rect (10, rec3_y, 380, 25)
    rect (10, rec5_y, 380, 25)
    
    fill(0, 255, 0)
    rect (10, rec2_y, 380, 25)
    rect (10, rec4_y, 380, 25)
    rect (10, rec6_y, 380, 25)
    
    #MONSTERS
    rect (mons1_spawn, rec1_y-mons_size, mons_size, mons_size)
    mons1_spawn+=mons1_move
    if mons1_spawn >= width-mons_size:
        mons1_move= -mons1_move
        mons1_spawn+=mons1_move
    elif mons1_spawn <= 0:
        mons1_move=-mons1_move
        mons1_spawn+=mons1_move
    
    rect (mons2_spawn, rec3_y-mons_size, mons_size, mons_size)
    mons2_spawn+=mons2_move
    if mons2_spawn >= width-mons_size:
        mons2_move= -mons2_move
        mons2_spawn+=mons2_move
    elif mons2_spawn <= 0:
        mons2_move=-mons2_move
        mons2_spawn+=mons2_move
    
    rect (mons3_spawn, rec5_y-mons_size, mons_size, mons_size)
    mons3_spawn+=mons3_move
    if mons3_spawn >= width-mons_size:
        mons3_move= -mons3_move
        mons3_spawn+=mons3_move
    elif mons3_spawn <= 0:
        mons3_move=-mons3_move
        mons3_spawn+=mons3_move
    
