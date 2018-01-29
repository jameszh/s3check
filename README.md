
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
$ s3check --bucket <a s3 bucket>
[*] Can list objects in the bucket <a s3 bucket>: PASS
[*] Can write objects in the bucket <a s3 bucket>: PASS
[*] Can read objects in the bucket <a s3 bucket>: PASS
[*] Can delete objects in the bucket <a s3 bucket> PASS
```