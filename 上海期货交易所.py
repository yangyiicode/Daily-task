#�����ڻ�������������ȡ
import requests
import time
import demjson
import pandas  as pd
url01="http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQFuturesData?page=1&num=15&sort=position&asc=0&node="
url03="&base=futures"
lis=[['ȼ��', 'ry_qh', '13'], ['ԭ��', 'yy_qh', '30'], ['����', 'lv_qh', '1'], ['��', 'xj_qh', '4'], ['��п', 'xing_qh', '17'],['��ͭ', 'tong_qh', '5'], ['�ƽ�', 'hj_qh', '19', 'futures.fu_dig2'], ['���Ƹ�', 'lwg_qh', '21'], ['�߲�', 'xc_qh', '22'],['��Ǧ','qian_qh','25'],['����','by_qh','25'],['����','lq_qh','25'],['�������','rzjb_qh','14'],['����','xi_qh','21'],['����','ni_qh','21'], ['ֽ��','zj_qh','21']]
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
message.to_csv('g:�Ϻ��ڻ�������.csv')
