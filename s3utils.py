from __future__ import absolute_import
# from storages.backends.s3boto import S3BotoStorage

StaticRootS3BotoStorage = lambda: storages.backends.s3boto.S3BotoStorage(location='static')
MediaRootS3BotoStorage  = lambda: storages.backends.s3boto.S3BotoStorage(location='media')