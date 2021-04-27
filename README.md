# sg-list



## 1. Install & Configure aws cli  & boto
```
#aws configure
# pip install boto3
```

## 2. Copy 3 files in same location. input.csv, output.csv, sg-list.py
1.Enter date,change no, sg id in correct order in input.csv
2.Run below command to execute
```
# python sg-list.py
```
3. output of output.csv contains
```
date,change,id,tags,inbound,outbound
```
