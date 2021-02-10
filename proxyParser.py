directory = 'proxies.txt'

with open(directory) as k:
    initProxies = k.read().splitlines()

usingProxies = False
proxies = []

try:
    for proxy in initProxies:
        proxy = proxy.split(':')
        ip = proxy [0]
        port = proxy[1]
        try:
            user = proxy[2]
            password = proxy[3]
            finProxy = {'http':'http://'+user+':'+password+'@'+ip+':'+port, 'https':'http://'+user+':'+password+'@'+ip+':'+port}
        except:
            finProxy = {'http':'http://'+ip+':'+port, 'https':'http://'+ip+':'+port}
        proxies.append(finProxy)
except Exception as e:
    log('Error parsing proxies. Exiting')
    log(str(e))

if len(proxies) != 0:
    log('Successfully loaded '+str(len(proxies))+' proxies from '+str(directory))
    usingProxies = True
else:
    log('Loaded 0 proxies. Running localhost')
