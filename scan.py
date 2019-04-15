#!/usr/bin/python3
import os
import subprocess
import json


def webapp_iter():
    resource_json = subprocess.check_output([ 'az', 'webapp', 'list' ])

    webapps = json.loads(resource_json)

    for webapp in webapps:
        yield webapp


if __name__ == '__main__':
    for webapp in webapp_iter():
        webapp_name = webapp['name']
        hostname = webapp_name + '.azurewebsites.net'
        target = 'https://' + hostname
        print('Scanning', target)
        resource_group_name = webapp['resourceGroup']
        subprocess.check_output([
            'docker',
            'run',
            '--volume',
            os.getcwd() + ':/zap/wrk',
            '--tty',
            'coderpatros/zap-scanner:1-latest',
            target
        ])
        os.rename('zap-junit.xml', hostname + '.junit.xml')
    else:
        print('No web apps found in subscription.')
