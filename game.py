import pygame, time
import params, main, player, Level_01, street, workRoom, computerRoom, computerRoomV2
from config import cur, con
from moviepy.editor import *
from BrainRooms import brainRoom1, brainRoom2, brainRoom3, brainRoom4, brainRoom5

dialogRooms = [
    workRoom.NowLocation,
    computerRoom.NowLocation,
    computerRoomV2.NowLocation
]

def run():
    global walls, activator, NowLocation, NowLocationRect, NowLocationBase
    walls = Level_01.walls
    activator = Level_01.activator
    NowLocation = Level_01.NowLocation
    NowLocationRect = Level_01.NowLocationRect
    NowLocationBase = 'Level_01.NowLocation'
    newXPos = Level_01.newXPos
    newYPos = Level_01.newYPos
    dialog_window = []

    running = True
    while running:
        cur.execute(f"UPDATE PlayerPos SET location = '{NowLocationBase}'")
        cur.execute(f"UPDATE PlayerPos SET newXPos = {newXPos}")
        cur.execute(f"UPDATE PlayerPos SET newYPos = {newYPos}")
        con.commit()
        #print(f"'{NowLocationBase}' , {newXPos} , {newYPos}")
        # Держим цикл на правильной скорости
        main.clock.tick(params.FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_SPACE:
                    #dialog_start()
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        main.all_sprites.update()
        # Рендеринг

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    params.switch += 1
                if params.switch % 2 == 0:
                    params.for_spawn_dialog_window = True
                if params.switch % 2 == 1:
                    params.for_spawn_dialog_window = False

        PlayerY = player.Player.getY(main.player)
        PlayerX = player.Player.getX(main.player)
        activatorChecker = player.Player.activatorChecker(main.player)

        if PlayerY < 250 and NowLocation == Level_01.NowLocation:
            secretaryDialog = VideoFileClip(r'SecretaryDialog.mp4')
            secretaryDialog.preview()
            letter = VideoFileClip('Letter.mp4')
            letter.preview()
            nextDay = VideoFileClip('NextDay.mp4')
            nextDay.preview()
            time.sleep(0.1)

            NowLocation = street.NowLocation
            NowLocationRect = street.NowLocationRect
            NowLocationBase = 'street.NowLocation'
            walls = street.walls
            activator = street.activator
            newXPos = street.newXPos
            newYPos = street.newYPos

        if activatorChecker == True and NowLocation == street.NowLocation:
            NowLocation = workRoom.NowLocation
            NowLocationRect = workRoom.NowLocationRect
            NowLocationBase = 'workRoom.NowLocation'
            walls = workRoom.walls
            activator = workRoom.activator
            newXPos = workRoom.newXPos
            newYPos = workRoom.newYPos
            dialog_window = workRoom.dialog_window

        if PlayerY < 250 and NowLocation == workRoom.NowLocation:
            NowLocation = computerRoom.NowLocation
            NowLocationRect = computerRoom.NowLocationRect
            NowLocationBase = 'computerRoom.NowLocation'
            walls = computerRoom.walls
            activator = computerRoom.activator
            newXPos = computerRoom.newXPos
            newYPos = computerRoom.newYPos
            main.sprites_for_dialog = pygame.sprite.Group()
            dialog_window = computerRoom.dialog_window

        if activatorChecker == True:
            if PlayerX > 1050 and PlayerY > 650 and NowLocation == computerRoom.NowLocation:
                letterScene = VideoFileClip('letterScene.mp4')
                letterScene.preview()

                NowLocation = brainRoom1.NowLocation
                NowLocationRect = brainRoom1.NowLocationRect
                NowLocationBase = 'brainRoom1.NowLocation'
                walls = brainRoom1.walls
                activator = brainRoom1.activator
                newXPos = brainRoom1.newXPos
                newYPos = brainRoom1.newYPos

            elif NowLocation == brainRoom1.NowLocation:
                NowLocation = brainRoom2.NowLocation
                NowLocationRect = brainRoom2.NowLocationRect
                NowLocationBase = 'brainRoom2.NowLocation'
                walls = brainRoom2.walls
                activator = brainRoom2.activator
                newXPos = brainRoom2.newXPos
                newYPos = brainRoom2.newYPos

            elif NowLocation == brainRoom2.NowLocation:
                NowLocation = brainRoom3.NowLocation
                NowLocationRect = brainRoom3.NowLocationRect
                NowLocationBase = 'brainRoom3.NowLocation'
                walls = brainRoom3.walls
                activator = brainRoom3.activator
                newXPos = brainRoom3.newXPos
                newYPos = brainRoom3.newYPos

            elif NowLocation == brainRoom3.NowLocation:
                NowLocation = brainRoom4.NowLocation
                NowLocationRect = brainRoom4.NowLocationRect
                NowLocationBase = 'brainRoom4.NowLocation'
                walls = brainRoom4.walls
                activator = brainRoom4.activator
                newXPos = brainRoom4.newXPos
                newYPos = brainRoom4.newYPos

            elif NowLocation == brainRoom4.NowLocation:
                NowLocation = brainRoom5.NowLocation
                NowLocationRect = brainRoom5.NowLocationRect
                NowLocationBase = 'brainRoom5.NowLocation'
                walls = brainRoom5.walls
                activator = brainRoom5.activator
                newXPos = brainRoom5.newXPos
                newYPos = brainRoom5.newYPos

            elif NowLocation == brainRoom5.NowLocation:
                NowLocation = computerRoomV2.NowLocation
                NowLocationRect = computerRoomV2.NowLocationRect
                NowLocationBase = 'computerRoomV2.NowLocation'
                walls = computerRoomV2.walls
                activator = computerRoomV2.activator
                newXPos = computerRoomV2.newXPos
                newYPos = computerRoomV2.newYPos
                main.sprites_for_dialog = pygame.sprite.Group()
                dialog_window = computerRoom.dialog_window

        for i in range(0, len(walls)):
            main.all_sprites.add(walls[i])

        for i in range(0, len(activator)):
            main.all_sprites.add(activator[i])

        for i in range(0, len(dialog_window)):
            main.sprites_for_dialog.add(dialog_window[i])

        main.player.setWalls(walls)
        main.player.setActivator(activator)

        main.screen.blit(NowLocation, NowLocationRect)
        main.all_sprites.draw(main.screen)

        if activatorChecker == True:
            #if params.for_spawn_dialog_window == True:
            if NowLocation in dialogRooms:
                main.sprites_for_dialog.update()
                main.sprites_for_dialog.draw(main.screen)

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()