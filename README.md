# Claude Code Ping 🔔

Get notified with a sound when Claude Code finishes responding. Perfect for long-running tasks.

## Quick Start

```bash
# Clone and install
git clone https://github.com/yourusername/cc-ping.git
cd cc-ping
uv sync  # or: pip install -r requirements.txt

# Add as Claude Code hook
claude hooks add stop "uv run python /path/to/cc-ping/claude_stop_notifier.py"
```

That's it! You'll now hear a notification sound when Claude finishes.

## Features

- 🔊 Custom notification sound
- 🖥️ macOS native notifications with timestamp
- 📱 Optional mobile notifications via Pushover
- 🎯 Zero configuration required

## Customization

- **Custom sound**: Set `CC_SOUND_FILE` environment variable
- **Notification text**: Edit `title` and `message` in `claude_stop_notifier.py`

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
