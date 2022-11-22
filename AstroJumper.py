import time
import thumby
import math
import random

while(1):

    # BITMAP: width: 40, height: 15
    astro = bytearray([0,240,240,252,254,230,230,230,230,252,0,0,254,130,130,130,130,0,0,2,2,254,2,2,0,0,254,130,130,130,254,0,0,254,2,2,2,254,0,0,
                0,7,7,63,63,15,15,15,63,63,0,0,32,32,32,32,63,0,0,0,0,63,0,0,0,0,63,1,3,12,48,0,0,63,32,32,32,63,0,0])
    # BITMAP: width: 45, height: 15
    stars = bytearray([0,0,0,8,0,42,0,8,0,0,0,0,132,14,4,0,0,0,0,64,64,0,88,0,64,64,0,0,0,0,0,0,16,0,0,0,0,0,0,0,10,4,10,0,0,
                0,0,16,40,16,0,0,0,0,0,2,2,13,2,2,0,0,0,0,0,0,0,3,0,0,0,0,0,1,0,0,0,17,0,0,0,1,0,0,0,0,0,0,0,0])
    
    
    # BITMAP: width: 45, height: 15
    jumper = bytearray([0,4,4,4,252,4,0,0,252,0,0,0,252,0,0,252,8,16,8,252,0,0,252,132,132,132,252,0,0,252,132,132,132,132,0,0,252,132,132,132,252,0,0,252,252,
                14,16,16,16,15,0,0,0,15,16,16,16,15,0,0,31,0,0,0,31,0,0,31,0,0,0,0,0,0,31,16,16,16,16,0,0,31,1,3,6,24,0,0,27,27])
    
    astroSprite = thumby.Sprite(40, 15, astro)
    stars1Sprite = thumby.Sprite(45, 15, stars)
    jumperSprite = thumby.Sprite(45, 15, jumper)
    astroSprite.x = 5
    stars1Sprite.x = 45
    jumperSprite.x = 20
    jumperSprite.y = 14
    
    
    # BITMAP: width: 8, height: 8
    # aButton = bytearray([0,60,70,106,106,70,60,0])
    
    # aButtonSprite = thumby.Sprite(8,8, aButton)
    # aButtonSprite.x = 8
    # aButtonSprite.y = 32
    
    #     # BITMAP: width: 8, height: 8
    # bitmap17 = bytearray([60,66,185,149,149,185,66,60])
    
    
    # BITMAP: width: 5, height: 8
    amogi= bytearray([28,254,59,59,254])
    
    # BITMAP: width: 8, height: 2
    platform = bytearray([3,3,3,3,3,3,3,3])
    
    # Make a sprite object using bytearray (a path to binary file from 'IMPORT SPRITE' is also valid)
    amogiSprite = thumby.Sprite(8, 8, amogi)
    
    platformSprite = thumby.Sprite(8, 2, platform)
    
    # Set the FPS (without this call, the default fps is 30)
    thumby.display.setFPS(60)
    
    amogiSprite.x = int((thumby.display.width/2) - (8/2))
    amogiSprite.y = int(thumby.display.height - 10)
    
    platformSprite.x = int((thumby.display.width/2) - (8/2))
    platformSprite.y = thumby.display.height - 2
    
    thumby.display.fill(0) # Fill canvas to black
    thumby.display.drawSprite(amogiSprite)
    thumby.display.drawSprite(platformSprite)
    thumby.display.drawSprite(astroSprite)
    thumby.display.drawSprite(stars1Sprite)
    thumby.display.drawSprite(jumperSprite)
    # thumby.display.drawSprite(aButtonSprite)
    thumby.display.update()
    
    while(1):
        t0 = time.ticks_ms()   # Get time (ms)
        
        bobRate = 150
        bobRange = 2
        
        bobOffset = math.sin(t0 / bobRate) * bobRange
        
        amogiSprite.y = int(thumby.display.height - 10) + bobOffset
        
        thumby.display.fill(0) # Fill canvas to black
        thumby.display.drawSprite(platformSprite)
        thumby.display.drawSprite(astroSprite)
        thumby.display.drawSprite(stars1Sprite)
        thumby.display.drawSprite(jumperSprite)
        thumby.display.drawSprite(amogiSprite)
        thumby.display.update()
        
        if (thumby.inputPressed() == True):
            print("start game!")
            break
    
    thumby.display.fill(0)
    
    bounceStart = time.ticks_ms()
    
    def bounce(start):
        global isFalling
        now = time.ticks_ms()
        x = ((now-start) / 150)
        if x >= 5:
            isFalling = True
        else:
            isFalling = False
        return -((x-5) ** 2) + 25
    
    
    def renderPlatforms(platforms):
        for i in range(0, len(platforms)):
            thumby.display.drawSprite(platforms[i])
    
    def checkPlatformJump(sprite, platforms):
        for platform in platforms:
            if (sprite.y >= platform.y - 7 and sprite.y <= platform.y and platform.x - 5 <= sprite.x <= platform.x + 5):
                return True
        return False
    
    def moveSpritesDown(sprites, stars, height):
        global lastMovement
        for sprite in sprites:
            sprite.y = sprite.y - (height - lastMovement)
            if sprite.y >= thumby.display.height:
                sprites.remove(sprite)
                newPlat = thumby.Sprite(8,2, platform)
                newPlat.x = random.randint(0, thumby.display.width - 8)
                newPlat.y = 0
                sprites.append(newPlat)
        for star in stars:
            star.y = star.y - (height - lastMovement) / 4
            if star.y >= thumby.display.height:
                sprites.remove(star)
                newStar = thumb.Sprite(45, 15, stars)
                rando = random.randint(0, thumby.display.width - 15)
                newStar.x = rando
                if (rando % 2 == 0):
                    newStar.mirrorX(1)
                if (rando % 3 == 0):
                    newStar.mirrorY(1)
                newStar.y = 0
                stars.append(newStar)
        lastMovement = height
                
        return
    
    isFalling = False
    totalScore = 0
    
    sprites = []
    starSprites = []
    amogiHeight = thumby.display.height - 10
    platforms = []
    
    
    lastMovement = 0
    
    for i in range(0, 4):
        platforms.append(thumby.Sprite(8,2,platform))
        platforms[i].x = i * 20
        platforms[i].y = i * 10
        sprites.append(platforms[i])
        starSprites.append(thumby.Sprite(45, 15, stars))
        starSprites[i].x = i * 20
        starSprites[i].y = i * 32 % thumby.display.height
    
    while(1):
        
        if (amogiSprite.y >= thumby.display.height + 15):
            break
        
        # Check if the amogi is bouncing on the first platformSprite
        if (amogiSprite.y >= platformSprite.y - 5 and platformSprite.x - 5 <= amogiSprite.x <= platformSprite.x + 5 ):
            bounceStart = time.ticks_ms()
            amogiHeight = amogiSprite.y
            lastMovement = 0
    
            
        # Check if the amogi bounces on an random platform
        if isFalling and (checkPlatformJump(amogiSprite, platforms)):
            bounceStart = time.ticks_ms()
            amogiHeight = amogiSprite.y
            lastMovement = 0
    
        # Move the amogi left or right
        if (thumby.buttonL.pressed()):
            newX = amogiSprite.x - 1
            if newX <= -4:
                amogiSprite.x = thumby.display.width - 8
            else:
                amogiSprite.x = newX
            amogiSprite.mirrorX = True
        if (thumby.buttonR.pressed()):
            newX = amogiSprite.x + 1
            if newX >= thumby.display.width - 4:
                amogiSprite.x = 0
            else:
                amogiSprite.x = newX
            amogiSprite.mirrorX = False
            
        # Get the bounce offset based on last jump
        bounceOffset = bounce(bounceStart)
        height = amogiHeight - bounceOffset
        
        # If the height of the amogi goes off the screen move the sprites down
        if height <= 0: 
            moveSpritesDown(platforms, starSprites, height)
            if not isFalling:
                amogiSprite.y = 0
        else:
            amogiSprite.y = height
            
            
        thumby.display.fill(0)
        renderPlatforms(platforms)
        thumby.display.drawSprite(amogiSprite)
        thumby.display.drawSprite(platformSprite)
        thumby.display.drawText(totalScore, 0, 0, 1)
        thumby.display.update()

    



