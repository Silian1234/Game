import pygame, random
import params, main, imports, player, dialogs, Level_01, DoorRoom01, LabirintRoom, street, workRoom
from moviepy.editor import *
from config import cur, con

def run():
    global walls, activator, NowLocation, NowLocationRect, NowLocationBase
    walls = Level_01.walls
    activator = Level_01.activator
    NowLocation = Level_01.NowLocation
    NowLocationRect = Level_01.NowLocationRect
    NowLocationBase = 'Level_01.NowLocation'
    newXPos = Level_01.newXPos
    newYPos = Level_01.newYPos

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

            NowLocation = street.NowLocation
            NowLocationRect = street.NowLocationRect
            NowLocationBase = 'street.NowLocation'
            walls = street.walls
            activator = street.activator
            newXPos = street.newXPos
            newYPos = street.newYPos

        if activatorChecker == True and NowLocation == Level_01.NowLocation:
            NowLocation = workRoom.NowLocation
            NowLocationRect = workRoom.NowLocationRect
            NowLocationBase = 'workRoom.NowLocation'
            walls = workRoom.walls
            activator = workRoom.activator
            newXPos = workRoom.newXPos
            newYPos = workRoom.newYPos

        for i in range(0, len(walls)):
            main.all_sprites.add(walls[i])

        for i in range(0, len(activator)):
            main.all_sprites.add(activator[i])

        main.player.setWalls(walls)
        main.player.setActivator(activator)

        main.screen.blit(NowLocation, NowLocationRect)
        main.all_sprites.draw(main.screen)

        if params.for_spawn_dialog_window == True:
            main.sprites_for_dialog.update()
            main.sprites_for_dialog.draw(main.screen)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    params.switch += 1
                if params.switch % 2 == 0:
                    params.for_spawn_dialog_window = True
                if params.switch % 2 == 1:
                    params.for_spawn_dialog_window = False

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()