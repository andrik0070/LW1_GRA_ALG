from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
from math import cos, sin
from numpy import arange
from pprint import pprint

currentPoint = (0, 0)
points = []
moves = []


def main():
    with open('./data/1_3.txt') as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        point_number = int(content.pop(0))
        global points
        for point in content[:point_number]:
            points.append(tuple([int(coordinate) for coordinate in point.split(' ')]))
        del content[:point_number]

        content.pop(0)

        global moves
        for move in content:
            moves.append(int(move))

        pprint(points)
        pprint(moves)

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 150)
    glutCreateWindow("OpenGL lesson 3")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()


def move_to(point):
    global currentPoint
    currentPoint = point


def line_to(point):
    global currentPoint
    pprint(point)
    glBegin(GL_LINE_STRIP)
    glVertex2i(currentPoint[0], currentPoint[1])
    glVertex2i(point[0], point[1])
    glEnd()
    currentPoint = point


def display():
    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    glColor3d(1, 0, 0)

    global moves
    global points

    glEnable(GL_CLIP_PLANE0)
    glClipPlane(GL_CLIP_PLANE0, (-7500, 7500, 0, 0))

    for move in moves:
        if move < 0:
            move_to(points[abs(move) - 1])
        else:
            line_to(points[move - 1])
        glFlush()

    glDisable(GL_CLIP_PLANE0)


def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-500, 500, -500, 500)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


main()
