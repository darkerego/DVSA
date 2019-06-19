from sys import argv, exit
import aiohttp
import asyncio
import argparse
from colorama import Fore, Back, Style

program_name = argv[0]

def output_cmd(line):
    """\
    Function to format text for curl command output
    :param line: text to format
    :return: --
    """
    print(Fore.LIGHTRED_EX + Style.NORMAL + "$ " + line + Style.RESET_ALL)


async def fetch(session, url, auth_token, payload, method, _headers=None, verbose=False, curl=False):
    """\
    main program logic:
    aiohttp request function

    :param session: aiohttp session
    :param url: api endpoint
    :param auth_token: authentication token
    :param payload: post data
    :param method: http method (get, post)
    :param _headers: additional headers to append to request
    :param verbose: increase verbosity (show raw requests, other info)
    :param curl: print curl command for corresponding request
    :return: await response.text()
    """
    headers = {"Authorization": auth_token, "Accept": "*/*", "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) "
                                                          "Gecko/20100101 Firefox/67.0"}
    if _headers:
        if verbose:
            print('Appending headers %s' % _headers)
        headers.update(_headers)  # append additional header specified on CLI
    if verbose:
        print('Raw Request : %s %s %s %s ' % (headers, payload, url, method))

    curl_cmd = str('curl -X %s -H %s --data %s --url %s ' %(method, headers, payload, url))
    if curl:
        print('\nCurl command :\n')
        output_cmd(curl_cmd)
        print('\n')
    if method == 'POST':
        async with session.post(url, data=payload, headers=headers) as response:
            return await response.text()
    elif method == 'GET':
        async with session.get(url, data=payload, headers=headers) as response:
            return await response.text()
    else:
        raise ValueError('Invalid Method Type %s' % method)


def get_args():
    """\
    Helper function to parse CLI args
    :return: args
    """

    usage = "Curl-Style Async HTTP request formatter (originally written for Damn Vulnerable Serverless Appplication)\n"
    usage += "%s args\n" % program_name
    parser = argparse.ArgumentParser(usage)
    parser.add_argument('-c', '--config', dest='conf_file', type=str, default='conf.py', help='Configuration file '
                                                                                              'holding parameters, '
                                                                                              'CLI overwrite')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', default=False, help='Increase '
                                                                                                    'verbosity of'
                                                                                                    ' output')
    parser.add_argument('-C', '--curl', dest='curl', action='store_true', default=False, help='Output curl command of '
                                                                                              'request')
    parser.add_argument('-a', "--auth_token", dest='auth_token', type=str, required=False)
    parser.add_argument('-p', '--payload', dest='json_payload', type=str, default='{"action":"orders"}',
                        help='Custom parameters to pass (ex:\'{"action": "get"}\' )')

    parser.add_argument('-u', '--url', dest='server_url', type=str,
                        help='DVSA Instance to query. Format: https://<id>.execute-api.<region>.amazonaws.com/<stage>')
    parser.add_argument('-X' '--method', dest='method', type=str, choices=['GET', 'POST'], help='HTTP request type')
    parser.add_argument('-H', '--header', dest='append_headers', action=type("", (argparse.Action,), dict(
        __call__=lambda a, p, n, v, o: getattr(n, a.dest).update(dict([v.split('=')])))),
                        default={}, help='Additional headers to add to request. Format: '
                                         '"-H Key=Value", Use --verbose to see in more detail. '
                                         'Can be called multiple times: -H Authorization=Allow -H Signature=XXX ')
    parser.add_argument('--wtf', dest='WTF', action='store_true', help='Confused?')
    args = parser.parse_args()
    return args


async def main():
    """\
    Program start
    :return: --
    """
    args = get_args()
    if args.WTF:
        print('Please see https://github.com/OWASP/DVSA if you are totally confused.')
        exit(1)
    if args.conf_file:
        try:
            import config
        except ImportError:
            print('Cannot find config file %s' % args.config)
        else:
            auth_token = config.auth_token
            payload = config.payload
            url = config.server_url
            method = config.method
    if args.auth_token:
        auth_token = args.auth_token
    if args.json_payload:
        payload = args.json_payload
    if args.server_url:
        url = args.server_url
    if args.method:
        method = args.method
    if args.verbose:
        verbose = True
    else:
        verbose = False
    if args.curl:
        curl = True
    else:
        curl = False
    if args.append_headers:
        append_headers = args.append_headers
    else:
        append_headers = None
    if verbose:
        
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url, auth_token, payload, method, append_headers, verbose, curl)
        print('Sent HTTP request to %s now...' % url)
        print(html)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
