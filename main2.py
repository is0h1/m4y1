from pygame import *

init()
size = 1000, 700
window = display.set_mode(size)
clock = time.Clock

class Block:
    def __init__(self, img_path, width, height):
        global blocks
        self.image = transform.scale(image.load(img_path), (width, height))
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.y = 0
        blocks.append(self)

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
blocks = []
big_rock = Block('asset_level/big_rock.png', 150, 150)
medium_rock = Block('asset_level/medium_rock.png', 150, 100)
for i in range(5):
    
