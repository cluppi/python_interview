import uuid
from datetime import datetime
from multiprocessing import Process

import boto3


class CreateSignup:
    def __init__(self):
        self.dynamodb = boto3.resource("dynamodb", region_name="eu-west-1")
        self.table = self.dynamodb.Table("signups")

    def create(
        self, email: str, request_datetime: datetime, full_name: str
    ) -> dict:

        signup = self.createSignupObject(full_name, request_datetime)

        p = Process(target=self.c, args=(email, full_name, request_datetime))
        p.start()

    def c(self, email, full_name, request_datetime):
        self.table.put_item(
            Item={
                'email': email,
                "uuid": str(uuid.uuid4()),
                "name": full_name,
                "time": request_datetime.strftime("%H:%M:%S"),
            }
        )

    def createSignupObject(self, full_name, request_datetime):
        return {
            "uuid": str(uuid.uuid4()),
            "name": full_name,
            "time": request_datetime.strftime("%H:%M:%S"),
        }
