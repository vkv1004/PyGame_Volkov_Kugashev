import os
import main, random, sys
from main.locals import *

main.init()
main.key.set_repeat(200, 70)

fps = 30
width = 600
height = 600
new_asteroid_tick = 40

screen = main.display.set_mode((width, height))
clock = main.time.Clock()
main.display.set_caption('Пояс астероидов')
main.mouse.set_visible(False)

player = None
all_sprites = main.sprite.Group()
player_group = main.sprite.Group()
asteroid_group = main.sprite.Group()


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = main.image.load(fullname).convert()
    except main.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def Key():
    while True:
        for event in main.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_RETURN:
                    return


def write_Text(text, font, surface, x, y):
    text_object = font.render(text, 1, main.Color('white'))
    text_rect = text_object.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_object, text_rect)


def terminate():
    main.quit()
    sys.exit()
