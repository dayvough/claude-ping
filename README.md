# Claude Code Ping 🔔

Get notified with a sound when Claude Code finishes responding. Perfect for
long-running tasks.

## Quick Start

````bash
# Clone and install
git clone https://github.com/yourusername/claude-ping.git
cd claude-ping
uv sync  # or: pip install -r requirements.txt

# Configure Claude Code settings
# Add to ~/.claude/settings.json:
```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "uv run python /path/to/claude-ping/claude_ping.py"
          }
        ]
      }
    ]
  }
}

# Set GILFOYLE_MODE=true if you want the best experience
"GILFOYLE_MODE=true uv run python /path/to/claude-ping/claude_ping.py"
````

That's it! You'll now hear a notification sound when Claude finishes.

## Features

- 🔊 Custom notification sound
- 🖥️ macOS native notifications with timestamp
- 📱 Optional mobile notifications via Pushover
- 🎯 Zero configuration required

## Customization

- **Custom sound**: Set `CC_SOUND_FILE` environment variable
- **Gilfoyle mode**: Set `GILFOYLE_MODE=true` to use "You Suffer.mp3" (the
  shortest song ever)
- **Notification text**: Edit `title` and `message` in `claude_ping.py`

### Gilfoyle Mode

For the
[true Silicon Valley experience](https://www.youtube.com/watch?v=uS1KcjkWdoU):

```bash
export GILFOYLE_MODE=true
```

This switches the notification sound to "You Suffer.mp3". Make sure to add this
file to the project directory.

## Pushover Setup (Optional)

For mobile notifications:

1. Create a [Pushover](https://pushover.net/) account
2. Create an application in Pushover to get your API token
3. Copy `.env.example` to `.env` and fill in your credentials:

   ```bash
   cp .env.example .env
   # Edit .env with your Pushover credentials
   ```

## Requirements

- macOS (uses `afplay` and AppleScript)
- Python 3.8+
- Claude Code CLI

## License

MIT
