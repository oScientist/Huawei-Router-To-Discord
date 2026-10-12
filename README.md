# Huawei Router Discord Bot 🌐🤖 (Huawei Router HS8545M5)

A custom Discord bot built using `discord.py` that interfaces with Huawei routers via a companion framework (`HuaweiDiscordFramework`) to manage network settings, MAC filtering, wireless access, and device lists directly through Discord commands.

## 🛠️ Features

* 🔒 **MAC Filter Control**: Enable or disable the router's MAC filtering instantly.

* 📶 **Wireless Network Toggle**: Turn the router's Wi-Fi network on or off.

* 📋 **Device Management**: View logged DHCP clients and the current MAC whitelist.

* ➕➖ **Whitelist Modification**: Add or remove device MAC addresses or indices dynamically.

* 🔄 **Router Reboot**: Remotely trigger a system reboot of the router.

* 📡 **Startup Logging**: Automatically logs bot initialization details and device metrics to a designated Discord channel.

## 📋 Prerequisites

* **Python**: Version 3.8 or higher.

* **Discord Bot Token**: Created via the Discord Developer Portal with appropriate intents (`Intents.all()`).

* **Companion Framework**: `HuaweiDiscordFramework` module installed locally or in your project path.

## 🚀 Getting Started

### 1. Installation

Clone or download the project files into your working directory, ensuring `main_bot.py` and `HuaweiDiscordFramework.py` are in the same folder.

Install the required dependencies:

```
pip install requirements.txt

```

### 2. Configuration

Open `main_bot.py` and insert your Discord Bot Token into the `TOKEN` variable:

```
TOKEN = "your_discord_bot_token_here"

```

### 3. Run the Bot

Execute the script via your terminal:

```
python main_bot.py

```

## 💬 Command Reference

The bot uses the exclamation mark (`!`) prefix. Below are the available commands:

| **Command** | **Arguments** | **Description** | 
| `!on` | *None* | Enables the router's MAC filter. | 
| `!off` | *None* | Disables the router's MAC filter. | 
| `!dhcp` | *None* | Displays a list of currently logged DHCP devices. | 
| `!whitelist` | *None* | Shows the list of whitelisted devices. | 
| `!add` | `<mac_address>` | Adds a specific MAC address to the whitelist. | 
| `!remove` | `<indexnumber>` | Removes a device from the whitelist by index. | 
| `!wlan` | `<on/off>` | Turns the wireless network on or off. | 
| `!help` | *None* | Displays the list of available commands. | 
| `!restart` | *None* | Reboots the Huawei router. | 

## ⚠️ Security Warning

* Keep your Discord Bot Token strictly confidential. Never commit your token to public version control systems like GitHub.

* Ensure that the bot runs on a secure local environment that has proper network access to your router gateway (`192.168.100.2`).

## 
