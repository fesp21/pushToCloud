#! /usr/bin/python

import boto
import os
from os import listdir
thisIsConnection = boto.connect_s3()
theFirstBucketInYourAccount = thisIsConnection.get_all_buckets()[0]
imageFileInCurrentDirectory = [x for x in listdir("./") if (x.endswith(".jpg") or x.endswith(".png") or x.endswith(".JPG"))]
for filename in imageFileInCurrentDirectory:
    newkey = theFirstBucketInYourAccount.new_key(filename)
    newkey.set_contents_from_filename(filename)
    newkey.set_acl('public-read')
    newkey = []





