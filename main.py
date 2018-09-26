from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys


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
    gluOrtho2D(-1000, w, -1000, h)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def display():

    rgb1 = 26 / 255
    rgb2 = rgb1

    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINE_LOOP)
    glColor3f(rgb1, rgb2, 1.0)
    glVertex2f(900, 450)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2i(250, 150)
    glColor3f(0.43, 0.43, 1.0)
    glVertex2i(300, 180)
    glColor3f(0.43, 0.43, 1.0)
    glVertex2i(500, 700)
    glColor3f(0.43, 0.43, 1.0)
    glVertex2i(250, 150)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(550, 150)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2i(550, 450)
    glEnd()
    glutSwapBuffers()


main()
