import json
import string

fi=open('cinema.json')
st=fi.read()
data=json.loads(st)
fi.close()
dict1={}
for j in data:
	dict1[j['Title'].lower()]=str(j['Revenue'])
print len(dict1)

fi=open('final.tsv')
st=fi.read()
list1=st.split('\n')
list1.remove('')
fi.close()
list2=[]
for i in list1:
	try:
		buff=i.split('\t')
		rev=dict1[buff[1].lower()]
		list2.append(i+'\t'+rev)
	except:
		list2.append(i)

print len(list2)

fi=open('final1.tsv','w')
for i in list2:
	fi.write(i+'\n')
fi.close()

	
