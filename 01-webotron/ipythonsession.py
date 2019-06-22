# coding: utf-8
import boto3
session = boto3.Session
session = boto3.Session(profile_name="pyton")
boto3.session.Session().available_profiles
session = boto3.Session(profile_name="default")
s3 = session.resource ('s3')
for bucket in s3.buckets.all():
    print(bucket)

s3.create_bucket(Bucket='automatingawsthor-boto3')
for bucket in s3.buckets.all():
    print(bucket)
