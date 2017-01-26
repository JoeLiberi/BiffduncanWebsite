from __future__ import absolute_import
import storages.backends.s3boto

StaticRootS3BotoStorage = lambda: storages.backends.s3boto.S3BotoStorage(location='static')
MediaRootS3BotoStorage  = lambda: storages.backends.s3boto.S3BotoStorage(location='media')