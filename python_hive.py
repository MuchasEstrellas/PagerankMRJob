from pyhive import hive
cursor = hive.connect('localhost').cursor()
cursor.execute("SELECT * FROM `wiki` WHERE `id` LIKE '%.htmm%' OR `id` LIKE '%.htmk%'  ORDER BY `id` ASC")
rows = cursor.fetchall()

for i in range(0,len(rows),2):
    pair_found = False
    newname=""
    newlinks=""
    if '.htmm' in rows[i][0]:
        if '.htmk' in rows[i+1][0]:
            newname = newrow[0].replace("htmm","html").encode('utf-8')
            # originCnt = int(newname.split("/")[-1].replace('"',''))
            # newCnt = originCnt + int(rows[i+1][0].split("/")[-1].replace('"',''))
            # newname = newname.replace("/" + str(originCnt), "/" + str(newCnt))
            newlinks = '"'+str(rows[i][1].encode('utf-8').replace('"','')+" "+rows[i+1][1].encode('utf-8').replace('"','')).strip()+'"'
    elif '.htmk' in rows[i][0]:
        if '.htmm' in rows[i+1][0]:
            newname = rows[i+1][0].replace("htmm", "html").encode('utf-8')
            # originCnt=int(newname.split("/")[-1].replace('"',''))
            # newCnt=originCnt+int(rows[i][0].split("/")[-1].replace('"',''))
            # newname=newname.replace("/"+str(originCnt),"/"+str(newCnt))
            newlinks= '"'+str(rows[i+1][1].encode('utf-8').replace('"','')+" "+rows[i][1].encode('utf-8').replace('"','')).strip()+'"'
    newrow = newname+"\t"+newlinks
    print(newrow)
