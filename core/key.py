#core.key
#by boot1110001

### IMPORTS ####################################################################
import pygame
from core import log
from datetime import datetime

### FUNCTIONS ##################################################################
def ongamekey(pressed_keys, map, lang, verbose):
    xcell, ycell = map.player.xcell, map.player.ycell
    _xcellL, _ycellU = xcell, ycell
    _xcellR, _ycellD = xcell, ycell

    log.p.info("key pressed")

    if pressed_keys[pygame.K_UP] and not pressed_keys[pygame.K_DOWN]:
        _ycellU-=1
        if (map.checkmove(xcell, _ycellU, verbose, lang)):
            map.player.move_up()
            map.goal.move_down()
            map.move_down()
            if verbose : log.p.up('['+datetime.now().strftime("%Y%m%d%H%M%S-%f")+'] ('+str(xcell)+', '+str(_ycellU)+')')

    if pressed_keys[pygame.K_DOWN] and not pressed_keys[pygame.K_UP]:
        _ycellD+=1
        if (map.checkmove(xcell, _ycellD, verbose, lang)):
            map.player.move_down()
            map.goal.move_up()
            map.move_up()
            if verbose : log.p.down('['+datetime.now().strftime("%Y%m%d%H%M%S-%f")+'] ('+str(xcell)+', '+str(_ycellD)+')')

    if pressed_keys[pygame.K_LEFT] and not pressed_keys[pygame.K_RIGHT]:
        _xcellL-=1
        if (map.checkmove(_xcellL, ycell, verbose, lang)):
            map.player.move_left()
            map.goal.move_right()
            map.move_right()
            if verbose : log.p.left('['+datetime.now().strftime("%Y%m%d%H%M%S-%f")+'] ('+str(_xcellL)+', '+str(ycell)+')')

    if pressed_keys[pygame.K_RIGHT] and not pressed_keys[pygame.K_LEFT]:
        _xcellR+=1
        if (map.checkmove(_xcellR, ycell, verbose, lang)):
            map.player.move_right()
            map.goal.move_left()
            map.move_left()
            if verbose : log.p.right('['+datetime.now().strftime("%Y%m%d%H%M%S-%f")+'] ('+str(_xcellR)+', '+str(ycell)+')')

def onmenukey(event, mselect, mmaxselect, verbose):
    if (event.key == pygame.K_UP):
        mselect = mselect - 1
        if mselect < 0: mselect = mmaxselect
        if verbose : log.p.up('mselect = '+str(mselect))
    elif (event.key == pygame.K_DOWN):
        mselect = mselect + 1
        if mselect > mmaxselect: mselect=0
        if verbose : log.p.down('mselect = '+str(mselect))
    return mselect

def onlevelkey(event, lselect, lmaxselect, verbose):
    if (event.key == pygame.K_LEFT):
        lselect-=1
        if lselect < 0: lselect = lmaxselect
        if verbose : log.p.left('lselect = '+str(lselect))
    elif (event.key == pygame.K_RIGHT):
        lselect+=1
        if lselect > lmaxselect: lselect = 0
        if verbose : log.p.right('lselect = '+str(lselect))
    return lselect
