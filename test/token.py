import jwt

encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')

token = jwt.decode(encoded, 'secret', algorithms=['HS256'])

if __name__ == '__main__':
    print(encoded)
    print(token)
