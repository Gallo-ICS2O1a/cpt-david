rec_speed=100
horizontal_move=200
movement=5

def setup():
    size(400, 700)
def keyReleased():
    global rec_speed
    if keyCode==38:
        rec_speed+=100

def keyPressed(): 
    global horizontal_move
    global movement
    if keyCode==37:
        horizontal_move-=movement
    if keyCode==39:
        horizontal_move+=movement
    
        
def draw():
    global rec_speed
    global horizontal_move
    global movement
    
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