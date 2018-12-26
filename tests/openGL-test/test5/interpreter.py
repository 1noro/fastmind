
def main():
	str1 = open('1.lv', 'r').read()
	
	print(str1)
	print('-'*80)
	
	lv_info=str1.split('\n', 1)[0].split('::')
	print('Level Name: '+lv_info[0])
	print('Level Width: '+lv_info[1])
	print('Level Height: '+lv_info[2])
	
	print('-'*80)
	str2 = '\n'.join(str1.split('\n')[1:])
	print(str2)
	
	print('-'*80)
	print('Level Width: '+str(len(list(str2.split('\n', 1)[0]))))
	list_by_lines1=str2.split('\n')
	list_by_lines2=list(filter(('').__ne__, list_by_lines1))
	# ~ print(list_by_lines1)
	# ~ print(list_by_lines2)
	print('Level Height: '+str(len(list_by_lines2)))
	
	print('-'*80)
	str3 = str2.replace('\n','').replace('\r','')
	print(str3)
	
	print('-'*80)
	map_list=list(str3)
	print(map_list)

main()
