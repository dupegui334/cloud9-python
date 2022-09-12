#!/usr/bin/env python3

import boto3 #SDK of AWS for python

AWS_REGION = 'us-east-1' #Our AWS region i North Virginia  

EC2_RESOURCE = boto3.resource('ec2', region_name=AWS_REGION) #ec2 its just a name we gave to that

instances = EC2_RESOURCE.instances.all() # Grab all the info from the instances

for instance in instances: #For loop to print all the info 
    print(f'EC2 instance id: {instance.id}') # Print instanceS ID
    #print(f"EC2 instance state: {instance.state}")
    print(f"EC2 instance state: {instance.state['Name']}") # cause we need to write 'Name' we have to use doble quotes outside " ". 
    print(f"EC2 instance state: {instance.tags}") # cause we need to write 'Name' we have to use doble quotes outside " ".
    print(f"EC2 instance name: {instance.tags[0]['Value']}")# In case you want to see the name of the instance its running