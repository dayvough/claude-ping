#!/usr/bin/env python3
import json
import sys
import subprocess
import os
import requests
from datetime import datetime

def send_mac_notification(title, message, sound_file=None):
    """Send macOS notification with sound"""
    sound_file = sound_file or "/Users/dayvough/Projects/ai/claude/cc-ping/notif.mp3"
    # sound_file = sound_file or "/System/Library/Sounds/Glass.aiff"
    
    script = f'''
    tell application "System Events"
        display notification "{message}" with title "{title}"
    end tell
    '''
    subprocess.run(['osascript', '-e', script])
    
    if os.path.exists(sound_file):
        subprocess.run(['afplay', sound_file])

def send_phone_notification(title, message, pushover_token=None, pushover_user=None):
    """Send notification to phone via Pushover"""
    if not pushover_token or not pushover_user:
        return
    
    data = {
        "token": pushover_token,
        "user": pushover_user,
        "title": title,
        "message": message,
        "sound": "cosmic",
        "priority": 1
    }
    
    try:
        requests.post("https://api.pushover.net/1/messages.json", data=data)
    except:
        pass

def main():
    # Read input from Claude Code
    input_data = json.loads(sys.stdin.read())
    
    # Check if stop_hook_active to prevent loops
    if input_data.get('stop_hook_active'):
        print(json.dumps({"decision": "approve"}))
        return
    
    # Get config from environment or defaults
    sound_file = os.getenv('CC_SOUND_FILE', '/Users/dayvough/Projects/ai/claude/cc-ping/notif.mp3')
    pushover_token = os.getenv('PUSHOVER_TOKEN')
    pushover_user = os.getenv('PUSHOVER_USER')
    
    # Send notifications
    time_str = datetime.now().strftime('%H:%M:%S')
    title = "Claude Code Finished"
    message = f"Claude completed response at {time_str}"
    
    send_mac_notification(title, message, sound_file)
    send_phone_notification(title, message, pushover_token, pushover_user)
    
    # Let Claude continue
    print(json.dumps({"decision": "approve"}))

if __name__ == "__main__":
    main()