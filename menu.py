import pygame, pygame_menu, importlib, imports, time
import game, params
from moviepy.editor import *
importlib.reload(game)

mytheme = pygame_menu.themes.THEME_ORANGE.copy()
myimage = pygame_menu.baseimage.BaseImage(
    image_path='menu.png',
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_REPEAT_XY,
)
mytheme.background_color = myimage
mytheme.widget_font_size = 72
mytheme.widget_font = pygame_menu.font.FONT_8BIT

def start_the_game():
    # Do the job here !
    pygame.mixer.music.stop()
    scene1 = VideoFileClip(r'Scene1.mp4')
    scene1.preview()
    time.sleep(0.1)
    game.run()

def start():
    pygame.mixer.init()
    pygame.mixer.music.load("menu_music.mp3")
    pygame.init()
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)
    surface = pygame.display.set_mode((params.WIDTH, params.HEIGHT))

    menu = pygame_menu.Menu('Menu', params.WIDTH, params.HEIGHT,
                           theme=mytheme)
    menu.add.button('Play', start_the_game)
    menu.add.button('Exit', pygame_menu.events.EXIT)
    menu.mainloop(surface)