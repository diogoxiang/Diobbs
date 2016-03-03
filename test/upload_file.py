import qiniu
access_key='pUr2s6VcRoB8T0MKe6dmmlhDpQcqacnbJollpdL4'
secret_key='19DhOANFb9vAkb_9o51NPIWdCuvurwjGqDojN6Gl'
bucket_name='9iknow'
q = qiniu.Auth(access_key, secret_key)
key = 'hello'
data = 'hello qiniu!'
token = q.upload_token(bucket_name)
ret, info = qiniu.put_data(token, key, data)
if ret is not None:
    print('All is OK')
else:
    print(info) # error message in info
