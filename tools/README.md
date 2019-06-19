# Tools

Here we have tools for interacting with our instances. Please help me expand this. Use asyncio when possible. Thank you.

#### DVSA Multi

- Curl style payload crafter for DVSA
- Uses aiohttp
- Very configurable.

```
 ./dvsatool.py -h
usage: Curl-Style Async HTTP request formatter (originally written for Damn Vulnerable Serverless Appplication)
./dvsatool.py args

       [-h] [-c CONF_FILE] [-v] [-C] [-a AUTH_TOKEN] [-p JSON_PAYLOAD]
       [-u SERVER_URL] [-X--method {GET,POST}] [-H APPEND_HEADERS] [--wtf]

optional arguments:
  -h, --help            show this help message and exit
  -c CONF_FILE, --config CONF_FILE
                        Configuration file holding parameters, CLI overwrite
  -v, --verbose         Increase verbosity of output
  -C, --curl            Output curl command of request
  -a AUTH_TOKEN, --auth_token AUTH_TOKEN
  -p JSON_PAYLOAD, --payload JSON_PAYLOAD
                        Custom parameters to pass (ex:'{"action": "get"}' )
  -u SERVER_URL, --url SERVER_URL
                        DVSA Instance to query. Format: https://<id>.execute-
                        api.<region>.amazonaws.com/<stage>
  -X--method {GET,POST}
                        HTTP request type
  -H APPEND_HEADERS, --header APPEND_HEADERS
                        Additional headers to add to request. Format: "-H
                        Key=Value", Use --verbose to see in more detail. Can
                        be called multiple times: -H Authorization=Allow -H
                        Signature=XXX
  --wtf                 Confused?

````
