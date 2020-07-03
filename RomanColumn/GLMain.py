# ---------------------------------------------------------------------------------------------------------------------
# -                                                                                                                   -
# -                                        Project Name: Roman columns                                                -
# -                               Github: https://www.github.com/diamondcreeper098                                    -
# -                                                                                                                   -
# ---------------------------------------------------------------------------------------------------------------------
# The Import Section
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

# ----------------------------------------------------------------------------------------------------------------------
# the definitions section
screenWidth = 1280  # Window's Width
screenHeight = 720  # Window's Height
tileSize = 5        # Each Tile's Size (Tiles are Square)


# ----------------------------------------------------------------------------------------------------------------------
# function rectangle will draw rectangle
# y is reverse in OpenGL meaning that is from bottom to top
# 0 is the bottom of the screen and screenHeight is the top of the screen
def drawrectangle(_x, _y, _width, _height):
    x2 = _x + _width
    y2 = _y + _height
    glBegin(GL_QUADS)
    glVertex2f(_x, _y)  # The bottom left point
    glVertex2f(_x, y2)  # The top left point
    glVertex2f(x2, y2)  # The top right point
    glVertex2f(x2, _y)  # The bottom right point
    glEnd()


# ----------------------------------------------------------------------------------------------------------------------
# This section we will are going to make the Viewport
def iterate():
    glViewport(0, 0, screenWidth, screenHeight)              # Making the Viewport
    glMatrixMode(GL_PROJECTION)                              # Setting the matrix mode to GL_PROJECTION
    glLoadIdentity()                                         # Loading the default (clean) identity
    glOrtho(0.0, screenWidth, 0.0, screenHeight, 0.0, 1.0)   # Setting the Viewport to be Orthogonal
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# ----------------------------------------------------------------------------------------------------------------------
# This section will make a window and clear it


# showScreen function is for the screen related stuff
def showscreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clearing the screen
    glLoadIdentity()  # Reset the Graphics
    iterate()
    for i in range(0, int(screenHeight / tileSize)):
        for j in range(0, int(screenWidth / tileSize)):
            shades = math.sin(j / 10)
            glColor3f(shades, shades, shades)
            drawrectangle(j * tileSize, i * tileSize, tileSize, tileSize)
    glutSwapBuffers()


def main():
    # We are going to initialize a glut window with Color mode and size of screenWidth x screenHeight
    # And then show the window
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(screenWidth, screenHeight)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("OpenGL go brrrr")
    glutDisplayFunc(showscreen)
    glutIdleFunc(showscreen)
    glutMainLoop()


if __name__ == '__main__':
    main()
