import pygame

class Sprites(pygame.sprite.Group):

    def draw(self, surface):

        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            self.spritedict[spr] = surface_blit(spr.image, spr.rect)
        self.lostsprites = []