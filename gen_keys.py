from tinyec import registry
import secrets

curve = registry.get_curve("brainpoolP256r1")

def compress_point(point):
    return hex(point.x) + hex(point.y % 2)[2:]

def ecc_calc_encryption_keys(pubkey):
    myPivKey = secrets.randbelow(curve.field.n)
    myPubKey = curve.g * myPivKey
    shared_key = pubkey * myPivKey
    return myPubKey, shared_key

def ecc_calc_decryption_keys(privkey, pubkey):
    shared_key = privkey * pubkey
    return shared_key

privKey = secrets.randbelow(curve.field.n)
otherPubKey = curve.g * privKey
print("My private key: " + hex(privKey))
print("My public key: " + compress_point(otherPubKey))

(myPubKey, shared_key) = ecc_calc_encryption_keys(otherPubKey)
print("Shared key: " + hex(shared_key))
print("My public key: " + compress_point(myPubKey))

decryptKey = ecc_calc_decryption_keys(privKey, otherPubKey)
print("Decryption key: " + compress_point(decryptKey))