#graph.py
import pygame,font

class Graph:
    """class used to create a graph and place it on the screen"""
    def __init__(self,surface,length,height,x_array,y_array,x_label="x axis",y_label="y axis"):
        # defines initial variables
        self.surface = surface
        self.length = length
        self.height = height
        self.x_array = x_array
        self.y_array = y_array
        self.x_label = x_label
        self.y_label = y_label

    def draw_graph(self, xpos, ypos):
        """function that draws the graph and places it onto the page"""
        # checks that the x axis and y axis values are the same
        if len(self.x_array) == len(self.y_array):
            try:
                # finds the distance to place each point on the graph
                # from each other depending on the size of the array
                unit_x = self.length/len(self.x_array)
                unit_y = self.height/max(self.y_array)

                # draw axis
                pygame.draw.line(self.surface, (0, 0, 0), (xpos, ypos), (xpos + self.length, ypos), 2)
                pygame.draw.line(self.surface, (0, 0, 0), (xpos, ypos), (xpos, ypos - self.height), 2)
                # draws the x label
                font.TextToScreen(self.surface, str(self.x_label), (self.length / 2) + xpos, ypos + 10, 20, (0, 0, 0),
                                  1)
                # draws the y label
                font.TextToScreen(self.surface, str(self.y_label), xpos - 80, ypos - (self.height / 2), 20, (0, 0, 0),
                                  1)
                # draws the largest value on the graph x and y axis
                font.TextToScreen(self.surface, str(max(self.x_array)), xpos + self.length - 20, ypos, 20, (0, 0, 0), 1)
                font.TextToScreen(self.surface, str(max(self.y_array))[:3], xpos - 40, ypos - self.height, 20,
                                  (0, 0, 0), 1)

                # places each point on the graph
                for i in range(len(self.x_array)):
                    # calculates the placement of the graph
                    point_x = int(xpos + (unit_x * self.x_array[i]))
                    point_y = int(ypos - (unit_y * self.y_array[i]))

                    # draws a small rectangle in the calculated position position
                    pygame.draw.rect(self.surface, (0, 0, 0), (point_x - 5, point_y - 5, 10, 10))

            # if there isn't enough information to create a graph it prints an error
            except ZeroDivisionError:
                font.TextToScreen(self.surface,"No Data To Make Graph", xpos+(self.length/2),ypos - (self.height/2),40,
                                  (0,0,0),1)













