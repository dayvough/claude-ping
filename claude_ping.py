#!/usr/bin/env python3
import json
import sys
import subprocess
import os
from datetime import datetime
from pathlib import Path

# Load .env file if it exists
env_file = Path(__file__).parent / '.env'
if env_file.exists():
    with open(env_file) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                # Only set if not already in environment
                if key not in os.environ:
                    os.environ[key] = value

def send_mac_notification(title, message, sound_file=None):
    """Send macOS notification with sound"""
    sound_file = sound_file or str(Path(__file__).parent / "notif.mp3")
    
    script = f'''
    tell application "System Events"
        display notification "{message}" with title "{title}"
    end tell
    '''
    subprocess.run(['osascript', '-e', script])
    
    if os.path.exists(sound_file):
        subprocess.run(['afplay', sound_file])


def main():
    # Read input from Claude Code
    input_data = json.loads(sys.stdin.read())
    
    # Check if stop_hook_active to prevent loops
    if input_data.get('stop_hook_active'):
        print(json.dumps({"decision": "approve"}))
        return
    
    # Determine paths to bundled sound files relative to this script
    script_dir = Path(__file__).parent
    default_sound = script_dir / "notif.mp3"
    gilfoyle_sound = script_dir / "You Suffer (Napalm Death).mp3"
    
    # Check if Gilfoyle mode is enabled
    if os.getenv('GILFOYLE_MODE', '').lower() in ('true'):
        sound_file = os.getenv('CC_SOUND_FILE', str(gilfoyle_sound))
    else:
        sound_file = os.getenv('CC_SOUND_FILE', str(default_sound))
    
    # Send notifications
    time_str = datetime.now().strftime('%H:%M:%S')
    title = "Claude Code Finished"
    message = f"Claude completed response at {time_str}"
    
    send_mac_notification(title, message, sound_file)
    
    # Let Claude continue
    print(json.dumps({"decision": "approve"}))

if __name__ == "__main__":
    main()