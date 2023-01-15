import urllib.parse
import requests
import sys

print("python3 ubifuzz.py domain")
combinations = []
for i in range(256):
    binary = format(i, '08b')
    if "00" in binary and binary != "11111111":
        encoded = urllib.parse.quote(binary) # URL encode the binary string
        url = sys.argv[1] + encoded # Append the encoded binary string to the URL
        response = requests.get(url) # Send a GET request to the URL
        if binary in response.text: # Check if the binary string is reflected in the response
            print("")
            print(f"Reflected value found: {binary} with encoding: URL in url: {url} with a length of {len(response.content)}")
        else:
            for enc in ['hex','base64','quopri','uu','rot13','url','ascii']:
                try:
                    encoded = eval("urllib.parse."+enc+"(binary)")
                    url = sys.argv[1] + encoded # Append the encoded binary string to the URL
                    response = requests.get(url) # Send a GET request to the URL
                    if binary in response.text: # Check if the binary string is reflected in the response
                        print("")
                        print(f"Reflected value found: {binary} with encoding: {enc} in url: {url} with a length of {len(response.content)}")
                        break
                    else:
                        print("")
                        print(f"Reflected value not found: {binary} in url: {url} with a length of {len(response.content)}")
                except:
                    pass
    else:
        encoded = urllib.parse.quote("11111111") # URL encode the binary string
        url = sys.argv[1] + encoded # Append the encoded binary string to the URL
        response = requests.get(url) # Send a GET request to the URL
        if binary in response.text: # Check if the binary string is reflected in the response
            print("")
            print(f"Reflected value found: {binary} with encoding: URL in url: {url} with a length of {len(response.content)}")
        else:
            for enc in ['hex','base64','quopri','uu','rot13','url','ascii']:
                try:
                    encoded = eval("urllib.parse."+enc+"(binary)")
                    url = sys.argv[1] + encoded # Append the encoded binary string to the URL
                    response = requests.get(url) # Send a GET request to the URL
                    if binary in response.text: # Check if the binary string is reflected in the response
                        print("")
                        print(f"Reflected value found: {binary} with encoding: {enc} in url: {url} with a length of {len(response.content)}")
                        break
                    else:
                        print("")
                        print(f"Reflected value not found: {binary} in url: {url} with a length of {len(response.content)}")
                except:
                    pass
