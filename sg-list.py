import boto3
import os.path
import csv
import json



input_file_name = 'input.csv'
output_file_name = 'output.csv'
file_check = 0
sg_id_actual_list=[]
output_data_rows={}


client = boto3.client('ec2')
response = client.describe_security_groups()
total_sg_list = response['SecurityGroups']
#print(response)

if os.path.exists(input_file_name):
	print("Input file exists")
else:
	file_check=1
	print("Input file missing(input.csv), Please place it in current directory..")

if os.path.exists(output_file_name):
	print("Output file exists")
else:
	print("Output file missing(output.csv), Creating a new one..")
	f = open(output_file_name, 'a+')
	f.close()


with open(input_file_name, newline='') as csvfile:
	input_data = csv.reader(csvfile)
	for row in input_data:
#		print(row[2])
		sg_id_actual_list.append(row[2])
		output_data_rows[row[2]]={'date' : row[0], 'change' : row[1], 'sg_id' : row[2]}


#print(output_data_rows)

for item in sg_id_actual_list:
	val = [d for i, d in enumerate(total_sg_list) if item in d.values()]
	val = val[0]
	output_data_rows[val['GroupId']].update({'tags' : val['Tags'], 'inbound' : val['IpPermissions'], 'outbound' : val['IpPermissionsEgress']})


#print(output_data_rows)

with open(output_file_name, 'a+' ) as f:
	for val  in output_data_rows.values():
		tmp=str(val['date'])+","+str(val['change'])+","+str(val['sg_id'])+","+str(val['tags'])+","+str(val['inbound'])+","+str(val['outbound'])+"\n"
		f.write(tmp)

	

	f.close()
