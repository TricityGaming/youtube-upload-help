#!/bin/bash
cat video_list.txt | while read FILE; do python multiple_upload.py "$FILE" || break; done
