import requests
import time
import demjson
url01="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQFuturesData?page=1&num=5&sort=position&asc=0&node="
url03="_qh&base=futures"
a=['pta','czy','ycz','czp','dlm','qm','jdm','bst','mh','zxd','zc','bl','wxd','gt','mg','ms','xpg']
ulist=[]
for i in a:
#    print(url01+i+url03)
    ulist.append(url01+i+url03)
i=0
message=0
for url in ulist:
    r=requests.get(url)
    demo=r.text
    data=demjson.decode(demo)
    data1=pd.DataFrame(data,columns=list(data[0].keys()))
    i+=1
    
    if i>1:   
        message=message.append(data1)
    else:
        message=data1
        
message['createtime']=time.strftime('%Y.%m.%d %H:%M:%S ',time.localtime(time.time()))   
message['updatetime']=None
message.to_csv('g:data4.csv')