import hashlib  



def shorten_url(long_url):
    short_url_hash = hashlib.sha256(long_url.encode()).hexdigest()[:6]
    short_url = short_url_hash
    
    return short_url  
