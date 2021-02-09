# youtube-upload-help
A shell script - Uploading multiple videos (dependency: youtube-upload)
- A script for uploading multiple videos only works with youtube-upload (https://github.com/tokland/youtube-upload)

Read the textline in video_list.txt.

Information: 
- YouTube blocks too many upload in a short time rate -> If this happen delete the videos which went online already and execute the script after an hour again.
- The title will be the file name (without .mp4 or something like that)

Set-Up:
- Extract all files in the folder where youtube-upload (https://github.com/tokland/youtube-upload) is located
- Write your paths to the videos in the video_list.txt
- Edit the privacy settings in multiple_upload.py to unlisted/private or public (Default: private)
- Start the script with ./start_upload.sh
- It also works with screen but it will terminate the screen when an error comes up (screen -S upload ./start_upload.sh)

Important: No Spaces in the File Names so before you write the filepaths in the video_list.txt delete the spaces!
- How you replace all spaces with underscores: rename 's/\s/_/g' *
