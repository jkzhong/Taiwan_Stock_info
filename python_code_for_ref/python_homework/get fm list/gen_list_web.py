import osimport timeimport randomimport urllib.requestimport reOutput_list_file = open("Sky_FM.list", "w")url = 'http://listen.sky.fm/public1'      content = urllib.request.urlopen(url)content = content.read()content_str = content.decode('utf-8','ignore').split(",")#print(content_str)for loop_num in range(len(content_str)):    name_list = re.search("name\":\".{,30}",content_str[loop_num])    if name_list :        #print(name_list.group(0)[7:len(name_list.group(0))-1])        Output_list_file.write("#SKY FM:%s\n"%name_list.group(0)[7:len(name_list.group(0))-1])            url_list = re.search(r"http.{25,90}pls",content_str[loop_num])    if url_list :        #print(url_list.group(0))        Output_list_file.write("mplayer –o oss –cache 256 –playlist %s < /dev/null &\n"%url_list.group(0))Output_list_file.close()#merge must wite all search list id,key,name....    #merge_list = re.search(r'(name.{,30}") (http.{25,90}pls)',content_str[loop_num]) #error    #if merge_list :        #print(merge_list.group(0))        #print(merge_list.group(1))# ([\s\S]+) : it means# \s : all whitspace# \s : any chart# [] : make "or" condiction.  [\s\S] this chart is whitspace or any chart(AZ09az)# +  : to match 1 or more repetitions of the preceding RE. not limit any string number. # () : inside are Regular expression (set group)# reference web site : http://docs.python.org/3.3/library/re.html#re.M