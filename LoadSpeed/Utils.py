import os

def rename(path):
	l=os.listdir(path)
	for i in l:
		n=i[:i.index('.')]
		p1=path+'\\'+i
		step=(int(n)-1)*50
		p2=path+'\\'+str(step).zfill(6)+'.jpg'
		os.rename(p1,p2)


if __name__=='__main__':
	path = r'E:\result\ComparaPic\VID_20180201_185138'
	rename(path)
