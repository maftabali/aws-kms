# aws-kms

Python script to show how to encrypt and decrypt data from within applications and when using AWS services integrated with KMS.

Uses boto3 AWS SDK

Create a aws profile with access to the resources that you intend to monitor

`aws configure --profile=<profile_name>`

Update the config file to use key alias and data to be encrypted like a database password

Install pipenv
`pip install pipenv`

To run
`pipenv run python aws-kms.py`
