# -*- coding: utf8 -*-
"""
cassandra_backup.main.

~~~~~~~~~~~~~~~~~~~~~~

Command line tools.
"""

import argparse


def cli():
    """Setup command line arguments."""
    parser = argparse.ArgumentParser(
        description="cassandra backup command tools.")
    parser.add_argument("--op",
                        type=str,
                        metavar="op",
                        dest="op_type",
                        help="operation type",
                        required=True)
    parser.add_argument("--aws-key-id",
                        type=str,
                        metavar="aws key id",
                        dest="aws_key_id",
                        help="aws key id, optional")
    parser.add_argument("--aws-access-key-id",
                        type=str,
                        metavar="aws-access-key-id",
                        dest="aws_access_key_id",
                        help="aws access key id, optional")
    parser.add_argument("--aws-secret-access-key",
                        type=str,
                        metavar="aws-secret-access-key",
                        dest="aws_secret_access_key",
                        help="aws secret access key, optional")
    parser.add_argument("--s3-bucket-name",
                        type=str,
                        metavar="s3-bucket-name",
                        dest="s3_bucket_name",
                        help="s3 bucket name, required",
                        required=True)
    parser.add_argument("--s3-region",
                        type=str,
                        metavar="s3-region",
                        dest="s3_region",
                        help="s3 region name, optional")
    parser.add_argument("--hosts",
                        type=str,
                        metavar="hosts",
                        dest="hosts",
                        help="hosts are need to backup or restore",
                        required=True)
    parser.add_argument("--cassandra-dir",
                        type=str,
                        metavar="cassandra-dir",
                        dest="cassandra_dir",
                        help="cassandra installed location",
                        required=True)
    parser.add_argument("--cassandra-data-dir",
                        type=str,
                        metavar="cassandra-data-dir",
                        dest="cassandra_data_dir",
                        help="cassandra data stored location")
    parser.add_argument("--keyspace",
                        type=str,
                        metavar="keyspace",
                        dest="keyspace",
                        help="cassandra keyspace, optional")
    parser.add_argument("--table",
                        type=str,
                        metavar="table",
                        dest="table",
                        help="table in keyspace, optional")
