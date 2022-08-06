from jinja2 import BaseLoader, TemplateNotFound
from google.cloud import storage
import warnings
from google.cloud.exceptions import GoogleCloudError
import posixpath as path


class GCSJinjaLoader(BaseLoader):
    def __init__(self, bucket_name, prefix='', gcs=None):
        self._client = storage.Client()
        try:
            self.bucket = self._client.get_bucket(bucket_name)
        except GoogleCloudError:
            raise
        self.prefix = prefix
        super(GCSJinjaLoader, self).__init__()

    def get_source(self, __, template):
        if self.prefix:
            template = path.join(self.prefix, template)
        data = self.bucket.get_blob(template)
        if not data:
            raise TemplateNotFound(template)

        return (data.download_as_bytes().decode('utf-8'), None, lambda: True)
