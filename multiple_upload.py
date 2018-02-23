#!/usr/bin/env python
#multiple_upload.py
import os
import sys
from youtube_upload import main, lib

fpath = sys.argv[1]

title = os.path.basename(fpath)
title = os.path.splitext(title)[0]

args = [
    '--client-secrets=client_secrets.json',
    '--privacy=private',
    '--title=%s' % title,
    fpath,
]

# debug
# print(args)

sys.exit(lib.catch_exceptions(main.EXIT_CODES, main.main, args))
