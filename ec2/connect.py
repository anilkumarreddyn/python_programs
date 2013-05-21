#SD
#This script connects a Amazon EC2 instance in given location using your AWS Key and Secret. Replace with appropriate info below
#You will need to install BOTO on python version > 2.7
#!/root/.python/bin/python

import boto.ec2
import re
import time

def main():
  #Replace <> with your values
  conn = boto.ec2.connect_to_region("<region>", aws_access_key_id='<aws_key>', aws_secret_access_key='<aws_secret>')
  print "Connected to --->", re.split(':', str(conn))[1]

  conn.run_instances(
        'ami-XXXXXXX',
        key_name='<your_key>',
        instance_type='t1.micro',
        security_groups=['<your_security_group>'])  

  raw_input("Wait for the instance to come up")
 
  reservations = conn.get_all_instances() 
  print reservations,'\n'
  instance_id = [] 
  for i in range(0, len(reservations)): 
    instance = reservations[i].instances
    instance_id.append(re.split(':', str(instance[0]))[1])
    print "Instance Name --->", instance[0]
    for x in range(0, len(instance)):
      print "Instance Type --->", instance[x].instance_type
      print "Instance Placement --->", instance[x].placement,"\n"

  raw_input("Press enter to shutdown the instances")  
 
  for instance in instance_id:
    print "Stopping Instance ID --> " , instance
    conn.stop_instances(instance_ids=[instance])

if __name__ == '__main__':
  main()


