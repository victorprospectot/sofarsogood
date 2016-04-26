def encriptar_rsa(message):
	from Crypto.PublicKey import RSA
	public_key_text = open('./public_key.pem', 'rb').read()
	public_key = RSA.importKey(public_key_text)
	return public_key.encrypt(message,32)[0]


def desencriptar_rsa(message):
	from Crypto.PublicKey import RSA
	private_key_text = open('./private_key.pem', 'rb').read()
	private_key = RSA.importKey(private_key_text)
	return private_key.decrypt(message)

def encriptar_mensaje(message):
	import base64
	return base64.encodestring(encriptar_rsa(message))

def desencriptar_mensaje(message):
	import base64
	return desencriptar_rsa(base64.decodestring(message))
