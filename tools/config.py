#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Darkerego, 2019
# Config for multi-dvsa

# change these
instance_id = 'aaxxxx'
region = 'us-west-2'
stage = '/dev/order'


server_url = "https://' + 'instance_id' + '.execute-api.' + region + '.amazonaws.com/' + stage
auth_token = '.eyJzdWtWN ... N420pRPJ9nh0w'
payload = '{"action": "get"}'
method = 'POST'

# some other payloads
# payload = '{ "action":"billing", "order-id": "9f51b1e1-eff9-4dc1-8e17-7ee19ba51272", "data": {"ccn": "4242424242424242", "exp": "11/2020", "cvv": "444"} }'
