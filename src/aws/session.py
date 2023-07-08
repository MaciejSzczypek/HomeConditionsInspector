import boto3


def get_session(aws_access_key_id: str, aws_secret_access_key: str) -> boto3.Session:
    return boto3.Session(
        aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key
    )
