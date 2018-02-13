import pygame_textinput,pygame,font

class Textbox():
    """class for making textboxes in which data can be input using the pygame_textinput module"""
    def __init__(self,surface,size=20,char=20,boxcolour=(255,255,255),textcolour=(0,0,0),font_type="LiberationMono"):
        self.size = size
        self.textcolour = textcolour
        self.boxcolour = boxcolour
        self.surface = surface
        self.xlen = char*0.6*size
        self.char= char
        self.ylen = size
        self.font_type = font_type
        self.textinput = pygame_textinput.TextInput(self.font_type,self.size,True,self.textcolour)


    def make(self,x0pos,y0pos,events):
        """ makes the box on the surface"""
        # getting mouse game input
        x, y = pygame.mouse.get_pos()

        # converting placment reference point from the center of the screen to the top left hand corner
        xpos = (1920/2) - (self.xlen/2) + x0pos
        ypos = (1010 / 2) - (self.ylen/ 2) + y0pos


        # draws a rectangle
        pygame.draw.rect(self.surface, self.boxcolour, (xpos, ypos, self.xlen, self.ylen))
        if x > xpos and x < xpos + self.xlen and y > ypos and y < ypos + self.ylen:
            self.textinput.update(events)
        string = self.textinput.get_text()
        if len(string) <= self.char:
            self.surface.blit(self.textinput.get_surface(),(xpos,ypos))
        else:
            font.TextToScreen(self.surface,string[0:self.char],x0pos,y0pos,self.size,self.textcolour)

        return string

    def makepass(self,x0pos,y0pos,events):

        x, y = pygame.mouse.get_pos()

        xpos = (1920/2) - (self.xlen/2) + x0pos
        ypos = (1010 / 2) - (self.ylen/ 2) + y0pos



        pygame.draw.rect(self.surface, self.boxcolour, (xpos, ypos, self.xlen, self.ylen))
        if x > xpos and x < xpos + self.xlen and y > ypos and y < ypos + self.ylen:
            self.textinput.update(events)
        string = self.textinput.get_text()
        aster = Textbox.ast(self,string)
        if len(string) <= self.char:

            font.TextToScreen(self.surface,aster,x0pos,y0pos,self.size,self.textcolour)
        else:
            font.TextToScreen(self.surface,aster[0:self.char],x0pos,y0pos,self.size,self.textcolour)

        return string


    def ast(self,string):
        ast = ""
        for i in range(len(string)):
            ast = ast + "*"

        return ast


