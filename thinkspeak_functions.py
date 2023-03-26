import time
from urllib.request import urlopen
import json


WRITE_API_KEY='ZZXJN8536U5BLY5A'
READ_API_KEY='JRIQ8KJT2R2CNLLL'
CHANNEL_ID='887479'
value=[]
x=0
def read_last_value(field_no):
    TS =urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s"% (CHANNEL_ID,READ_API_KEY))
    response = TS.read()
    response = response.decode()
    data=json.loads(response)
    field_id=str("field"+str(field_no))
    last_value=data[field_id]
    last_created=data['created_at']
    last_data=(last_created,last_value)
    TS.close()
    return(last_data)

def read_data(field_no,total_entry):
    TS =urlopen("http://api.thingspeak.com/channels/%s/feeds.json?api_key=%s"% (CHANNEL_ID,READ_API_KEY))
    response = TS.read()
##    print(response)
    print();
    response=response.decode()
##    print(response)
    print();
    data=json.loads(response)
##    print(data)
    print();
    field_id=str("field"+str(field_no))
    feed = data['feeds']
    created= feed[1]['created_at']
    for i in range((total_entry)):
        value.append(feed[i]['field1'])
    return(value)


#https://api.thingspeak.com/update?api_key= ZZXJN8536U5BLY5A & field1 =0
def write_data(field_no,value):
    field_id=str("field"+str(field_no))
    upload=urlopen('http://api.thingspeak.com/update?api_key=%s&%s=%d'% (WRITE_API_KEY,field_id,value))
    print(str("status code:"+str(upload.getcode())))

    
    #status codes 200 indicates data is uploaded i believe

def read_channel_name():
    TS =urlopen("http://api.thingspeak.com/channels/%s/feeds.json?api_key=%s"% (CHANNEL_ID,READ_API_KEY))
    response = TS.read()
    response = response.decode()
    data=json.loads(response)
    channel = data['channel']
    name=channel['name']
    return(str(name))

def read_total_entries():
    TS =urlopen("http://api.thingspeak.com/channels/%s/feeds.json?api_key=%s"% (CHANNEL_ID,READ_API_KEY))
    response = TS.read()
    response = response.decode()
    data=json.loads(response)
    channel = data['channel']
    total_entries=channel['last_entry_id']
    return(total_entries)
while(1):
    #try:
    print("1.write data")
    print("2.read all data")
    print("3.read last data")
    print("4.read channel name")
    print("5.Exit")
    x=int(input("Specify your option by enter the corresponding number:"))
    if(x==1):
        field_no=int(input("enter the number value of field which data to be written:"))
        value=int(input("enter the value to be uploaded:"))
        write_data(field_no,value)
    elif(x==2):
        field_no=int(input("enter the number value of field which data to be read:"))
        total_entry=read_total_entries()
        print(read_data(field_no,total_entry))
    elif(x==3):
        field_no=int(input("enter the number value of field which data to be read:"))
        print(read_last_value(field_no))
    elif(x==4):
        read_channel_name()
    elif(x==5):
        exit()
   # except:
    #    pass
##        print("err")
    
