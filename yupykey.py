# -*- encoding: utf-8 -*-
import requests
import os
import urlparse
import multiprocessing
import time
import math
import random

VERIFY_URLS = ['https://api.yubico.com/wsapi/2.0/verify',
               'https://api2.yubico.com/wsapi/2.0/verify',
               'https://api3.yubico.com/wsapi/2.0/verify',
               'https://api4.yubico.com/wsapi/2.0/verify',
               'https://api5.yubico.com/wsapi/2.0/verify',
               ]


class YuPyKey(object):
    """ Class to handle YubiKey One-Time-Password verification.

    You can get an API Key here:
    https://upgrade.yubico.com/getapikey/

    :type client_id: id
    :param client_id: Yubico API Client ID

    """
    def __init__(self, client_id):
        self.client_id = client_id
        self.res = None

    def _verify_otp(self, index, verify_url, res_queue, otp):
        """ Perform a single request to Yubico API.

        :type index: int
        :param index: Index of the API endpoint

        :type verify_url: str
        :param verify_url: API url

        :type res_queue: multiprocessing.Queue
        :param res_queue: Queue where status result is send

        :type otp: str
        :param otp: one-time-password to verify

        """
        time.sleep(math.log(index+1))
        nonce = os.urandom(16).encode('hex')
        payload = {'id': self.client_id, 'nonce': nonce, 'otp': otp}
        # ssl cert verification with requests
        r = requests.get(verify_url, params=payload, verify=True)
        r.raise_for_status()
        # parsing api result
        res = dict(urlparse.parse_qsl(r.text.replace('\r\n', '&')))
        if not res['status'] in ['BACKEND_ERROR', 'NOT_ENOUGH_ANSWERS']:
            res_queue.put(res['status'])

    def verify_otp(self, otp):
        """ Run queries with multiprocessing.

        :type otp: str
        :param otp: one-time-password to verify

        """
        processs = []
        res_queue = multiprocessing.Queue()
        random.shuffle(VERIFY_URLS)
        for index, api_url in enumerate(VERIFY_URLS):  # start 1 process for each urls
            process = multiprocessing.Process(target=self._verify_otp,
                                              args=[index, api_url, res_queue, otp])
            process.start()
            processs.append(process)

        res = res_queue.get()  # waits until any of the url respond with a status

        for process in processs:
            process.terminate()

        return res

    def verify(self, public_id, otp):
        """ Verify if the one-time-password match the user
        yubikey public id and verify the OTP against Yubico Web API.

        :type public_id: str
        :param public_id: Yubikey public id to verify

        :type otp: str
        :param otp: One-time-password to verify

        :rtype: bool
        :return: True if the OTP is valided, else False

        """
        if otp.startswith(public_id):
            self.res = self.verify_otp(otp)
            if self.res == 'OK':
                return True
        else:
            self.res = 'BAD_CLIENT'
        return False

    def raise_for_status(self):
        res, self.res = self.res, None
        if res and res != 'OK':
            raise Exception(res)
