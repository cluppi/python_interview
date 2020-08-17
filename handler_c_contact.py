import json
import logging
import urllib
from datetime import datetime

from src.create_signup import CreateSignup
from src.response import Response


def handle(event, context):
    try:
        event_body = json.loads(urllib.parse.unquote_plus(event["body"]))

        signs = CreateSignup()
        create = signs.create(
            event["requestContext"]["authorizer"]["claims"]["email"],
            datetime.now(),
            event_body[0],
        )

        return Response.handle(create, 200)

    except Exception as e:
        msg = f"Unable{str(e)}"
        logging.exception(msg)
        return Response.handle({"error": msg}, 500)