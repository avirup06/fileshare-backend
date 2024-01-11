import json
import logging
import base64
from json.decoder import JSONDecodeError
import jwt
import os
import time
from functools import lru_cache
from fastapi import Response, HTTPException, Request


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def response_helper(status_code, msg, data: dict, headers=None, exception=False):
    """
    :param status_code:
    :param msg:
    :param data:
    :param headers:
    :param exception:
    :return:
    """

    if not isinstance(msg, str):
        msg = json.dumps(msg)

    result = {
        "body": {
            "result": data
        },
        "message": msg
    }

    if exception:
        raise HTTPException(
            status_code=status_code,
            detail=result
        )

    return Response(
        content=json.dumps(result),
        status_code=status_code,
        media_type="application/json"
    )

def prepare_response(message, status_code):
    if (
            isinstance(message, dict)
            or isinstance(message, list)
            or isinstance(message, str)
    ):
        message = json.dumps(message)
    return {"statusCode": status_code, "body": message}


def base64_encode_data(data):
    if isinstance(data, str):
        input_data = data
    elif isinstance(data, (int, float, complex, set)):
        input_data = str(data)
    elif isinstance(data, (dict, list, tuple)):
        input_data = json.dumps(data)
    else:
        return None

    string_bytes = input_data.encode("ascii")
    base64_bytes = base64.b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


def base64_decode_data(base64_string):
    base64_bytes = base64_string.encode("ascii")
    string_bytes = base64.b64decode(base64_bytes)
    string = string_bytes.decode("ascii")
    try:
        return json.loads(string)
    except JSONDecodeError as e:
        return string


def decode_base64(base64_string):
    # Add padding to the base64 string
    base64_with_padding = base64_string + "=" * (4 - len(base64_string) % 4)
    # Decode the base64 image
    return base64.b64decode(base64_with_padding)






