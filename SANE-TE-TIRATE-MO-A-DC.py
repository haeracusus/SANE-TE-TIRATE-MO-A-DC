import sys
ln = 1
lines = []
correctname = 'Y'

def askfilename():
    global correctname
    filename = input('')
    print(filename+'.txt. Is that correct?')
    correctname=input('[Y/n] ')
    checkname()


def checkname():
	if correctname.lower() == 'y':
		file = open(filename+'.txt','w')
		global ln
		while True:
			line = input('| '+str(ln)+' | ')
			if line == 'EOF':
				for aline in lines:
					with open(filename+'.txt','a') as thefile:
						thefile.write(aline+'\n')
				sys.exit('Changes written to file.')


			ln += 1
			lines.append(line)
	else:
		askfilename()


filename = input('')
print(filename+'.txt. Is that correct?')
correctname=input('[Y/n] ')
checkname()


