# This script will print all the IAM, EC2 and s3 buckets in a account

import boto3
aws_man_con = boto3.session.Session(profile_name = "root",region_name = "us-east-1")

#Creating cleint session for iam, ec2 and s3

iam_cli = aws_man_con.client("iam")
s3_cli = aws_man_con.client("s3")
ec2_cli = aws_man_con.client("ec2")

#list all iam users using client

def iam():
        r_iam = iam_cli.list_users()['Users']
        print("The IAM users are :")
        for i in r_iam:
                print("username is {} and arn is {}".format(i['UserName'],i['Arn']))
                print("----------------------------")

#list all ec2 instances

def ec2():
        r_ec2 = ec2_cli.describe_instances()
        print("The ec2 instances are : ")
        for i in r_ec2['Reservations']:
                print(i['Instances'][0]['InstanceId'])
        print("-------------------------")
        print()

#list all the s3 buckets

def s3():
        r_s3 = s3_cli.list_buckets()
        print("The buckets are : ")
        for k in r_s3['Buckets']:
                print(k['Name'])

def main():
        iam()
        ec2()
        s3()


if __name__ == "__main__":
        main()
