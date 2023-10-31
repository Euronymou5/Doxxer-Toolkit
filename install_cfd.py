# Cloudflared Install.

import os
import platform
import subprocess
import time

print('\n\033[33mInstalling cloudflare...')

arch = platform.machine()

if 'arm' in arch or 'Android' in arch:
    url = 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm'
elif 'x86_64' in arch:
    url = 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64'
else:
    url = 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-386'

subprocess.run(['wget', url, '-O', 'server/cloudflared'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if os.path.isfile('server/cloudflared'):
   print('\n\033[32mCloudflare installed successfully.')
   os.chmod('server/cloudflared', 0o755)
else:
    print('\n\033[31mAn error occurred when trying to download cloudflared.')
    exit()