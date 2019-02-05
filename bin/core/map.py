#core.map
#by boot1110001

### IMPORTS ####################################################################

### CLASSES ####################################################################
class Map:
    def __init__(self, str):
        self.str=str

        lv_info=str.split('\n', 1)[0].split('::')
        self.lvname=lv_info[0]
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

    def __eq__(self,other):
        out=False
        return out
