
def keyword_list_generator(file_name):
    keywords=[]
    with open(file_name,'r') as file:
        for each_line in file:
            each_line=each_line.replace('\n','')
            req, keyword_string=each_line.split(':')
            #print(req+' are')
            #print(keyword_string)
            for k in keyword_string.split(','):
                if(len(k.strip(' '))!=1):
                    keywords.append(k.strip(' ').lower())
                else:
                    keywords.append(k.lower())

    keywords.remove('')
    #print(keywords)
    occur_table={}
    for each_key in keywords:
        occur_table[each_key]=0
    print('keywords are ')
    print(occur_table)
    return occur_table;


def keyword_checker(resume_file,tow):
    #tow is the table of words
    #r_f is the file to be scanned
    count=0;
    with open(resume_file,'r') as file:
        for each_line in file:
            for each_key in tow:
                #print(each_key)
                if(each_line.lower().find(each_key)!=-1):
                    count=count+1;
                    tow[each_key]=tow[each_key]+1     
    print(count)
    #print(tow)
    return tow;
    
