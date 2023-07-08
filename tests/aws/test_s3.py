from unittest.mock import Mock, patch

import boto3

from src.aws.s3 import upload_file_to_s3


@patch("boto3.Session", spec=boto3.Session)
@patch("src.conf.config.S3Config")
def test_upload_file_to_s3(s3_config: Mock, session_mock: Mock):
    upload_file_to_s3(s3_config, "dummy")
    session_mock.return_value.client.assert_called_once_with("s3")
    session_mock.return_value.client.return_value.upload_file.assert_called_once()
