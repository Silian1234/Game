import pygame, time, officeRoomV2, computerRoomV4, workRoomV3, undergroung, labirint1, undergroundV2, workRoomV4, computerRoomV5
import params, main, player, Level_01, street, workRoom, computerRoom, computerRoomV2, workRoomV2, computerRoomV3, officeRoom, bossRoom
from DoorRooms import DoorRoom01, DoorRoom02, DoorRoom03,DoorRoom04, DoorRoom05, DoorRoom06, DoorRoom07, DoorRoom08, DoorRoom09
from config import cur, con
from moviepy.editor import *
from BrainRooms import brainRoom1, brainRoom2, brainRoom3, brainRoom4, brainRoom5

leftWrongBrainRooms = [
    brainRoom1.NowLocation,
    brainRoom2.NowLocation,
    brainRoom4.NowLocation,
    brainRoom5.NowLocation
]

dialogRooms = [
    workRoom.NowLocation,
    computerRoom.NowLocation,
    computerRoomV2.NowLocation,
    workRoomV2.NowLocation,
    officeRoom.NowLocation,
    officeRoomV2.NowLocation,
    workRoomV3.NowLocation,
    workRoomV4.NowLocation,
    bossRoom.NowLocation
]

doorRooms = [
    DoorRoom01.NowLocation,
    DoorRoom02.NowLocation,
    DoorRoom03.NowLocation,
    DoorRoom04.NowLocation,
    DoorRoom05.NowLocation,
    DoorRoom06.NowLocation,
    DoorRoom07.NowLocation,
    DoorRoom08.NowLocation,
    DoorRoom09.NowLocation
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
    activatorV2 = Level_01.activator

    """labirintRulesScene = VideoFileClip('labirintRules.mp4')
    labirintRulesScene.preview()
    time.sleep(0.1)

    NowLocation = labirint1.NowLocation
    NowLocationRect = labirint1.NowLocationRect
    NowLocationBase = 'labirint1.NowLocation'
    walls = labirint1.walls
    activator = labirint1.activator
    newXPos = labirint1.newXPos
    newYPos = labirint1.newYPos
    main.sprites_for_dialog = pygame.sprite.Group()"""

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
        activatorCheckerV2 = player.Player.activatorCheckerV2(main.player)

        if PlayerY < params.HEIGHT / (1080 / 250) and NowLocation == Level_01.NowLocation:
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

        elif activatorChecker == True and NowLocation == street.NowLocation:
            NowLocation = workRoom.NowLocation
            NowLocationRect = workRoom.NowLocationRect
            NowLocationBase = 'workRoom.NowLocation'
            walls = workRoom.walls
            activator = workRoom.activator
            newXPos = workRoom.newXPos
            newYPos = workRoom.newYPos
            dialog_window = workRoom.dialog_window

        elif PlayerY < params.HEIGHT / (1080 / 250) and NowLocation == workRoom.NowLocation:
            NowLocation = computerRoom.NowLocation
            NowLocationRect = computerRoom.NowLocationRect
            NowLocationBase = 'computerRoom.NowLocation'
            walls = computerRoom.walls
            activator = computerRoom.activator
            newXPos = computerRoom.newXPos
            newYPos = computerRoom.newYPos
            main.sprites_for_dialog = pygame.sprite.Group()
            dialog_window = computerRoom.dialog_window

        elif PlayerX > params.WIDTH / (1920 / 1677) and PlayerY < params.HEIGHT / (1080 / 400) and NowLocation == computerRoomV2.NowLocation:
            NowLocation = workRoomV2.NowLocation
            NowLocationRect = workRoomV2.NowLocationRect
            NowLocationBase = 'workRoomV2.NowLocation'
            walls = workRoomV2.walls
            activator = workRoomV2.activator
            newXPos = workRoomV2.newXPos
            newYPos = workRoomV2.newYPos
            main.sprites_for_dialog = pygame.sprite.Group()
            dialog_window = workRoomV2.dialog_window

        elif PlayerX > params.WIDTH / (1920 / 400) and PlayerY < params.HEIGHT / (1080 / 328) and NowLocation == workRoomV2.NowLocation:
            NowLocation = computerRoomV3.NowLocation
            NowLocationRect = computerRoomV3.NowLocationRect
            NowLocationBase = 'computerRoomV3.NowLocation'
            walls = computerRoomV3.walls
            activator = computerRoomV3.activator
            newXPos = computerRoomV3.newXPos
            newYPos = computerRoomV3.newYPos
            main.sprites_for_dialog = pygame.sprite.Group()

        elif PlayerX > params.WIDTH / (1920 / 190) and PlayerY < params.HEIGHT / (1080 / 530) and NowLocation == officeRoom.NowLocation:
            secondRulesScene = VideoFileClip('SecondRules.mp4')
            secondRulesScene.preview()
            time.sleep(0.1)

            NowLocation = DoorRoom01.NowLocation
            NowLocationRect = DoorRoom01.NowLocationRect
            NowLocationBase = 'DoorRoom01.NowLocation'
            walls = DoorRoom01.walls
            activator = DoorRoom01.activator
            newXPos = DoorRoom01.newXPos
            newYPos = DoorRoom01.newXPos

            #заготовки для других комнат
            #если кнопка напротив 2 двери: 550 < PlayerY < 650 and 70 < PlayerX < 200
            #если кнопка напротив 2 двери: 550 < PlayerY < 650 and 570 < PlayerX < 700
            #если кнопка напротив 3 двери: 550 < PlayerY < 650 and 1070 < PlayerX < 1200
            #если кнопка напротив 4 двери: 550 < PlayerY < 650 and 1570 < PlayerX < 1700

        elif params.HEIGHT / (1080 / 550) < PlayerY < params.HEIGHT / (1080 / 650) and params.WIDTH / (1920 / 1070) < PlayerX < params.WIDTH / (1920 / 1200) and NowLocation == DoorRoom01.NowLocation:
            NowLocation = DoorRoom02.NowLocation
            NowLocationRect = DoorRoom02.NowLocationRect
            NowLocationBase = 'DoorRoom02.NowLocation'
            walls = DoorRoom02.walls
            activator = DoorRoom02.activator
            newXPos = DoorRoom01.newXPos
            newYPos = DoorRoom01.newXPos

        elif params.HEIGHT / (1080 / 550) < PlayerY < params.HEIGHT / (1080 / 650) and params.WIDTH / (1920 / 1570) < PlayerX < params.WIDTH / (1920 / 1700) and NowLocation == DoorRoom02.NowLocation:
            NowLocation = DoorRoom03.NowLocation
            NowLocationRect = DoorRoom03.NowLocationRect
            NowLocationBase = 'DoorRoom03.NowLocation'
            walls = DoorRoom03.walls
            activator = DoorRoom03.activator
            newXPos = DoorRoom01.newXPos
            newYPos = DoorRoom01.newXPos

        elif params.HEIGHT / (1080 / 550) < PlayerY < params.HEIGHT / (1080 / 650) and params.WIDTH / (1920 / 1570) < PlayerX < params.WIDTH / (1920 / 1700) and NowLocation == DoorRoom03.NowLocation:
            NowLocation = DoorRoom04.NowLocation
            NowLocationRect = DoorRoom04.NowLocationRect
            NowLocationBase = 'DoorRoom04.NowLocation'
            walls = DoorRoom04.walls
            activator = DoorRoom04.activator
            newXPos = DoorRoom01.newXPos
            newYPos = DoorRoom01.newXPos

        elif params.HEIGHT / (1080 / 550) < PlayerY < params.HEIGHT / (1080 / 650) and params.WIDTH / (1920 / 1070) < PlayerX < params.WIDTH / (1920 / 1200) and NowLocation == DoorRoom04.NowLocation:
            NowLocation = DoorRoom05.NowLocation
            NowLocationRect = DoorRoom05.NowLocationRect
            NowLocationBase = 'DoorRoom05.NowLocation'
            walls = DoorRoom05.walls
            activator = DoorRoom05.activator
            newXPos = DoorRoom01.newXPos
            newYPos = DoorRoom01.newXPos

        elif params.HEIGHT / (1080 / 550) < PlayerY < params.HEIGHT / (1080 / 650) and params.WIDTH / (1920 / 570) < PlayerX < params.WIDTH / (1920 / 700) and NowLocation == DoorRoom05.NowLocation:
            NowLocation = DoorRoom07.NowLocation
            NowLocationRect = DoorRoom07.NowLocationRect
            NowLocationBase = 'DoorRoom07.NowLocation'
            walls = DoorRoom07.walls
            activator = DoorRoom07.activator
            newXPos = DoorRoom01.newXPos
            newYPos = DoorRoom01.newXPos

        elif params.HEIGHT / (1080 / 550) < PlayerY < params.HEIGHT / (1080 / 650) and params.WIDTH / (1920 / 70) < PlayerX < params.WIDTH / (1920 / 200) and NowLocation == DoorRoom07.NowLocation:
            NowLocation = DoorRoom08.NowLocation
            NowLocationRect = DoorRoom08.NowLocationRect
            NowLocationBase = 'DoorRoom08.NowLocation'
            walls = DoorRoom08.walls
            activator = DoorRoom08.activator
            newXPos = DoorRoom01.newXPos
            newYPos = DoorRoom01.newXPos

        elif params.HEIGHT / (1080 / 550) < PlayerY < params.HEIGHT / (1080 / 650) and params.WIDTH / (1920 / 570) < PlayerX < params.WIDTH / (1920 / 700) and NowLocation == DoorRoom08.NowLocation:
            NowLocation = DoorRoom09.NowLocation
            NowLocationRect = DoorRoom09.NowLocationRect
            NowLocationBase = 'DoorRoom09.NowLocation'
            walls = DoorRoom09.walls
            activator = DoorRoom09.activator
            newXPos = DoorRoom01.newXPos
            newYPos = DoorRoom01.newXPos

        elif params.HEIGHT / (1080 / 550) < PlayerY < params.HEIGHT / (1080 / 650) and params.WIDTH / (1920 / 570) < PlayerX < params.WIDTH / (1920 / 700) and NowLocation == DoorRoom09.NowLocation:
            NowLocation = officeRoomV2.NowLocation
            NowLocationRect = officeRoomV2.NowLocationRect
            NowLocationBase = 'officeRoomV2.NowLocation'
            walls = officeRoomV2.walls
            activator = officeRoomV2.activator
            newXPos = officeRoomV2.newXPos
            newYPos = officeRoomV2.newYPos
            main.sprites_for_dialog = pygame.sprite.Group()
            dialog_window = officeRoomV2.dialog_window

        elif PlayerY > params.HEIGHT / (1080 / 1000) and NowLocation == officeRoomV2.NowLocation:
            NowLocation = computerRoomV4.NowLocation
            NowLocationRect = computerRoomV4.NowLocationRect
            NowLocationBase = 'computerRoomV4.NowLocation'
            walls = computerRoomV4.walls
            activator = computerRoomV4.activator
            newXPos = computerRoomV4.newXPos
            newYPos = computerRoomV4.newYPos
            main.sprites_for_dialog = pygame.sprite.Group()

        elif PlayerX < params.WIDTH / (1920 / 460) and PlayerY > params.HEIGHT / (1080 / 840) and NowLocation == workRoomV3.NowLocation:
            NowLocation = undergroung.NowLocation
            NowLocationRect = undergroung.NowLocationRect
            NowLocationBase = 'undergroung.NowLocation'
            walls = undergroung.walls
            activator = undergroung.activator
            newXPos = undergroung.newXPos
            newYPos = undergroung.newYPos
            main.sprites_for_dialog = pygame.sprite.Group()

        elif PlayerX < params.WIDTH / (1920 / 340) and PlayerY > params.HEIGHT / (1080 / 1015) and NowLocation == labirint1.NowLocation:
            NowLocation = undergroundV2.NowLocation
            NowLocationRect = undergroundV2.NowLocationRect
            NowLocationBase = 'undergroundV2.NowLocation'
            walls = undergroundV2.walls
            activator = undergroundV2.activator
            newXPos = undergroundV2.newXPos
            newYPos = undergroundV2.newYPos
            main.sprites_for_dialog = pygame.sprite.Group()

        elif PlayerX > params.WIDTH / (1920 / 400) and PlayerY < params.HEIGHT / (1080 / 328) and NowLocation == workRoomV4.NowLocation:
            NowLocation = computerRoomV5.NowLocation
            NowLocationRect = computerRoomV5.NowLocationRect
            NowLocationBase = 'computerRoomV5.NowLocation'
            walls = computerRoomV5.walls
            activator = computerRoomV5.activator
            newXPos = computerRoomV5.newXPos
            newYPos = computerRoomV5.newYPos
            main.sprites_for_dialog = pygame.sprite.Group()

        elif PlayerY > params.HEIGHT / (1080 / 1000) and NowLocation == bossRoom.NowLocation:
            finalVideo = VideoFileClip('finalVideo.mp4')
            finalVideo.preview()
            time.sleep(1)
            running = False

        if activatorChecker == True:
            if PlayerX > params.WIDTH / (1920 / 1050) and PlayerY > params.HEIGHT / (1080 / 650) and NowLocation == computerRoom.NowLocation:
                letterScene = VideoFileClip('letterScene.mp4')
                letterScene.preview()
                time.sleep(0.1)

                NowLocation = brainRoom1.NowLocation
                NowLocationRect = brainRoom1.NowLocationRect
                NowLocationBase = 'brainRoom1.NowLocation'
                walls = brainRoom1.walls
                activator = brainRoom1.activator
                activatorV2 = brainRoom1.activatorV2
                newXPos = brainRoom1.newXPos
                newYPos = brainRoom1.newYPos

            elif NowLocation == brainRoom1.NowLocation:
                NowLocation = brainRoom2.NowLocation
                NowLocationRect = brainRoom2.NowLocationRect
                NowLocationBase = 'brainRoom2.NowLocation'
                walls = brainRoom2.walls
                activator = brainRoom2.activator
                activatorV2 = brainRoom2.activatorV2
                newXPos = brainRoom2.newXPos
                newYPos = brainRoom2.newYPos

            elif NowLocation == brainRoom2.NowLocation:
                NowLocation = brainRoom3.NowLocation
                NowLocationRect = brainRoom3.NowLocationRect
                NowLocationBase = 'brainRoom3.NowLocation'
                walls = brainRoom3.walls
                activator = brainRoom3.activator
                activatorV2 = brainRoom3.activatorV2
                newXPos = brainRoom3.newXPos
                newYPos = brainRoom3.newYPos

            elif NowLocation == brainRoom3.NowLocation:
                NowLocation = brainRoom4.NowLocation
                NowLocationRect = brainRoom4.NowLocationRect
                NowLocationBase = 'brainRoom4.NowLocation'
                walls = brainRoom4.walls
                activator = brainRoom4.activator
                activatorV2 = brainRoom4.activatorV2
                newXPos = brainRoom4.newXPos
                newYPos = brainRoom4.newYPos

            elif NowLocation == brainRoom4.NowLocation:
                NowLocation = brainRoom5.NowLocation
                NowLocationRect = brainRoom5.NowLocationRect
                NowLocationBase = 'brainRoom5.NowLocation'
                walls = brainRoom5.walls
                activator = brainRoom5.activator
                activatorV2 = brainRoom5.activatorV2
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
                dialog_window = computerRoomV2.dialog_window

            elif NowLocation == computerRoomV3.NowLocation:
                NowLocation = officeRoom.NowLocation
                NowLocationRect = officeRoom.NowLocationRect
                NowLocationBase = 'officeRoom.NowLocation'
                walls = officeRoom.walls
                activator = officeRoom.activator
                newXPos = officeRoom.newXPos
                newYPos = officeRoom.newYPos
                main.sprites_for_dialog = pygame.sprite.Group()
                dialog_window = officeRoom.dialog_window

            elif NowLocation == computerRoomV4.NowLocation:
                NowLocation = workRoomV3.NowLocation
                NowLocationRect = workRoomV3.NowLocationRect
                NowLocationBase = 'workRoomV3.NowLocation'
                walls = workRoomV3.walls
                activator = workRoomV3.activator
                newXPos = workRoomV3.newXPos
                newYPos = workRoomV3.newYPos
                main.sprites_for_dialog = pygame.sprite.Group()
                dialog_window = workRoomV3.dialog_window

            elif NowLocation == undergroung.NowLocation:
                #labirintRulesScene = VideoFileClip('labirintRules.mp4')
                #labirintRulesScene.preview()
                #time.sleep(0.1)

                """NowLocation = labirint1.NowLocation
                NowLocationRect = labirint1.NowLocationRect
                NowLocationBase = 'labirint1.NowLocation'
                walls = labirint1.walls
                activator = labirint1.activator
                newXPos = labirint1.newXPos
                newYPos = labirint1.newYPos
                main.sprites_for_dialog = pygame.sprite.Group()"""

                NowLocation = undergroundV2.NowLocation
                NowLocationRect = undergroundV2.NowLocationRect
                NowLocationBase = 'undergroundV2.NowLocation'
                walls = undergroundV2.walls
                activator = undergroundV2.activator
                newXPos = undergroundV2.newXPos
                newYPos = undergroundV2.newYPos
                main.sprites_for_dialog = pygame.sprite.Group()

            elif NowLocation == undergroundV2.NowLocation:
                NowLocation = workRoomV4.NowLocation
                NowLocationRect = workRoomV4.NowLocationRect
                NowLocationBase = 'workRoomV4.NowLocation'
                walls = workRoomV4.walls
                activator = workRoomV4.activator
                newXPos = workRoomV4.newXPos
                newYPos = workRoomV4.newYPos
                main.sprites_for_dialog = pygame.sprite.Group()
                dialog_window = workRoomV4.dialog_window

            elif NowLocation == computerRoomV5.NowLocation:
                NowLocation = bossRoom.NowLocation
                NowLocationRect = bossRoom.NowLocationRect
                NowLocationBase = 'bossRoom.NowLocation'
                walls = bossRoom.walls
                activator = bossRoom.activator
                newXPos = bossRoom.newXPos
                newYPos = bossRoom.newYPos
                main.sprites_for_dialog = pygame.sprite.Group()
                dialog_window = bossRoom.dialog_window

        """for i in range(0, len(walls)):
            main.all_sprites.add(walls[i])

        for i in range(0, len(activator)):
            main.all_sprites.add(activator[i])

        for i in range(0, len(activatorV2)):
            main.all_sprites.add(activatorV2[i])"""

        for i in range(0, len(dialog_window)):
            main.sprites_for_dialog.add(dialog_window[i])

        main.player.setWalls(walls)
        main.player.setActivator(activator)
        main.player.setActivatorV2(activatorV2)

        main.screen.blit(NowLocation, NowLocationRect)
        main.all_sprites.draw(main.screen)

        if activatorChecker == True:
            #if params.for_spawn_dialog_window == True:
            if NowLocation in dialogRooms:
                main.sprites_for_dialog.update()
                main.sprites_for_dialog.draw(main.screen)
            elif NowLocation in doorRooms:
                gameover = VideoFileClip('Gameover.mp4')
                gameover.preview()
                time.sleep(0.1)

                secondRulesScene = VideoFileClip('SecondRules.mp4')
                secondRulesScene.preview()
                time.sleep(0.1)

                NowLocation = DoorRoom01.NowLocation
                NowLocationRect = DoorRoom01.NowLocationRect
                NowLocationBase = 'DoorRoom01.NowLocation'
                walls = DoorRoom01.walls
                activator = DoorRoom01.activator
                newXPos = DoorRoom01.newXPos
                newYPos = DoorRoom01.newXPos
                cur.execute(f"UPDATE PlayerPos SET befLocation = ' '")

            elif NowLocation == labirint1.NowLocation:
                gameover = VideoFileClip('Gameover.mp4')
                gameover.preview()
                time.sleep(0.1)

                labirintRulesScene = VideoFileClip('labirintRules.mp4')
                labirintRulesScene.preview()
                time.sleep(0.1)

                NowLocation = labirint1.NowLocation
                NowLocationRect = labirint1.NowLocationRect
                NowLocationBase = 'labirint1.NowLocation'
                walls = labirint1.walls
                activator = labirint1.activator
                newXPos = labirint1.newXPos
                newYPos = labirint1.newXPos
                cur.execute(f"UPDATE PlayerPos SET befLocation = ' '")

        if activatorCheckerV2 == True:
            if NowLocation in leftWrongBrainRooms:
                gameover = VideoFileClip('Gameover.mp4')
                gameover.preview()
                time.sleep(0.1)

                letterScene = VideoFileClip('letterScene.mp4')
                letterScene.preview()
                time.sleep(0.1)

                NowLocation = brainRoom1.NowLocation
                NowLocationRect = brainRoom1.NowLocationRect
                NowLocationBase = 'brainRoom1.NowLocation'
                walls = brainRoom1.walls
                activator = brainRoom1.activator
                newXPos = brainRoom1.newXPos
                newYPos = brainRoom1.newYPos
                cur.execute(f"UPDATE PlayerPos SET befLocation = ' '")

            elif NowLocation == brainRoom3.NowLocation:
                gameover = VideoFileClip('Gameover.mp4')
                gameover.preview()
                time.sleep(0.1)

                letterScene = VideoFileClip('letterScene.mp4')
                letterScene.preview()
                time.sleep(0.1)

                NowLocation = brainRoom1.NowLocation
                NowLocationRect = brainRoom1.NowLocationRect
                NowLocationBase = 'brainRoom1.NowLocation'
                walls = brainRoom1.walls
                activator = brainRoom1.activator
                newXPos = brainRoom1.newXPos
                newYPos = brainRoom1.newYPos
                cur.execute(f"UPDATE PlayerPos SET befLocation = ' '")

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()