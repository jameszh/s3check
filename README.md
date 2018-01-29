
# s3check

Check access permissions (LIST/WRITE/READ/DELETE) within a specified S3 bucket.


### Install

```
pip install git+https://github.com/jameszh/s3check
```

### Usage
```
$ s3check --help
Usage: s3check [OPTIONS]

Options:
  --bucket TEXT  The bucket to check
  --help         Show this message and exit.
```

```
$ s3check --bucket s3bucket
[*] List objects in the bucket s3bucket: Pass
[*] Write to the bucket s3bucket: Pass
[*] Read from the bucket s3bucket: Pass
[*] Delete object from bucket s3bucket: Pass
```