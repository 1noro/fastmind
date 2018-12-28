#core.map
#by boot1110001

### IMPORTS ####################################################################

### CLASSES ####################################################################
class Map:
    def __init__(self, str):
        self.file_str=str

        lv_info=str.split('\n', 1)[0].split('::')
        self.lv_name=lv_info[0]
        pre_lv_width=lv_info[1]
        pre_lv_height=lv_info[2]

        str2 = '\n'.join(str.split('\n')[1:])

        print('Level Width: '+str(len(list(str2.split('\n', 1)[0]))))

        

    def set_stdsize(self,new_stdsize):
        self.width=new_stdsize
        self.height=new_stdsize

    def __eq__(self,other):
        out=False
        return out
