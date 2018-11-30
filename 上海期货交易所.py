#金融期货交易所数据爬取
import requests
import time
import demjson
import pandas  as pd
url01="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQFuturesData?page=1&num=15&sort=position&asc=0&node="
url03="&base=futures"
lis=[['燃油', 'ry_qh', '13'], ['原油', 'yy_qh', '30'], ['沪铝', 'lv_qh', '1'], ['橡胶', 'xj_qh', '4'], ['沪锌', 'xing_qh', '17'],['沪铜', 'tong_qh', '5'], ['黄金', 'hj_qh', '19', 'futures.fu_dig2'], ['螺纹钢', 'lwg_qh', '21'], ['线材', 'xc_qh', '22'],['沪铅','qian_qh','25'],['白银','by_qh','25'],['沥青','lq_qh','25'],['热轧卷板','rzjb_qh','14'],['沪锡','xi_qh','21'],['沪镍','ni_qh','21'], ['纸浆','zj_qh','21']]
lis2=[]
for i in range(len(lis)):
    lis2.append(lis[i][1])

ulist=[]
for i in lis2:
#    print(url01+i+url03)
    ulist.append(url01+i+url03)
i=0
message=0
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }
for url in ulist:
    r=requests.get(url,headers)
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
message.to_csv('g:上海期货交易所.csv')
