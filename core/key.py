#core.key
#by boot1110001

### IMPORTS ####################################################################
import pygame

### FUNCTIONS ##################################################################
def ongamekey(event, map, lang, verbose):
    xcell, ycell = map.player.xcell, map.player.ycell
    _xcell, _ycell = xcell, ycell
    if (event.key == pygame.K_UP):
        _ycell-=1
        if (map.checkmove(xcell, _ycell, verbose, lang)):
            map.player.move_up()
            map.goal.move_down()
            map.move_down()
            if verbose : print('[ UP ] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key == pygame.K_DOWN):
        _ycell+=1
        if (map.checkmove(xcell, _ycell, verbose, lang)):
            map.player.move_down()
            map.goal.move_up()
            map.move_up()
            if verbose : print('[DOWN] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key == pygame.K_LEFT):
        _xcell-=1
        if (map.checkmove(_xcell, ycell, verbose, lang)):
            map.player.move_left()
            map.goal.move_right()
            map.move_right()
            if verbose : print('[LEFT] ('+str(_xcell)+', '+str(ycell)+')')
    elif (event.key == pygame.K_RIGHT):
        _xcell+=1
        if (map.checkmove(_xcell, ycell, verbose, lang)):
            map.player.move_right()
            map.goal.move_left()
            map.move_left()
            if verbose : print('[RIGH] ('+str(_xcell)+', '+str(ycell)+')')

def ongamekey2(pressed_keys, map, lang, verbose):
    xcell, ycell = map.player.xcell, map.player.ycell
    _xcell, _ycell = xcell, ycell
    if pressed_keys[pygame.K_UP]:
        _ycell-=1
        if (map.checkmove(xcell, _ycell, verbose, lang)):
            map.player.move_up()
            map.goal.move_down()
            map.move_down()
            if verbose : print('[ UP ] ('+str(_xcell)+', '+str(ycell)+')')

    if pressed_keys[pygame.K_DOWN]:
        _ycell+=1
        if (map.checkmove(xcell, _ycell, verbose, lang)):
            map.player.move_down()
            map.goal.move_up()
            map.move_up()
            if verbose : print('[DOWN] ('+str(_xcell)+', '+str(ycell)+')')

    if pressed_keys[pygame.K_LEFT]:
        _xcell-=1
        if (map.checkmove(_xcell, ycell, verbose, lang)):
            map.player.move_left()
            map.goal.move_right()
            map.move_right()
            if verbose : print('[LEFT] ('+str(_xcell)+', '+str(ycell)+')')

    if pressed_keys[pygame.K_RIGHT]:
        _xcell+=1
        if (map.checkmove(_xcell, ycell, verbose, lang)):
            map.player.move_right()
            map.goal.move_left()
            map.move_left()
            if verbose : print('[RIGH] ('+str(_xcell)+', '+str(ycell)+')')

def onmenukey(event, mselect, mmaxselect, verbose):
    if (event.key == pygame.K_UP):
        mselect = mselect - 1
        if mselect < 0: mselect = mmaxselect
        if verbose : print('[ UP ] mselect = '+str(mselect))
    elif (event.key == pygame.K_DOWN):
        mselect = mselect + 1
        if mselect > mmaxselect: mselect=0
        if verbose : print('[DOWN] mselect = '+str(mselect))
    return mselect

def onlevelkey(event, lselect, lmaxselect, verbose):
    if (event.key == pygame.K_LEFT):
        lselect-=1
        if lselect < 0: lselect = lmaxselect
        if verbose : print('[LEFT] lselect = '+str(lselect))
    elif (event.key == pygame.K_RIGHT):
        lselect+=1
        if lselect > lmaxselect: lselect = 0
        if verbose : print('[RIGH] lselect = '+str(lselect))
    return lselect
