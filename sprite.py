import pgzrun
WIDTH =800
HEIGHT = 600

def draw():
    screen.fill('BLUE')
    player.draw()

    screen.draw.line((0,300),(799,300), 'WHITE')
    screen.draw.line((400,0),(400,599), 'WHITE')
    screen.draw.text('ANGLE = ' + str(player.angle),(50,80))

def update():
    global player
    player.angle += 1

player = Actor('p1_walk03.png',(400,300))

pgzrun.go()