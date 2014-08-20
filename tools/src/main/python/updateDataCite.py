import httplib2, sys, base64, codecs
 
if (len(sys.argv) < 2):
    raise Exception('Please provide username and password')

# Set up the HTTP client:
h = httplib2.Http()
auth_string = base64.encodestring(sys.argv[1] + ':' + sys.argv[2])

 
# Read the doi.resolve file:
body_unicode = codecs.open("doi.resolve", 'r', encoding='utf-8').read().strip()

# Get the DOI:
doi = body_unicode.split("\n")[0].split("=")[1].strip()

# Test mode?
test_mode = ""
#test_mode = "?testMode=true"

# Check if the DOI already exists, and modify update method accordingly:
url = 'https://mds.datacite.org/doi/' + doi + test_mode
method = 'PUT'
response, content = h.request(url, 'GET', headers={'Authorization':'Basic ' + auth_string})
if response.status/100 == 2:
    method = 'POST'

# Send the DOI-to-URL mapping:
print("Sending "+doi+" "+method+" due to "+str(response.status))
print(body_unicode);

response, content = h.request(url, method,
                              body = body_unicode.encode('utf-8'),
                              headers={'Content-Type':'text/plain;charset=UTF-8',
                                       'Authorization':'Basic ' + auth_string})
if (response.status != 201):
    print str(response.status)
 
print(content.decode('utf-8'))

# Check if the metadata already exists, and modify update method accordingly:
url = 'https://mds.datacite.org/metadata/' + doi + test_mode
method = 'PUT'
response, content = h.request(url, 'GET', headers={'Authorization':'Basic ' + auth_string})
if response.status/100 == 2:
    method = 'POST'

# Now send the metadata:
print("Sending metadata for "+doi+" due to "+method+" "+str(response.status))
body_unicode = codecs.open("doi.xml", 'r', encoding='utf-8').read().strip()
response, content = h.request(url, method,
                              body = body_unicode.encode('utf-8'),
                              headers={'Content-Type':'application/xml;charset=UTF-8',
                                       'Authorization':'Basic ' + auth_string})
if (response.status != 201):
    print str(response.status)
 
print(content.decode('utf-8'))