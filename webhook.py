import time, requests

wait_seconds = 60 * 2
directories = ['C:/Users/Administrator/Desktop/file.txt']
webhook_url = 'https://discord.com/api/webhooks/1'

notified = []
for directory in directories:
    lines = open(directory, 'r', encoding='utf-8', errors='ignore').read().splitlines()
    notified.extend(lines)

while 1:
    for directory in directories:
        lines = open(directory, 'r', encoding='utf-8', errors='ignore').read().splitlines()
        for line in lines:
            if line not in notified:
                r = requests.post(webhook_url, json={'content': line})
                if r.status_code != 429: # webhook rate limit
                    notified.append(line)
    time.sleep(wait_seconds)