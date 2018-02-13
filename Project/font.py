import  pygame,os


class TextToScreen:
    """class which takes the text input of the user and blits it to the screen"""
    def __init__(self,screen, text, x=10 ,y=50, size = 60, colour = (0,0,0), centeringmethod=0):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.size = size
        self.colour = colour
        self.xc = (1920/2) - (len(self.text)*0.6*self.size/2) + self.x
        self.yc = (1010 / 2) - ( self.size/ 2) + self.y
        self.dir_path = os.path.dirname(os.path.realpath(__file__)) + "/" + "LiberationMono-Regular.ttf"
        try:
            self.text = str(self.text)
            # creates font object
            self.font = pygame.font.Font(self.dir_path,self.size)
            # creating text object
            self.text = self.font.render(self.text, True, self.colour)
            # gives the option to choose between placing with reference point from the top left hand corner
            # or from the center as a reference point
            if centeringmethod == 0:
                self.screen.blit(self.text,(self.xc,self.yc))
            else:
                self.screen.blit(self.text, (self.x, self.y))
        # if there happens to be an error it will raise an error
        except Exception:
            print("Font Error, saw it coming")
            raise Exception
