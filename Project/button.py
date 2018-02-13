#button.py
import pygame,time,font
pygame.init()


class Button:
    def __init__(self,surface,xlen=180,ylen=60,textsize = 60,colour1=(244,164,96),colour2=(255,228,196),colour3=(255,239,213),textcol = (255,255,255), textcol2=(244,164,96)):
        self.xlen = xlen
        self.ylen = ylen
        self.textsize = textsize
        self.colour1 = colour1
        self.colour2 = colour2
        self.colour3 = colour3
        self.surface = surface
        self.textcol = textcol
        self.textcol2 = textcol2
        self.up = False
        self.down = False


    def create(self,event,text="",x0pos=-860,y0pos=-460):
        """places the button on the screen and processes triggers
        returns true when button pressed"""

        # changes the point of reference from the top left hand corner to the center
        xpos = (1920/2) - (self.xlen/2) + x0pos
        ypos = (1010 / 2) - ( self.ylen/ 2) + y0pos

        # gets the mouse position
        x,y = pygame.mouse.get_pos()
        # draws a box to the screen in the first colour
        pygame.draw.rect(self.surface, self.colour1, (xpos, ypos, self.xlen, self.ylen))
        # draws the text over the box on the screen
        font.TextToScreen(self.surface, text, x0pos, y0pos, self.textsize, self.textcol)



        # when within the bounds of the box changes to colour 2
        if x > xpos and x < xpos + self.xlen and y > ypos and y < ypos + self.ylen:
            # draws the box with colour 2
            pygame.draw.rect(self.surface,self.colour2,(xpos,ypos,self.xlen,self.ylen))
            # draws the text over the top
            font.TextToScreen(self.surface, text, x0pos, y0pos, self.textsize, self.textcol2)
            hover = 1
        else:
            hover = 0

        # if pressed changes to colour 3 and makes the function return true
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.down = True

        elif event.type == pygame.MOUSEBUTTONUP:
            self.up = True

            if hover == 1:
                if self.down is True and self.up is True:
                    self.down = False
                    self.up = False
                    # draw the box with the third colour
                    pygame.draw.rect(self.surface, self.colour3,(xpos, ypos, self.xlen, self.ylen))
                    # draws the text over the top
                    font.TextToScreen(self.surface, text, x0pos, y0pos, self.textsize, self.textcol2)
                    print("button activated:",text)
                    # moves the mouse by 1 (gets rid of errors)
                    xmove = x + 1
                    ymove = y + 1
                    pygame.mouse.set_pos(xmove, ymove)

                    return True