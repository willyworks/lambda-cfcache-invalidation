import lamvery
import boto3
import os
from datetime import datetime

client = boto3.client('cloudfront')


def lambda_handler(event, context):
    lamvery.env.load()

    response = client.create_invalidation(
        DistributionId=os.environ['CF_DISR_ID'],
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': [
                    '/'
                ]
            },
            'CallerReference': datetime.now().strftime('%Y%m%d%H%M%S')
        }
    )
    print(response)
