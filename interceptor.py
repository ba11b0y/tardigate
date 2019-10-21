from mitmproxy import flowfilter


class Intercept:
    def __init__(self):
        pass

    def response(self, flow):
        print(flow.request.host)
        # flow.intercept()
        print(flow.request.query)
        print(flow.request)
        # flow.resume()
        print(flow.response)


def start():
    return Intercept()
