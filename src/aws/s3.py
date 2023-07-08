from os import path

from src.aws.session import get_session

from src.conf.config import S3Config


class S3Client:
    def __init__(self, config: S3Config) -> None:
        self._config = config
        self._client = get_session(
            aws_access_key_id=config.aws_access_key_id,
            aws_secret_access_key=config.aws_secret_access_key,
        ).client("s3")

    def upload_file(self, file_path: str) -> None:
        print("Uploading log file to s3...")
        self._client.upload_file(
            file_path, self._config.bucket, path.basename(file_path)
        )
        print("Successfully uploaded log file to s3!")


def upload_file_to_s3(config: S3Config, file_path: str) -> None:
    s3_client = S3Client(config)
    s3_client.upload_file(file_path)
