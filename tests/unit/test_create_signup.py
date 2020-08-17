import unittest
from datetime import datetime

import boto3
from moto import mock_dynamodb2

from src.create_signup import CreateSignup


class TestCreateSignup(unittest.TestCase):
    @mock_dynamodb2
    def test_creates_signup(self):

        dynamodb = boto3.resource("dynamodb", region_name="eu-west-1")

        table = dynamodb.create_table(
            TableName="contacts",
            KeySchema=[
                {"AttributeName": "email", "KeyType": "HASH"},
                {"AttributeName": "day", "KeyType": "RANGE"},
            ],
            AttributeDefinitions=[
                {"AttributeName": "email", "AttributeType": "S"},
                {"AttributeName": "day", "AttributeType": "S"},
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )

        client = CreateSignup()
        response = client.create('stuart.mason@gmail.com', '11/10/2020', 'Stu Mason')


        print(result)