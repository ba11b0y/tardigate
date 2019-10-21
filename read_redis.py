import redis
import base64
from finalcheck import predict_output

conn = redis.StrictRedis(host='192.168.43.23', port=6379)


def read_and_decode_from_redis(msg):
    decoded_fname = base64.b64decode(msg)
    with open("test.csv", "wb") as f:
        f.write(decoded_fname)


def flow_classify(filename):
    print(predict_output(filename))


def subscription_loop():

    sub = conn.pubsub()
    sub.subscribe("test")

    try:

        while True:
            message = sub.get_message()
            if message and message["type"] == "message":
                read_and_decode_from_redis(message['data'])
                flow_classify("test.csv")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    subscription_loop()
