import redis
import base64
from finalcheck import predict_output
import os
import pandas as pd

conn = redis.Redis(host='192.168.43.23', port=6379)


def get_id(xread_object):
    try:
        xid = xread_object[0][1][0][0]
    except IndexError:
        return []
    return xid


def get_headers(stream_name, xread_object):

    csv_flow = str(xread_object[0][1][0][1][b'csv']).strip('b').strip("'")
    data = csv_flow.split("\\n")
    headers = data[0].split(",")[0:-1]

    return headers


def parse_stream(stream_name, xread_object):

    csv_flow = str(xread_object[0][1][0][1][b'csv']).strip('b').strip("'")
    data = csv_flow.split("\\n")
    _data = data[1:][0].split(",")
    return _data


def read_redis_stream(stream_name, data):

    xread_object = conn.xread({stream_name: b"0-0"}, count=1)
    xid = get_id(xread_object)
    print(data)
    if xid != []:
        parsed_data = parse_stream(stream_name, xread_object)
        print(parsed_data)
        data.append(parsed_data)
        conn.xdel(stream_name, xid)
        read_redis_stream(stream_name, data)

    return data
    final_df = pd.DataFrame(data, columns=headers)
    return final_df


def make_df(data, headers):


def flow_classify(filename):
    print(predict_output(filename))


df_data_list = read_redis_stream("SAURAV", [])
flow_classify(df_data_list)
