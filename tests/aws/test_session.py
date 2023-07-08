from src.aws.session import get_session
from unittest.mock import Mock, patch
import boto3


@patch("boto3.Session", spec=boto3.Session)
def test_get_session(session_mock: Mock):
    get_session("dummy", "dummy")
    session_mock.assert_called_once()
