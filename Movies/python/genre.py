import string

fi=open('final.tsv')
st=fi.read()
list1=st.split('\n')
list1.remove('')
fi.close()

list2=[]
for i in list1:
	buff=i.split('\t')
	buff1=buff[7].split(',')
	for b in buff1:
		list2.append(b+'\t'+buff[8])

fi=open('genre.tsv','w')
for i in list2:
	fi.write(i+'\n')
fi.close()
