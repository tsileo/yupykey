=======
Yupykey
=======

Python `Yubico <http://www.yubico.com/>`_ client to validate YubiKey one-time passwords against the Yubico Web API (implements the  `Validation Protocol Version 2.0 <https://github.com/Yubico/yubikey-val/wiki/ValidationProtocolV20>`_).

* use exclusively SSL and validate the certificat (using `requests <http://www.python-requests.org>`_).
* parallel queries, randomly call all five API endpoint with a slight delay until a server answer.

Possible status
---------------

If an API answer with one of these status: BACKEND_ERROR, NOT_ENOUGH_ANSWERS, Yupikey wait for another answer.

Here are the possible status:

+--------------+-------------------------------+
| Status       | Meaning                       |
+==============+===============================+
| OK           | Valid OTP                     |
+------------+---------------------------------+
| BAD_OTP      | Invalid OTP                   |
+------------+------------+--------------------+
| REPLAYED_OTP | OTP already verified          |
+------------+------------+--------------------+

Yupykey provides one additional status, ``BAD_CLIENT``, when the public id does not match the provided one-time password.

+--------------+-------------------------------+
| Status       | Meaning                       |
+==============+===============================+
| BAD_CLIENT   | Public id and OTP don't match |           |
+------------+---------------------------------+

Overview
========

Yupikey is designed to make YubiKey one-time password validation easy.

::

    from yupikey import Yupykey
    yupikey = Yupikey(YUBICO_APP_ID)

    if yupikey.verify(public_id, otp):
        authenticate_user()
    
    yupikey.raise_for_status()

Requirements
============

* `requests <http://www.python-requests.org>`_

Installation
============

::

    $ pip install yupykey


Usage
=====

Drop
----

::

    $ yampress status



License (MIT)
=============

Copyright (c) 2013 Thomas Sileo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
