#!/bin/bash

#Creating 1 instance which will be the host
aws ec2 run-instances --image-id ami-14c5486b --instance-type t2.micro --key-name FirstKeyPair --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=HostInstanceSandeep},{Key=username,Value=SandeepRajanP},{Key=emailId,Value=sandeeprajan.p@quantiphi.com},{Key=Project,Value=PE_Training}]' --iam-instance-profile Arn=arn:aws:iam::488599217855:instance-profile/PE_trainee_Admin_role --user-data  '#!/bin/bash
yum update -y  
sudo -u ec2-user ssh-keygen -t rsa -b 2048 -f /home/ec2-user/.ssh/id_rsa -q -N ""
aws s3 cp /home/ec2-user/.ssh/id_rsa.pub s3://buckettraining007/id_rsa.pub' --region us-east-1 --security-group-ids sg-7d965f36 

aws s3 ls s3://buckettraining007/id_rsa.pub
while [ $? -ne 0 ]
do
    echo Loading........
    sleep 5
    aws s3 ls s3://buckettraining007/id_rsa.pub
    if [[ $? -eq 0 ]]
    then
        echo "file upload"
        break
    fi
    aws s3 ls s3://buckettraining007/id_rsa.pub
done

#Creating 1 instance which will be the server
aws ec2 run-instances --image-id ami-14c5486b --instance-type t2.micro --key-name FirstKeyPair --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=ServerInstanceSandeep},{Key=username,Value=SandeepRajanP},{Key=emailId,Value=sandeeprajan.p@quantiphi.com},{Key=Project,Value=PE_Training}]' --iam-instance-profile Arn=arn:aws:iam::488599217855:instance-profile/PE_trainee_Admin_role --user-data '#!/bin/bash
yum update -y
aws s3 cp s3://buckettraining007/id_rsa.pub /home/ec2-user/.ssh/
chmod 700 chmod 700 /home/ec2-user/.ssh
chmod 600 /home/ec2-user/.ssh/id_rsa.pub
chmod 600 /home/ec2-user/.ssh/authorized_keys	
cat /home/ec2-user/.ssh/id_rsa.pub >> /home/ec2-user/.ssh/authorized_keys' --region us-east-1 --security-group-ids sg-7d965f36
