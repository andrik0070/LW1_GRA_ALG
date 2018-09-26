from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
from math import cos, sin
from numpy import arange


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowSize(800, 600)
    glutCreateWindow("OpenGL lesson 1")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutMainLoop()


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-100, 100, -100, 100)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():
    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    glVertex2i(-100, 0)
    glVertex2i(100, 0)
    glVertex2i(0, -100)
    glVertex2i(0, 100)
    glEnd()

    glBegin(GL_LINE_STRIP)
    glColor3f(0, 0, 1)
    for x in arange(-100, 100, 0.5):
        y = abs(0.25 * x + 3 * cos(100 * x) * sin(x))
        glVertex2f(x, y)
    glEnd()

    glutSwapBuffers()


main()
