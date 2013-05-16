.. YuPyKey documentation master file, created by
   sphinx-quickstart on Mon May 13 20:21:15 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

YuPyKey: Python Yubico client
=============================

.. raw:: html

    <p>
    <span style="width:100px;float:left;">
      <iframe src="http://ghbtns.com/github-btn.html?user=tsileo&repo=yupykey&type=watch&count=true&size=small"
        allowtransparency="true" frameborder="0" scrolling="0" width="200px" height="35px"></iframe>
    </span><span style="width:100px;float:left;">    
    <a href="https://twitter.com/share" class="twitter-share-button" data-url="http://yupykey.readthedocs.org" data-text="Bakthat: Python Yubico Client" data-via="trucsdedev">Tweet</a>
    <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script></span></p>
    <p style="clear:left"></p>

.. module:: yupykey

Release v\ |version|.

Python `Yubico <http://www.yubico.com/>`_ client to validate YubiKey one-time passwords against the Yubico Web API (implements the  `Validation Protocol Version 2.0 <https://github.com/Yubico/yubikey-val/wiki/ValidationProtocolV20>`_).

* use exclusively SSL and validate the certificat (using `requests <http://www.python-requests.org>`_).
* parallel queries, randomly call all five API endpoint with a slight delay until a server answer.

Installation
============

::

    $ pip install yupykey


Requirements
============

* `requests <http://www.python-requests.org>`_


Usage
=====

Yupikey is designed to make YubiKey one-time password validation easy.

::

    from yupikey import Yupykey
    yupikey = Yupikey(YUBICO_APP_ID)

    if yupikey.verify(public_id, otp):
        authenticate_user()
    
    yupikey.raise_for_status()


Possible status
---------------

If an API answer with one of these status: ``BACKEND_ERROR``, ``NOT_ENOUGH_ANSWERS``, Yupikey wait for another answer.

Here are the possible status:

+--------------+-------------------------------+
| Status       | Meaning                       |
+==============+===============================+
| OK           | Valid OTP                     |
+--------------+-------------------------------+
| BAD_OTP      | Invalid OTP                   |
+--------------+-------------------------------+
| REPLAYED_OTP | OTP already verified          |
+--------------+-------------------------------+

Yupykey provides one additional status, ``BAD_CLIENT``, when the public id does not match the provided one-time password.

+--------------+-------------------------------+
| Status       | Meaning                       |
+==============+===============================+
| BAD_CLIENT   | Public id and OTP don't match |
+--------------+-------------------------------+


API
---

.. autoclass:: yupykey.YuPyKey
   :members:


Articles
--------

* `Add yours <http://google.com>`_

Feedback
--------

Please don't hesitate to `contact me <http://thomassileo.com/about/>`_ if you want to leave feedback, criticism, or to ask whatever questions you have.

License (MIT)
-------------

Copyright (c) 2013 Thomas Sileo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
