import boto3
from botocore.handlers import disable_signing
import os


resource = boto3.client('s3', region_name='ap-northeast-3')
resource = boto3.resource('s3')
resource.meta.client.meta.events.register('choose-signer.s3.*', disable_signing)

bucket = resource.Bucket('cse-cic-ids2018')

if not os.path.exists("datasets/"):
    os.makedirs("datasets")

if not os.path.exists("datasets/Friday-02-03-2018_TrafficForML_CICFlowMeter.csv"):
    bucket.download_file('Processed Traffic Data for ML Algorithms/Friday-02-03-2018_TrafficForML_CICFlowMeter.csv', 'datasets/Friday-02-03-2018_TrafficForML_CICFlowMeter.csv')
else:
    print("Dataset Friday-02-03-2018_TrafficForML_CICFlowMeter.csv already downloaded")


if not os.path.exists("datasets/Friday-16-02-2018_TrafficForML_CICFlowMeter.csv"):
    bucket.download_file('Processed Traffic Data for ML Algorithms/Friday-16-02-2018_TrafficForML_CICFlowMeter.csv', 'datasets/Friday-16-02-2018_TrafficForML_CICFlowMeter.csv')
else:
    print("Dataset Friday-16-02-2018_TrafficForML_CICFlowMeter.csv already downloaded")
# Check bucket content 
# for item in bucket.objects.all():
#    print(item)
