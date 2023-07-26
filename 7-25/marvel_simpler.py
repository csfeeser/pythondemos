import time
import hashlib

def main():

    with open("marvel.pub") as pubkey:
        pubkey= pubkey.read().rstrip("\n")
        # this should have our public key

    with open("marvel.priv") as privkey:
        privkey= privkey.read().rstrip("\n")
    
    ts= time.time()
    ts= str(ts)

                # OOPS!
    combined= ts + privkey + pubkey

    print("TIMESTAMP:", ts)
    print("PRIVATE:", privkey)
    print("PUBLIC:", pubkey)
    print("COMBINED STRING:", combined)

    # encode the string
    combined= combined.encode("utf-8")

    hashed= hashlib.md5(combined)

    hashed= hashed.hexdigest()

    print("HASH:", hashed)

    # using an F string to pull together all the queries into a proper URL
    url= f"http://gateway.marvel.com/v1/public/comics?ts={ts}&apikey={pubkey}&hash={hashed}"

    print(url)
    
main()
