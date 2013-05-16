import os
import sys
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "yupykey",
    version = "0.1.0",
    author = "Thomas Sileo",
    author_email = "thomas.sileo@gmail.com",
    description = "",
    license = "MIT",
    keywords = "",
    url = "https://github.com/tsileo/yupykey",
    py_modules=['yupykey'],
    long_description= read('README.rst'),
    install_requires=["requests",],
    entry_points={'console_scripts': ["yammpress = yammpress:main"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    scripts=["yupykey.py"],
#    zip_safe=False,
)
