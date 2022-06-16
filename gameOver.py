import pygame, time
import params, main, player, Level_01, street, workRoom, computerRoom, computerRoomV2, workRoomV2, computerRoomV3, officeRoom
from DoorRooms import DoorRoom01, DoorRoom02, DoorRoom03,DoorRoom04, DoorRoom05, DoorRoom06, DoorRoom07, DoorRoom08, DoorRoom09
from config import cur, con
from moviepy.editor import *
from BrainRooms import brainRoom1, brainRoom2, brainRoom3, brainRoom4, brainRoom5

def gameOverChecker():
    for row in cur.execute(f'SELECT location, xPos, yPos FROM PlayerPos'):
        NowLocation = row[0]
        PlayerX = row[1]
        PlayerY = row[2]
        if NowLocation == DoorRoom01.NowLocation:
            if PlayerX > params.WIDTH / (params.WIDTH / 90) and PlayerX < params.WIDTH / (params.WIDTH / 300) and PlayerY < params.HEIGHT / (params.HEIGHT / 715) and PlayerY > params.HEIGHT / (params.HEIGHT / 625):
                return True