#!/usr/bin/env bash



#Author: Piyush Ghai

set -ex

echo "uploading result files to s3"

hw_type=cpu

if [ "$1" = "True" ]
then
    hw_type=gpu
fi

echo `pwd`
cd /tmp/MMSBenchmark/out
echo `pwd`

today=`date +"%m-%d-%y"`
echo "Saving on S3 bucket on s3://benchmarkai-metrics-prod/daily/mms/$hw_type/$today"

for dir in $(ls `pwd`/)
do
    echo $dir
    aws s3 cp $dir/ s3://benchmarkai-metrics-prod/daily/mms/$hw_type/$today/$dir/ --recursive
done

echo "Files uploaded"
