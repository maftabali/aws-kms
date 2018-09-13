import boto3
import yaml

with open("config.yml",'r') as config:
    cfg = yaml.load(config)

kms_client = boto3.client('kms')

my_keyid = cfg['alias']
pwd = cfg['db_pwd']

response = kms_client.encrypt(KeyId=my_keyid,Plaintext=pwd)

encrypted_string = response['CiphertextBlob']

print('Encrypted string: ' + str(encrypted_string))

result = kms_client.decrypt(CiphertextBlob=encrypted_string)



decrypted_string = result['Plaintext']

print('Decrypted string: ' + str(decrypted_string))
