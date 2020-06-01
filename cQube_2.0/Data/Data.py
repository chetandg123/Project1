import base64


class credentials():
    URL = "http://52.66.209.6:4200/#/login"
    username = base64.b64decode("dGliaWxzb2x1dGlvbnNAY3F1YmUuY29t").decode("utf-8")
    password = base64.b64decode("dGliaWwxMjM=").decode("utf-8")
