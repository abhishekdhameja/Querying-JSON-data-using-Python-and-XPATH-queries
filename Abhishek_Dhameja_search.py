import sys
import json
import string

with open(sys.argv[1]) as data_file:
    json_data = json.load(data_file)

keywords=[]
count=0
res=[]
exclude = set(string.punctuation)

for i in range(2,len(sys.argv)):
    keyword=sys.argv[i]
    keyword = keyword.lower()
    # if '\'s' in keyword:
    #     ind = keyword.index('\'s')
    #     keyword = keyword[:ind] + keyword[ind + 2:]
        # print i
        # keyword = ''.join(ch for ch in keyword if ch not in ['\'','s'])
    # keyword = ''.join(ch for ch in keyword if ch not in exclude)
    keywords.append(keyword)


for data in json_data['data']:
    for para in data['paragraphs']:
        for qa in para['qas']:
            q=qa['question'].lower().strip()
            #q = ''.join(ch for ch in q if ch not in exclude)
            for ch in q:
                if ch in exclude and ch!='\'':
                    #if(ch=='-' or ch=='_' or ch==':' or ch==';' or ch==',' or ch=='.' or ch==''):
                    q=q.replace(ch,' ')
                elif ch=='\'':
                    q=q.replace(ch,'')
            #print q
            words=q.split()
            #if all(item in words for item in keywords):
            #print keywords
            #print words
            if all(item in words for item in keywords):
                #print True
                res.append({'id':qa['id'],'question':qa['question'],'answer':qa['answers'][0]['text']})
            count+=1

#print count

#print json.dumps(res)
with open('1b.json', 'w') as outfile:
    json.dump(res, outfile)

print len(res),'matching questions found.'
print '1b.json file created.'