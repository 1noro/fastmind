#core.map
#by boot1110001

### IMPORTS ####################################################################
from datetime import datetime
from graphic.elements.wall import Wall
from graphic.elements.goal import Goal
from graphic.elements.player import Player

### CLASSES ####################################################################
class Map:
    def __init__(self, str, stdsize, cellcenter, width, height, game_color_scheme):
        self.str=str

        lv_info=str.split('\n', 1)[0].split('::')
        self.lvrealname=lv_info[0]
        self.lvwidth=int(lv_info[1])
        self.lvheight=int(lv_info[2])

        str2 = '\n'.join(str.split('\n')[1:])

        real_lv_width=len(list(str2.split('\n', 1)[0]))
        list_by_lines=str2.split('\n')
        real_lv_height=len(list(filter(('').__ne__, list_by_lines)))

        if (self.lvwidth != real_lv_width):
            # print(self.lvwidth,' != ',real_lv_width)
            print('[WARN] The width of the indicated level does not correspond to reality. Assigning the correct width ... This can trigger an error in the printing of the level.')
            self.lvwidth = real_lv_width
        if (self.lvheight != real_lv_height):
            # print(self.lvwidth,' != ',real_lv_width)
            print('[WARN] The height of the indicated level does not correspond to reality. Assigning the correct width ... This can trigger an error in the printing of the level.')
            self.lvheight = real_lv_height

        self.onelinestr = str2.replace('\n','').replace('\r','')
        self.maplist = list(self.onelinestr)

        self.startindex = self.maplist.index("@")

        y = 1
        i=self.startindex+1
        while i>self.lvwidth:
            y+=1
            i-=self.lvwidth
        x = i

        self.startx = x
        self.starty = y

        # --- pre_draw_map -----------------------------------------------------
        self.wmap = [] # wall list
        self.womap = [] # wall object list
        self.goal = 0 # goal object
        self.player = 0 # player object

        xcellgap = cellcenter - self.startx
        ycellgap = cellcenter - self.starty
        xgap = int((xcellgap * width) / (width / stdsize))
        ygap = int((ycellgap * height) / (height / stdsize))

        maxx = stdsize * self.lvwidth
        maxy = stdsize * self.lvheight
        x = y = i = 0

        while (y < maxy):
            while (x < maxx):
                xcell = int((x * (width / stdsize)) / width) + 1
                ycell = int((y * (height / stdsize)) / height) + 1
                if (self.maplist[i] == '#'):
                    self.wmap.append([xcell, ycell])
                    self.womap.append(Wall(x+xgap, y+ygap, xcell, ycell, stdsize, game_color_scheme.WALL))
                elif (self.maplist[i] == '$'):
                    self.goal = Goal(x+xgap, y+ygap, xcell, ycell, stdsize, game_color_scheme.GOAL)
                elif (self.maplist[i] == '@'):
                    self.player = Player(x+xgap, y+ygap, xcell, ycell, stdsize, game_color_scheme.PLAYER1, game_color_scheme.PLAYER2)
                i+=1
                x+=stdsize
            x=0
            y+=stdsize

    def draw(self, screen):
        for o in self.womap: o.draw(screen)

    def move_left(self):
        for o in self.womap: o.move_left()

    def move_right(self):
        for o in self.womap: o.move_right()

    def move_up(self):
        for o in self.womap: o.move_up()

    def move_down(self):
        for o in self.womap: o.move_down()

    def checkvictory(self, victoryin, old_time, lang):
        victoryout = victoryin
        lvl_time = 0
        if (not victoryin and (self.player.x, self.player.y) == (self.goal.x, self.goal.y)):
            new_time = datetime.now()
            lvl_time = new_time - old_time
            print('[INFO] '+lang.time_stopped_at, new_time)
            print('[GOAL] '+lang.you_pass_the_level_in, lvl_time)
            victoryout = True
        return (victoryout, lvl_time)

    def __eq__(self,other):
        out=False
        return out
