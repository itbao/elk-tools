#!/usr/bin/env python
# coding = utf-8
#
# mail lsyh00@gmail.com


from faker import Factory
from elasticsearch import Elasticsearch
import argparse
import json
import time
from datetime import datetime,timedelta



def es_fill_data(es,num,index,_type,keylist):

    fake = Factory.create()
    number = 0

    for x in range(int(num)):

        genName = fake.name()
        genJob = fake.job()
        genEmail = fake.email()

        #global number
        number -= 1

        timestamp = datetime.utcnow() + timedelta(minutes = number)

        go = es.index(
            index=index,
            doc_type=_type,
            #id=str(number),
            body={
                "name": genName,
                "job": genJob,
                "email": genEmail,
                'timestamp': timestamp
            }
        )

        print json.dumps(go, indent=4)
        #time.sleep(0.01)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='PROG',
        usage=('%(prog)s -i index -t type -d doc_key1,doc_key2,... [-s|--server]'
               '[-p|--port] [-v | --verbose]'))

    parser.add_argument('--index', '-i')
    parser.add_argument('--type', '-t')
    parser.add_argument('--number', '-n', default=1)
    parser.add_argument('--data', '-d', nargs='*')
    parser.add_argument('--server', '-s', default='127.0.0.1')
    parser.add_argument('--port', '-p', default='9200')
    parser.add_argument('--verbose', '-v', action='count')

    args = vars(parser.parse_args())
    print args

    es_host = "http://{server}:{port}".format(server=args['server'],
            port=args['port'])
    es = Elasticsearch(es_host)

    es_fill_data(
            es,
            num=args['number'],
            index=args['index'],
            _type=args['type'],
            keylist=args['data']
            )

