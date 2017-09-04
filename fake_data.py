#!/usr/bin/env python
# coding = utf-8
#
# mail lsyh00@gmail.com


from faker import Factory
from elasticsearch import Elasticsearch
import argparse
import json
import time
from datetime import datetime, timedelta
from multiprocessing import Pool


def es_fill_data(es, index, _type, keylist, timestamp):

    fake = Factory.create()

    body = {}
    for key in keylist:
        methd = "fake.%s()" % key
        value = eval(methd)
        body.update({key: value})

    body.update({'timestamp': timestamp})

    go = es.index(
        index=index,
        doc_type=_type,
        body=body
    )

    print json.dumps(go, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='PROG',
        usage=('%(prog)s -i index -t type -d doc_key1,doc_key2,... [-s|--server]'
               '[-p|--port] [-v | --verbose]'))

    parser.add_argument('--index', '-i')
    parser.add_argument('--type', '-t')
    parser.add_argument('--number', '-n', default=1)
    parser.add_argument('--data', '-d', nargs='*',
                        choices=(
                            "ipv4",
                            "name",
                            "email",
                            "phone_number",
                            "random_int"
                            )
                        )
    parser.add_argument('--server', '-s', default='127.0.0.1')
    parser.add_argument('--port', '-p', default='9200')
    parser.add_argument('--verbose', '-v', action='count')

    args = vars(parser.parse_args())
    print args

    es_host = "http://{server}:{port}".format(server=args['server'],
                                              port=args['port'])
    es = Elasticsearch(es_host)
    num = int(args['number'])

    #p = Pool(10)
    for i in xrange(num):
        timestamp = datetime.utcnow() - timedelta(minutes=i)
        es_fill_data(
            es,
            index=args['index'],
            _type=args['type'],
            keylist=args['data'],
            timestamp=timestamp
        )

        #p.apply_async(
        #        es_fill_data(
        #            es,
        #            args['index'],
        #            args['type'],
        #            args['data'],
        #            timestamp
        #            )
        #        )
    #p.close()
