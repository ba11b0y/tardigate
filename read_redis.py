import redis
import base64
from finalcheck import predict_output

conn = redis.Redis(host='192.168.43.23', port=6379)


def read_and_decode_from_redis(key):
    file_name_b64 = conn.lpop(key)
    decoded_fname = base64.b64decode(file_name_b64)
    with open("test.csv", "wb") as f:
        f.write(decoded_fname)


def flow_classify(filename):
    print(predict_output(filename))


flow_classify("test.csv")
