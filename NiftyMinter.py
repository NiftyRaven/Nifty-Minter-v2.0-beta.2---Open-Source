
"""
 _   _  _____  _____  ____  __      __  _   _ 
| \ | ||  ___||_   _||  _ \ \ \    / / | \ | |
|  \| || |_     | |  | |_) | \ \  / /  |  \| |
| |\  ||  _|    | |  |  _ <   \ \/ /   | |\  |
|_| \_||_|      |_|  |_| \_\   \__/    |_| \_|
+=============================================

NiftyMinter - Open Source Release
==================================

Description:
------------
NiftyMinter is an innovative NFT minting tool designed to seamlessly integrate with the Ravencoin blockchain. It allows users to mint, manage, and trade NFTs effortlessly, providing an interactive and user-friendly interface.

Licensing Information:
-----------------------
This software is released under the MIT License, a permissive free software license that puts very few restrictions on reuse, making it a great choice for open-source projects.

MIT License
-----------
Copyright (c) 2024 NiftyRaven.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Distribution:
-------------
NiftyMinter is distributed in the hope that it will be useful for the community. Contributions are welcome to enhance its features and functionality. You can find the repository and contribute at [GitHub Repository URL].

Donation Addresses:
-------------------
If you find this software useful and would like to support the development and maintenance of NiftyMinter, please consider donating to the following addresses:

- **Community Marketplace (NiftyRaven Rewards Wallet):**
  [REr5yJZXanH1r8TK5BACwsGhq3qBrt78rQ](https://explorer.mangofarmassets.com/address/REr5yJZXanH1r8TK5BACwsGhq3qBrt78rQ)

- **Developer Donation Address:**
  [RWSHne54VgbWyNj3c2Um3Utu1GzDcmuNiX](https://explorer.mangofarmassets.com/address/RWSHne54VgbWyNj3c2Um3Utu1GzDcmuNiX)

Thank you for your support and contributions!

Be awesome, keep minting, stay NIFTY!

"""


########################################################################################################################
########################################################################################################################
# IMPORTS & INITIAL SETUP START
############################################################################################################
############################################################################################################
import os  # Operating system related functions (e.g., file handling).
import discord  # Main Discord library.
import requests  # HTTP requests.
import json  # JSON encoding and decoding.
from discord.ext import commands  # Bot commands extension for Discord.
from bitcoin import random_key, privkey_to_pubkey, pubkey_to_address  # Bitcoin key and address functions.
import base64  # Base64 encoding and decoding.
import datetime  # Date and time functions.
import ravencoin  # Ravencoin related functions (unspecified module).
import asyncio  # Asynchronous I/O.
import re  # Regular expressions for string matching.
import random  # Random number generation.
from discord.ext import tasks  # Background task extension for Discord.
from requests.structures import CaseInsensitiveDict  # Case insensitive dictionaries for HTTP headers.
import aiohttp  # Asynchronous HTTP requests.
import io  # Input/output operations.
from bs4 import BeautifulSoup  # HTML/XML parsing.
from flask import Flask, request, jsonify  # Flask web framework for creating web applications.
import threading  # Thread-based parallelism.
from collections import defaultdict  # Default dictionary for key-value pairs.
from discord import ButtonStyle, Embed, Color, User  # Discord UI elements.
from discord.ui import Button, View, Modal, TextInput  # Discord UI elements.
import pytz  # Timezone calculations.
import urllib.parse  # URL parsing.
import matplotlib.pyplot as plt  # Plotting library.
from io import BytesIO  # Byte streams for I/O.
import time  # Time access and conversions.
from tempfile import NamedTemporaryFile  # Temporary files.
import aiofiles  # Asynchronous file I/O.
from pathlib import Path  # Path manipulation.
import subprocess  # Subprocess management.
from bitcoinrpc.authproxy import AuthServiceProxy  # Bitcoin JSON-RPC.
import hashlib  # Hashing algorithms.
import ravencoin_issuance  # Custom module for Ravencoin issuance (assumed).


############################################################################################################
# IMPORTS & INITIAL SETUP END
############################################################################################################
############################################################################################################
########################################################################################################################
########################################################################################################################
# GLOBAL VARIABLES START
########################################################################################################################

# Create bot instance
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents)
bot.remove_command('help')

# Global variables that might be unnecessary & outdated
user_addresses = {}
MINT_ADDRESS = "REr5yJZXanH1r8TK5BACwsGhq3qBrt78rQ"
MINT_FEE = 15

# Set the channel IDs for posting messages
MESSAGE_CHANNEL_ID = 1094831496566689802
BTC_CHANNEL = 1215094224035381278  # Replace with the ID of the channel for posting messages
NAME_UPDATE_CHANNEL_ID = 1066548111067058266  # Replace with the ID of the channel for updating the name


# Set the channel IDs for posting messages
ACTIVE_CHANNELS_FILE = 'active_channels.json'
USER_DATA_FILE = "C:/Users/neron/Documents/NFTRVN Token Bot/user_data.json"

# Set your bot token and Ravencoin node credentials here
TOKEN = 'your_token'
RPC_USER = "user" # Replace with your RPC username in config file
RPC_PASSWORD = "password" # Replace with your RPC password in config file
RPC_IP = "127.0.0.1" # Replace with your RPC IP address in config file
RPC_PORT = 8766 # Replace with your RPC port in config file
RPC_URL = "http://127.0.0.1:8766" # Replace with your RPC URL in config file

#Global variable needs to be reviewed
filename = 'my_file.txt' 

# API credentials
RAVENCOIN_API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=ravencoin&vs_currencies=usd"
API_PIN_BY_CID_ENDPOINT = "/pinning/pinFileToIPFS"
API_PIN_FILE_ENDPOINT = "/pinning/pinFileToIPFS"  # Endpoint for pinning a file
API_PIN_JSON_ENDPOINT = "/pinning/pinJSONToIPFS"

# Pinata API credentials
PINATA_API_KEY = "your_key_here"
PINATA_API_SECRET = "your_secret_here"
API_BASE_URL = "https://api.pinata.cloud"
API_PIN_BY_HASH_ENDPOINT = "/pinning/pinByHash"
PINATA_JWT = "your_jwt_here"
api_token = "your_token_here" # Replace with your API token for your pinata gateway

# Maximum file size and character limit
MAX_SIZE_BYTES = 75000000  # 75MB is the current limit
MAX_FILE_SIZE = 35 * 1_000_000   # 35MB is the current limit
CHAR_LIMIT = 2000

# Flask app
app = Flask(__name__)
USER_DATA_PATH = "C:/Users/neron/Documents/NFTRVN Token Bot/user_data.json"
base_info_url = "https://www.igraffit.com/rvn/asset-info.php?asset="




# Set the channel IDs for posting messages
VIP_ELITE_ROLE_IDS = {1145495368839204925, 1015723816921612308}
list_channel_id = 1237637061855547463
TESTCHANNEL_ID = 1237939399380045886
UPDATE_MSG_ID = None  # Stores the message ID of the update message

# Headers for Pinata API
headers = {
    "Authorization": f"Bearer {PINATA_JWT}"
}

# Random messages - Used for help & advertising.
# Combined random messages list
random_messages = [
    "https://www.igraffit.com",
    "CHECK THE CURRENT REWARDS FOR NIFTYRAVEN.COM ASSET HOLDERS - https://explorer.mangofarmassets.com/address/RXwFMLkQ6VmsxLtnyiNnyxiDYbHZYeKTDd",
    "An example of an NFT name for minting: Nifty_Raven_Car_1  -  The result of !mint with this nft name = NFTRVN#Nifty_Raven_Car_1",
    "http://rocketraven.net/faucet",
    "https://nftrvn.net/ - IN DEVELOPMENT - AUTONOMOUS WEBSITE",
    "Ravencoin assets can only have 30 characters... NFTRVN# takes up 7 of those 30. This means you can create an asset 23 characters long here.",
    "I can't WAIT until Cronenberg Gang Game is released!",
    "https://www.igraffit.com/",
    "To list all the addresses of a certain asset, type !listaddresses assetname, or to get the # of addresses holding an asset with top 10 holder list, type ?addresses assetname",
    "Want to see transactions of a specific address? Type: ?gettxs rvn_address>",
    "Want to see the last 4 transactions in the NFTRVN wallet? Type !listtransactions",
    "Want to invite me to your DISCORD? [Click Here for INFO](https://niftyraven.com/nifty-minter%E2%84%A2)",
    "RavenAngles is a project of RVN that reserves Main-Asset names, without potential future projects getting scalped.",
    "Did you know that this Discord was built by the NFTRVN community from the ground up...100% Organically.",
    "Tip: If minting with me, try to organize your assets minted by standardizing your asset/NFT names. Example: NFTRVN#Nifty_MushroomTat1, NFTRVN#Nifty_MushroomTat2, etc...",
    "CHECK THE CURRENT REWARDS FOR NIFTYRAVEN.COM/VIP HOLDERS & NIFTYRAVEN.COM/HELPER - https://explorer.mangofarmassets.com/address/REr5yJZXanH1r8TK5BACwsGhq3qBrt78rQ",
    "CHECK OUT: https://meco.eeconme.com/",
    "Did you know The Humble Miner has a game that on iPhone/Android where you can collect RVN NFTs and mine for PKBIT!",
    "Type ?getinfo assetname to retrieve asset information DIRECTLY from the Blockchain!",
    "Get the market cap with ?getmarketcap!",
    "Get the market info with ?marketinfo!",
    "Check asset messages or messages sent to an RVN address by typing ?getmsgs address",
    "Mint your own NFT with ?mint",
    "For help on available commands, type ?helpme",
    "Start the asset issuance process by typing ?issue_asset_view",
    "Buy or list tokens by typing ?NFTRVN",
    "Set the active channel for notifications by typing ?setactivechannel",
    "See the leaderboard of top minters by typing ?leaderboard",
    "Check the number of guilds by typing ?guildcount",
    "Get guild-specific address information by typing ?guildinfo",
    "Fetch the list of nodes by typing ?getnodes",
    "Check the balance of an address by typing ?get_balance address",
    "Unlock the wallet for transactions by typing ?unlockwallet",
    "Pin an IPFS hash with a name by typing ?pin ipfs_hash",
    "List your Ravencoin tokens by typing ?listtokens",
]

########################################################################################################################
# GLOBAL VARIABLES END
########################################################################################################################

############################################################################################################
#################################################
#################################################
############################################################################################################
########################################################################################################################
########################################################################################################################
# DEFINITIONs START
############################################################################################################
##
#NOT ASYNCRONOUS DEFINITIONS
##
#loads user data from the json file - change location if using
def load_user_data():
    """
    Loads user data from a JSON file, ensuring the file exists.
    """
    if not os.path.exists(USER_DATA_PATH):
        return {"users": {}}  # Return an empty template if the file doesn't exist

    with open(USER_DATA_PATH, "r") as file:
        return json.load(file)

#saves user data to the json file - change location if using
def save_user_data(user_data):
    """
    Saves user data to a JSON file with pretty formatting.
    """
    with open(USER_DATA_PATH, "w") as file:
        json.dump(user_data, file, indent=4)

#gets the user's address from the user data - change location if using
def get_user_address(user_id):
    """
    Retrieves a user's Ravencoin address from the loaded user data.
    """
    user_data = load_user_data()
    return user_data["users"].get(str(user_id), {}).get("address")

#gets rvn price
def get_ravencoin_price():
    response = requests.get(RAVENCOIN_API_URL)
    data = response.json()
    return data["ravencoin"]["usd"]

#gets rvn to btc price
def get_rvn_to_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ravencoin&vs_currencies=btc"
    response = requests.get(url)
    data = response.json()
    return data["ravencoin"]["btc"]


#load processed txids
def load_processed_txids():
    try:
        with open("processed_txids.txt", "r") as file:
            processed_txids = set(file.read().splitlines())
    except FileNotFoundError:
        processed_txids = set()
    return processed_txids




#save processed txids
def save_processed_txid(txid):
    with open("processed_txids.txt", "a") as f:
        f.write(f"{txid}\n")


#create a new asset explorer link
def create_asset_explorer_link(asset_name):
    encoded_asset_name = custom_url_encode(asset_name)
    return f"https://ravencoin.asset-explorer.net/a/{encoded_asset_name}"


# Add this function to save payment data to a file
def save_payment_data(asset_name, price, address):
    with open("payments.txt", "a") as f:
        f.write(f"{asset_name}:{price}:{address}\n")


# Validates i[fs hash
def is_valid_ipfs_hash(ipfs_hash):
    return len(ipfs_hash) == 46 and ipfs_hash.startswith("Qm")


# Validates asset name
def is_valid_asset_name(asset_name):
    return 1 <= len(asset_name) <= 13 and re.match(r'^[\w\.]+$', asset_name)


# Validates asset quantity
def process_transaction_details(tx_details, address):
    rvn_received = rvn_sent = 0
    assets_received = {}
    assets_sent = {}
    involved_addresses = set()

    for vin in tx_details.get('vin', []):
        if vin.get('address'):
            involved_addresses.add(vin['address'])
            # Assume rvn_sent is gathered from another source, as 'vin' doesn't provide value details

    for vout in tx_details.get('vout', []):
        script_pub_key = vout.get('scriptPubKey', {})
        if 'addresses' in script_pub_key:
            for addr in script_pub_key['addresses']:
                involved_addresses.add(addr)
                if addr == address:
                    rvn_received += vout.get('value', 0)
                    if 'asset' in script_pub_key:
                        asset_name = script_pub_key['asset'].get('name')
                        asset_amount = script_pub_key['asset'].get('amount', 0)
                        assets_received[asset_name] = assets_received.get(asset_name, 0) + asset_amount

    # Ensure that all elements in involved_addresses are strings
    involved_addresses = [str(addr) for addr in involved_addresses if addr is not None]

    # Now you can safely join them
    return rvn_received, rvn_sent, assets_received, assets_sent, ', '.join(involved_addresses)


# Get involved addresses
def get_involved_addresses(tx_details):
    involved_addresses = set()
    for vin in tx_details['vin']:
        if 'address' in vin:
            involved_addresses.add(vin['address'])
    for vout in tx_details['vout']:
        if 'addresses' in vout.get('scriptPubKey', {}):
            involved_addresses.update(vout['scriptPubKey']['addresses'])
    return ', '.join(involved_addresses)


# Parse transaction details
def parse_transaction_details(tx_details, address):
    message = ""
    for vin in tx_details.get('vin', []):
        message += f"Source Transaction ID: {vin.get('txid')}, Output Index: {vin.get('vout')}\n"

    for vout in tx_details.get('vout', []):
        value = vout.get('value', 0)
        addresses = vout['scriptPubKey'].get('addresses', [])
        asset_info = vout['scriptPubKey'].get('asset', {})
        asset_name = asset_info.get('name', 'RVN')
        asset_amount = asset_info.get('amount', value)

        message += f"Recipient Addresses: {', '.join(addresses)} - Amount: {asset_amount} {asset_name}\n"

    return message


# Verify the user is an admin
def is_admin():
    async def predicate(ctx):
        return ctx.author.guild_permissions.administrator
    return commands.check(predicate)


# Create a new Ravencoin address
def create_new_address():
    result = call_rpc("getnewaddress")
    if result is None or "result" not in result:
        return None
    return result["result"]


# Validate a Ravencoin address
def is_valid_ravencoin_address(address):
    if len(address) >= 26 and len(address) <= 36 and address.startswith('R'):
        return True
    return False


# Load payment data
def load_payment_data():
    payment_data = []
    with open("payments.txt", "r") as f:
        for line in f:
            parts = line.strip().split(":")
            if len(parts) == 3:
                asset_name, price, address = parts
                payment_data.append({"asset_name": asset_name, "price": float(price), "address": address})
            else:
                print(f"Error reading payment data: incorrect line format - {line.strip()}")
    return payment_data
    return None


# RPC CALL FUNCTION #1
def call_rpc(method, params=None):
    headers = {'content-type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "id": "1",
        "method": method,
    }
    if params:
        payload["params"] = params

    auth = (RPC_USER, RPC_PASSWORD)
    try:
        response = requests.post(RPC_URL, auth=auth, headers=headers, data=json.dumps(payload))
        return response.json()
    except Exception as e:
        print(f"Error calling RPC method {method}: {str(e)}")
        return None


# RPC CALL FUNCTION #2
def rpc_call(method, params=None):
    headers = {'content-type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "id": "1",
        "method": method,
        "params": params or []
    }

    auth = (RPC_USER, RPC_PASSWORD)
    try:
        response = requests.post(RPC_URL, auth=auth, headers=headers, data=json.dumps(payload))
        return response.json()
    except Exception as e:
        print(f"Error calling RPC method {method}: {str(e)}")
        return None


# Load user data from a JSON file #2
def load_user1_data(file_path):
    """
    Synchronously loads user data from a JSON file.
    """
    with open(file_path, "r") as file:
        return json.load(file)


# Load token sales data
def load_token_data():
    path = "token_sales_data.json"
    if not os.path.exists(path):
        return {}
    with open(path, "r") as file:
        return json.load(file)


# Save token sales data
def save_token_data(data):
    with open("token_sales_data.json", "w") as file:
        json.dump(data, file, indent=4)


# Log a token sale
def log_token_sale(token_name, seller_id, buyer_id, sale_price, quantity):
    data = load_token_data()
    if token_name not in data:
        data[token_name] = {
            "sales": [],
            "listings": []
        }
    data[token_name]["sales"].append({
        "seller_id": seller_id,
        "buyer_id": buyer_id,
        "sale_price": sale_price,
        "quantity": quantity,
        "date": datetime.now().isoformat()
    })
    save_token_data(data)


# List a token for sale
def list_token(token_name, seller_id, price, quantity):
    data = load_token_data()
    if token_name not in data:
        data[token_name] = {"sales": [], "listings": []}
    data[token_name]["listings"].append({
        "seller_id": seller_id,
        "price": price,
        "quantity": quantity,
        "date": datetime.now().isoformat()
    })
    save_token_data(data)


# Run the Flask app in a separate thread
def run_flask():
    app.run(host='0.0.0.0', port=5000)


# Determine the file extension based on the MIME type
def determine_file_extension(content_type):
    # Map MIME types to file extensions
    mime_type_mapping = {
        "image/jpeg": "jpg",
        "image/png": "png",
        "image/gif": "gif",
        "video/mp4": "mp4",
        "application/pdf": "pdf"
    }
    return mime_type_mapping.get(content_type, "bin")  # Default to .bin if unknown


# Pin a file to IPFS
def pin_item(ipfs_hash, nft_name):
    data = {
        "hashToPin": ipfs_hash,
        "pinataMetadata": {"name": nft_name}
    }
    try:
        response = requests.post(API_BASE_URL + API_PIN_BY_HASH_ENDPOINT, json=data, headers=headers)
        if response.status_code == 200:
            return True, response.json()  # Success
        else:
            print(f"Error during pinning: {response.text}")
            return False, response.text  # Error message
    except requests.RequestException as e:
        print(f"Exception during pinning: {e}")
        return False, str(e)  # Error message


# Update the asset data with new information
def update_asset_data(asset_name, update_data):
    # Replace invalid filename characters in asset name
    safe_asset_name = asset_name.replace('/', '-').replace('#', '_')
    file_name = f"{safe_asset_name}.json"

    asset_data = None
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            asset_data = json.load(file)
        # Check if 'last_sold' key exists; if not, initialize it
        if 'last_sold' not in asset_data:
            asset_data['last_sold'] = 0  # Initialize last sold price to 0 if it doesn't exist
    else:
        # Create new asset data if file doesn't exist
        asset_data = {
            'name': asset_name,
            'last_sold': 0,  # Initialize last sold price to 0 for new listings
            'other_data': {},  # Include other necessary initial data
        }

    # Update the asset data with the new information
    asset_data.update(update_data)

    # Example condition to update last sold price, modify as necessary
    if some_condition_to_update_last_sold:
        asset_data['last_sold'] = update_data.get('last_price', asset_data['last_sold'])

    # Save the updated asset data back to the file
    with open(file_name, 'w') as file:
        json.dump(asset_data, file, indent=4)


# Encode custom URL
def custom_url_encode(asset_name):
    """
    Custom URL encoding to match the Ravencoin Asset Explorer's requirements.
    """
    # Start by URL encoding the asset name
    encoded = urllib.parse.quote(asset_name, safe='')
    # Additional replacements for specific characters
    encoded = encoded.replace('%23', '#')  # Replacing encoded '#' back to '#'
    encoded = encoded.replace('%2F', '/')  # Replacing encoded '/' back to '/'
    encoded = encoded.replace('%2C', ',')  # Replacing encoded ',' back to ','
    return urllib.parse.quote(asset_name).replace('%23', '#').replace('%2F', '/').replace('%2C', ',')


# Fetch the current price and total assets for a specified asset
def get_current_price_and_assets(asset_name, listings):
    # Filter the listings to only include those for the specified asset_name
    asset_listings = [listing for listing in listings if listing['asset_name'] == asset_name]

    # Get the most recent listing for the asset (assuming listings are sorted by time)
    if asset_listings:
        latest_listing = asset_listings[-1]
        current_price = latest_listing['price_per_unit']
        total_assets = sum(listing['asset_balance'] for listing in asset_listings)
        return current_price, total_assets
    else:
        # Return default values if no listings found for the asset
        return "Unknown", 0


# Get Guilds Channel congiguration
def get_channel_config():
    try:
        with open('channel_config.json', 'r') as file:
            config = json.load(file)
        return config
    except FileNotFoundError:
        return {}


# Load active channels from the file
def load_active_channels():
    try:
        with open('active_channels.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Save active channels to the file
def save_active_channels(active_channels):
    with open('active_channels.json', 'w') as file:
        json.dump(active_channels, file, indent=4)


# Set the active channel for the specified guild
def set_channel_config(guild_id, channel_id):
    try:
        with open('channel_config.json', 'r') as file:
            config = json.load(file)
    except FileNotFoundError:
        config = {}

    config[str(guild_id)] = str(channel_id)

    with open('channel_config.json', 'w') as file:
        json.dump(config, file, indent=4)


# Load the guilds info from the file
def load_guilds_info():
    with open('guilds_info.json', 'r') as f:
        return json.load(f)


##
##############################################################################################
##
# ASYNCRONOUS DEFINITIONS START
##

# RPC CALL FUNCTION #1 ASYNC
async def call_rvn_rpc(method, params):
    async with aiohttp.ClientSession(auth=aiohttp.BasicAuth(RPC_USER, RPC_PASSWORD)) as session:
        headers = {'Content-Type': 'application/json'}
        data = {
            "jsonrpc": "1.0",
            "id": "discord",
            "method": method,
            "params": params  # Ensure this is a list with the correct parameters
        }

        async with session.post(RPC_URL, headers=headers, json=data) as response:
            response_json = await response.json()

            # Debug logs
            print(f"RPC Request: {json.dumps(data)}")
            print(f"RPC Response: {response_json}")

            return response_json


# RPC CALL FUNCTION #2 ASYNC
async def rvn_call_rpc(method, params):
    async with aiohttp.ClientSession(auth=aiohttp.BasicAuth(RPC_USER, RPC_PASSWORD)) as session:
        headers = {'Content-Type': 'application/json'}
        data = {
            "jsonrpc": "1.0",
            "id": "discord",
            "method": method,
            "params": params  # Ensure this is a list with the correct parameters
        }

        try:
            async with session.post(RPC_URL, headers=headers, json=data) as response:
                response_json = await response.json()

                return response_json
        except aiohttp.ClientError as e:
            # Handle any client-side errors (e.g., network issues)
            print(f"Error during RPC request: {e}")
            return None
        except asyncio.TimeoutError:
            # Handle timeout errors
            print("RPC request timed out")
            return None
        except Exception as e:
            # Handle any other unexpected errors
            print(f"Unexpected error during RPC request: {e}")
            return None


# Fetch assets received in a transaction
async def fetch_assets_received(txid: str):
    url = f"https://explorer.mangofarmassets.com/api/tx/{txid}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                assets_received = []
                for vout in data['vout']:
                    if 'assets' in vout:
                        for asset in vout['assets']:
                            assets_received.append((asset['name'], asset['amount']))
                return assets_received
            return None


# fetch transactions of an address
async def fetch_transactions(address):
    url = f"https://explorer.mangofarmassets.com/api/txs/?address={address}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            return None


# confirms connection to discord
async def confirm_connection():
    await bot.wait_until_ready()
    print('Connected to Discord API!')


# Sending Large Messages - Split the message into chunks of 2000 characters
async def send_large_message(ctx, message):
    # Split the message into chunks of 2000 characters
    for i in range(0, len(message), CHAR_LIMIT):
        chunk = message[i:i + CHAR_LIMIT]
        await ctx.send(chunk)


# Fetch transaction details
async def fetch_transaction_details(txid):
    try:
        # Fetch the raw transaction data
        raw_tx_response = rpc_call("getrawtransaction", [txid, False])  # False for getting hex string
        if not raw_tx_response or 'result' not in raw_tx_response:
            print(f"Failed to fetch raw transaction for txid: {txid}")
            return None

        # Extract the hex string of the transaction
        tx_hex = raw_tx_response['result']

        if not tx_hex:
            print(f"No hex string found in transaction data for txid: {txid}")
            return None

        # Decode the raw transaction using the hex string
        decoded_tx_response = rpc_call("decoderawtransaction", [tx_hex])
        if not decoded_tx_response or 'result' not in decoded_tx_response:
            print(f"Failed to decode transaction for txid: {txid}")
            return None

        # The result itself is the decoded transaction details
        tx_details = decoded_tx_response['result']
        return tx_details
    except Exception as e:
        print(f"Exception in fetch_transaction_details: {str(e)}")
        return None


#generate and check payment
async def gen_and_chk_payment(interaction, price):
    payment_address_response = await call_rvn_rpc("getnewaddress", [])
    if 'result' not in payment_address_response:
        await interaction.channel.send("Error generating payment address. Please try again.")
        return None, None

    payment_address = payment_address_response['result']
    await interaction.channel.send(f"{interaction.user.mention}, send your payment of {price} RVN to the following address: {payment_address}")

    timeout = time.time() + 20 * 60  # 20 minutes timeout
    payment_received = 0

    while time.time() < timeout:
        await asyncio.sleep(15)  # Wait for 15 seconds before checking for new transactions
        transactions = await call_rvn_rpc("listtransactions", [])

        for tx in transactions.get('result', []):
            if tx["address"] == payment_address and tx["category"] == "receive":
                payment_received += tx["amount"]
                if payment_received >= price:
                    # Full or over-payment received
                    if payment_received > price:
                        # Send back the change
                        change = payment_received - price
                        await refund_payment(interaction, change, payment_address)
                        payment_received = price  # Reset to the exact price after change
                    # Return payment_received and payment_address if the correct amount or more is received
                    return payment_received, payment_address

        # If we reach this point, payment is incomplete. Check if the user wants to proceed or refund
        if payment_received > 0 and payment_received < price:
            remaining_amount = price - payment_received
            await interaction.channel.send(f"{interaction.user.mention}, a partial payment of {payment_received} RVN has been received. "
                                           f"Please send the remaining {remaining_amount} RVN to complete the payment.")
            proceed = await ask_user_to_proceed(interaction)
            if not proceed:
                await refund_payment(interaction, payment_received, payment_address)
                return None, None

    # If the timeout is reached and no full payment is made, refund any received amount and return None
    if payment_received > 0:
        await refund_payment(interaction, payment_received, payment_address)
    await interaction.channel.send(f"{interaction.user.mention}, the payment process has timed out. Any received funds have been refunded.")
    return None, None


# Refund payment
async def refund_payment(ctx, amount, address):

    refund_txid_response = call_rpc("sendfromaddress", ["R9ssT21TmkgDsdJYCcmfv3qnuoREzzZvzk", address, amount])

    if 'result' in refund_txid_response:
        refund_txid = refund_txid_response['result']
        await ctx.send(f"{ctx.author.mention}, a refund of {amount} RVN has been sent back to the address: {address}. "
                       f"Transaction ID: https://explorer.mangofarmassets.com/tx/{refund_txid}")
    else:
        await ctx.send(f"{ctx.author.mention}, there was an error processing your refund. Please contact support.")


# Upload and mint process - Proceed Verification
async def ask_user_to_proceed(ctx):
    # Send a message to ask the user to proceed or not
    msg = await ctx.send(f"{ctx.author.mention}, do you want to proceed with the partial payment? (yes/no)")
    # Wait for a response
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ['yes', 'no']
    try:
        response = await bot.wait_for('message', check=check, timeout=60)  # 60 seconds to respond
        if response.content.lower() == 'yes':
            return True
        else:
            return False
    except asyncio.TimeoutError:
        await ctx.send(f"{ctx.author.mention}, you did not respond in time.")
        return False


# Upload and mint process - Minting Main Assets
async def mint_mainasset(asset_name, quantity, units, reissuable, address):
    try:
        # Unlock the wallet for 60 seconds
        await call_rvn_rpc("walletpassphrase", ["135790", 6000])

        await interaction.response.defer(ephemeral=True)
        print("Handling Payment.")
        await handle_payment(interaction, user_address)
        print("Attempting to proceed with minting, payment received.")

        await upload_and_mint_process(interaction, user_address)
        # Prepare parameters for the 'issue' RPC call
        params = [asset_name, quantity, address, "", units, reissuable, False, ""]

        # Issue the asset on the Ravencoin blockchain
        response = await call_rvn_rpc("issue", params)

        # Check if the minting was successful
        if response and 'result' in response:
            txid = response['result']
            print(f"Minting successful with txid = {txid}")
            return True, txid  # Operation successful
        else:
            print("Minting failed.")
            return False, "Minting failed or no transaction ID returned."

    except Exception as e:
        # Log the exception and return failure
        print(f"Exception in mint_mainasset: {e}")
        return False, str(e)  # Return indicating the operation failed along with the error message


# Upload and mint process - Handles Payment
async def handle_payment(ctx_or_interaction, user_address):
    # Example price
    price = 25
    payment_received, payment_address = await gen_and_check_payment(ctx_or_interaction, price)

    if not payment_received:
        await send_message(ctx_or_interaction, "Payment not received or verification failed.")
        return

    from_address = "RG3RxHpUQm14vY1mDZvHNCkfH4eZhjS6eZ"
    #await call_rvn_rpc("walletpassphrase", ["Password1!", 60000000000])  # Unlock the wallet for 60 seconds
    # Assuming payment was successful, proceed with transferring assets
    token_result = await call_rvn_rpc("transferfromaddress", ["NIFTYRAVEN.COM", from_address, 15, user_address, "", 0, "", from_address])
    if token_result is None or "result" not in token_result:
        await send_message(ctx_or_interaction, "Error sending NIFTYRAVEN.COM asset.")
        return

    token_txid = token_result['result']
    await send_message(ctx_or_interaction, f"You just received: 15 NIFTYRAVEN.COM! Transaction ID: <https://explorer.mangofarmassets.com/tx/{token_txid}>")

    # Load guild info from JSON file
    with open("guilds_info.json", "r") as f:
        guild_info = json.load(f)

    # Extract guild ID
    guild_id = str(ctx_or_interaction.guild.id if hasattr(ctx_or_interaction, 'guild') else ctx_or_interaction.channel.guild.id)
    guild_addresses = guild_info.get(guild_id, {})

    # Define transactions using the loaded addresses
    transactions = [
        {"address": guild_addresses.get("token_helpers"), "amount": 5, "description": "Token Helpers"},
        {"address": guild_addresses.get("guild"), "amount": 6, "description": "Ref"},
        {"address": guild_addresses.get("ref"), "amount": 7.5, "description": "Guild"}
    ]

    # Process each transaction
    for txn in transactions:
        if txn["address"]:  # Only process if the address is found
            send_rvn_result = await call_rvn_rpc("sendfromaddress", [payment_address, txn["address"], txn["amount"]])
            if send_rvn_result is not None or "result" in send_rvn_result:
                guild_txid = send_rvn_result['result']
                await send_message(ctx_or_interaction, f" {txn['amount']} Ravencoin from minting this Unique Asset (NFT) went to: {txn['description']} --> Address: {txn['address']} txid:{guild_txid}. >")
            if send_rvn_result is None or "result" not in send_rvn_result:
                await send_message(ctx_or_interaction, f"Error sending {txn['amount']} RVN to {txn['description']} ({txn['address']}).")
                continue  # Continue attempting other transactions even if one fails

    await send_message(ctx_or_interaction, "All transactions processed successfully.")


# Upload and mint process - Handles Payment of Main Assets
async def handle_mainassetpymt(ctx_or_interaction, user_address):
    # Example price
    price = 650
    payment_received, payment_address = await gen_and_check_payment(ctx_or_interaction, price)

    if not payment_received:
        await send_message(ctx_or_interaction, "Payment not received or verification failed.")
        return

    from_address = "RG3RxHpUQm14vY1mDZvHNCkfH4eZhjS6eZ"
    #await call_rvn_rpc("walletpassphrase", ["Password1!", 60000000000])  # Unlock the wallet for 60 seconds
    # Assuming payment was successful, proceed with transferring assets
    token_result = await call_rvn_rpc("transferfromaddress", ["NIFTYRAVEN.COM", from_address, 225, user_address, "", 0, "", from_address])
    if token_result is None or "result" not in token_result:
        await send_message(ctx_or_interaction, "Error sending NIFTYRAVEN.COM asset.")
        return

    token_txid = token_result['result']
    await send_message(ctx_or_interaction, f"You just received: 15 NIFTYRAVEN.COM! Transaction ID: <https://explorer.mangofarmassets.com/tx/{token_txid}>")

    # Load guild info from JSON file
    with open("guilds_info.json", "r") as f:
        guild_info = json.load(f)

    # Extract guild ID
    guild_id = str(ctx_or_interaction.guild.id if hasattr(ctx_or_interaction, 'guild') else ctx_or_interaction.channel.guild.id)
    guild_addresses = guild_info.get(guild_id, {})

    # Define transactions using the loaded addresses
    transactions = [
        {"address": guild_addresses.get("token_helpers"), "amount": 25, "description": "Token Helpers"},
        {"address": guild_addresses.get("guild"), "amount": 50, "description": "Ref"},
        {"address": guild_addresses.get("ref"), "amount": 75, "description": "Guild"}
    ]

    # Process each transaction
    for txn in transactions:
        if txn["address"]:  # Only process if the address is found
            send_rvn_result = await call_rvn_rpc("sendfromaddress", [payment_address, txn["address"], txn["amount"]])
            if send_rvn_result is not None or "result" in send_rvn_result:
                guild_txid = send_rvn_result['result']
                await send_message(ctx_or_interaction, f" {txn['amount']} Ravencoin from minting this Unique Asset (NFT) went to: {txn['description']} --> Address: {txn['address']} txid:{guild_txid}. >")
            if send_rvn_result is None or "result" not in send_rvn_result:
                await send_message(ctx_or_interaction, f"Error sending {txn['amount']} RVN to {txn['description']} ({txn['address']}).")
                continue  # Continue attempting other transactions even if one fails

    await send_message(ctx_or_interaction, "All transactions processed successfully.")


# Send a message to the user or interaction
async def send_message(ctx_or_interaction, message):
    if isinstance(ctx_or_interaction, discord.Interaction):
        await ctx_or_interaction.channel.send(message)
    else:
        await ctx_or_interaction.send(message)


# Function to fetch address group information
async def fetch_address_group(group_id, with_address_list=0):
    url = f"https://rvn.cryptoscope.io/api/getaddressgroup/?groupid={group_id}&withaddresslist={with_address_list}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                return None


# Function to fetch market capitalization
async def fetch_market_capitalization():
    url = "https://rvn.cryptoscope.io/api/getmarketcapitalization/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data
            else:
                return None


# Function to mint - Not used
async def mint_auto(interaction, ipfs_hash, asset_name):
    call_rpc("walletpassphrase", ["135790", 6000])  # Unlock the wallet for 60 seconds

    # Implementation of the minting logic
    try:
        result = await mint2(interaction, ipfs_hash, asset_name)  # Assuming this function exists and is asynchronous
        await interaction.followup.send(f"Minting successful: {result}", ephemeral=True)
    except Exception as e:
        await interaction.followup.send(f"Error during minting: {str(e)}", ephemeral=True)

# Generate and check payment #2
async def gen_and_check_payment(ctx_or_interaction, price):
    payment_address_response = await call_rvn_rpc("getnewaddress", [])
    if 'result' not in payment_address_response:
        await send_message(ctx_or_interaction, "Error generating payment address. Please try again.")
        return None, None

    payment_address = payment_address_response['result']
    await send_message(ctx_or_interaction, f"{ctx_or_interaction.user.mention}, send your payment of {price} RVN to the following address: {payment_address}")

    timeout = time.time() + 20 * 60  # 20 minutes timeout
    payment_received = 0

    while time.time() < timeout:
        await asyncio.sleep(15)  # Wait for 15 seconds before checking for new transactions
        transactions = await call_rvn_rpc("listtransactions", [])

        for tx in transactions.get('result', []):
            if tx["address"] == payment_address and tx["category"] == "receive":
                payment_received += tx["amount"]
                if payment_received >= price:
                    # Full or over-payment received
                    if payment_received > price:
                        # Send back the change
                        change = payment_received - price
                        await refund_payment(ctx_or_interaction, change, payment_address)
                        payment_received = price  # Reset to the exact price after change
                    # Return payment_received and payment_address if the correct amount or more is received
                    return payment_received, payment_address

        # If we reach this point, payment is incomplete. Check if the user wants to proceed or refund
        if payment_received > 0 and payment_received < price:
            remaining_amount = price - payment_received
            await send_message(ctx_or_interaction, f"{ctx_or_interaction.user.mention}, a partial payment of {payment_received} RVN has been received. "
                                                  f"Please send the remaining {remaining_amount} RVN to complete the payment.")
            proceed = await ask_user_to_proceed(ctx_or_interaction)
            if not proceed:
                await refund_payment(ctx_or_interaction, payment_received, payment_address)
                return None, None

    # If the timeout is reached and no full payment is made, refund any received amount and return None
    if payment_received > 0:
        await refund_payment(ctx_or_interaction, payment_received, payment_address)
    await send_message(ctx_or_interaction, f"{ctx_or_interaction.user.mention}, the payment process has timed out. Any received funds have been refunded.")
    return None, None


    """
async def gen_and_check_payment(ctx, price):
    payment_address_response = await call_rvn_rpc("getnewaddress", [])
    if 'result' not in payment_address_response:
        await ctx.send("Error generating payment address. Please try again.")
        return None, None

    payment_address = payment_address_response['result']
    await ctx.send(f"{ctx.author.mention}, send your payment of {price} RVN to the following address: {payment_address}")

    timeout = time.time() + 20 * 60  # 20 minutes timeout
    payment_received = 0

    while time.time() < timeout:
        await asyncio.sleep(15)  # Wait for 15 seconds before checking for new transactions
        transactions = await call_rvn_rpc("listtransactions", [])

        for tx in transactions.get('result', []):
            if tx["address"] == payment_address and tx["category"] == "receive":
                payment_received += tx["amount"]
                if payment_received >= price:
                    # Full or over-payment received
                    if payment_received > price:
                        # Send back the change
                        change = payment_received - price
                        await refund_payment(ctx, change, payment_address)
                        payment_received = price  # Reset to the exact price after change
                    # Return payment_received and payment_address if the correct amount or more is received
                    return payment_received, payment_address

        # If we reach this point, payment is incomplete. Check if the user wants to proceed or refund
        if payment_received > 0 and payment_received < price:
            remaining_amount = price - payment_received
            await ctx.send(f"{ctx.author.mention}, a partial payment of {payment_received} RVN has been received. "
                           f"Please send the remaining {remaining_amount} RVN to complete the payment.")
            proceed = await ask_user_to_proceed(ctx)
            if not proceed:
                await refund_payment(ctx, payment_received, payment_address)
                return None, None

    # If the timeout is reached and no full payment is made, refund any received amount and return None
    if payment_received > 0:
        await refund_payment(ctx, payment_received, payment_address)
    await ctx.send(f"{ctx.author.mention}, the payment process has timed out. Any received funds have been refunded.")
    return None, None
"""


# Check existing assets
async def check_existing_assets(prefix):
    print(f"Checking for existing assets that start with the given {prefix} on the Ravencoin blockchain.")
    asset_pattern = f"{prefix}*"

    try:
        rpc_response = await call_rvn_rpc("listassets", [asset_pattern, True])  # True for verbose to get all details
        if "result" in rpc_response:
            existing_assets = [asset for asset in rpc_response["result"]]
            print(f"Existing assets: {existing_assets}")

            return existing_assets
        else:
            print("RPC response is missing the 'result' key.")
            return []
    except Exception as e:
        print(f"An error occurred while checking existing assets: {e}")
        return []


# Get the next asset number
async def get_next_asset_number(existing_assets, prefix):
    # Extract numbers from existing assets and find the maximum
    numbers = []
    for asset in existing_assets:
        try:
            number = int(asset.replace(prefix, "").split(".")[1])  # Assumes format "prefix.name.number"
            numbers.append(number)
        except (IndexError, ValueError):
            continue  # Skip assets that do not match the expected format

    if numbers:
        return max(numbers) + 1
    else:
        return 1  # Start with 1 if no existing assets found


# Downloads the image to mint
async def download_image(image_url, temp_filename):
    async with aiohttp.ClientSession() as session:
        async with session.get(image_url) as response:
            if response.status == 200:
                # Open the temporary file with aiofiles for async write
                async with aiofiles.open(temp_filename, 'wb') as temp_file:
                    await temp_file.write(await response.read())
                return True
            else:
                print("Failed to download the image: Status", response.status)
                return False


# Pin the image to IPFS
async def pin_image_to_ipfs(image_path):
    print("PINNING...")
    pinata_api_url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_API_SECRET,
    }

    if not Path(image_path).is_file():
        logging.error(f"File not found: {image_path}")
        return None

    try:
        # Correct multipart/form-data usage
        data = aiohttp.FormData()
        data.add_field('file', open(image_path, 'rb'), filename=Path(image_path).name)

        async with aiohttp.ClientSession() as session:
            async with session.post(pinata_api_url, headers=headers, data=data) as response:
                if response.status == 200:
                    response_json = await response.json()
                    ipfs_hash = response_json.get("IpfsHash")
                    print(f"Image pinned successfully: {ipfs_hash}")
                    return ipfs_hash
                else:
                    logging.error(f"Failed to pin image to IPFS: {response.status}")
                    return None
    except Exception as e:
        logging.exception("Exception occurred while pinning image to IPFS:", exc_info=e)
        return None


# Pin image to IPFS from URL
async def pin_image_to_ipfs_from_url(image_url):
    # Use NamedTemporaryFile for creating a temp file, but only use its name for async operations
    with NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_filename = temp_file.name

    try:
        if await download_image(image_url, temp_filename):
            ipfs_hash = await pin_image_to_ipfs(temp_filename)
            return ipfs_hash
        else:
            return None
    finally:
        # Ensure the temporary file is always removed after use
        if os.path.exists(temp_filename):
            os.remove(temp_filename)


# Mint asset
async def mint_asset(ctx, asset_name, ipfs_hash, user_address):
    try:
        # Configuration for the root name of the asset
        root_name = "NFTRVN"
        call_rpc("walletpassphrase", ["135790", 6000])  # Unlock the wallet for 60 seconds
        # Preparing data for the 'issueunique' RPC call
        asset_tags = [asset_name]  # Tags for the unique assets
        ipfs_hashes = [ipfs_hash]  # IPFS hashes associated with each tag

        # Issue unique asset on the Ravencoin blockchain
        mint_response = await call_rvn_rpc("issueunique", [root_name, asset_tags, ipfs_hashes])

        # Check if the minting was successful
        if mint_response and 'result' in mint_response and mint_response['result']:
            mint_txid = mint_response['result'][0]  # Assume txid is the first item in 'result'
            print(f"Minting successful with txid = {mint_txid}")

            # Wait for the minting transaction to be confirmed
            confirmed = await confirm_transaction(ctx, mint_txid)
            if not confirmed:
                return False, "Minting transaction not confirmed."

            # Construct the full asset name for transfer
            full_asset_name = f"{root_name}#{asset_name}"

            # Transfer the minted asset to the specified user address
            transfer_response = await call_rvn_rpc("transfer", [full_asset_name, 1, user_address])

            # Check if the transfer was successful
            if transfer_response and 'result' in transfer_response:
                transfer_txid = transfer_response['result']
                print(f"Asset transferred successfully with txid = {transfer_txid}")
                return True, transfer_txid  # Operation successful
            else:
                print("Asset transfer failed.")
                return False, "Asset transfer failed or no transaction ID returned."
        else:
            print("Minting failed.")
            return False, "Minting failed or no transaction ID returned."

    except Exception as e:
        # Log the exception and return failure
        print(f"Exception in mint_asset: {e}")
        return False, str(e)  # Return indicating the operation failed along with the error message


# Confirm transaction
async def confirm_transaction(mint_txid, timeout=600):

    # Send initial message to indicate waiting for confirmation

    start_time = asyncio.get_event_loop().time()
    while (asyncio.get_event_loop().time() - start_time) < timeout:
        response = await call_rvn_rpc("gettransaction", [mint_txid])
        if response["result"]["confirmations"] >= 1:
            print(f"TXID: {mint_txid} confirmed.")
            return True
        else:
            # Update loading message every few seconds instead of waiting silently
            elapsed_time = int(asyncio.get_event_loop().time() - start_time)

            await asyncio.sleep(10)  # Check every 10 seconds

    # If the loop exits due to timeout, update the message to indicate failure
    return False


# Post to thread
async def post_to_thread(thread_id, message, image_url=None):
    # Fetch the thread by ID
    thread = bot.get_channel(thread_id)

    if thread is None or not isinstance(thread, discord.Thread):
        print("Thread not found or the channel is not a thread.")
        return


# Fetch asset details- WIP
async def fetch_asset_details(asset_name):
    try:
        # Call the 'getassetdata' RPC method
        result = await call_rvn_rpc("getassetdata", [asset_name])
        if result and "result" in result:
            return result["result"]
        else:
            print("Error: Asset data not found or invalid response.")
            return None
    except Exception as e:
        print(f"Error fetching asset data: {str(e)}")
        return None


# Fetch tokens for user - WIP
async def fetch_tokens_for_user(address):
    # Placeholder function to simulate fetching tokens from a database or an API
    return {"TokenA/SubAsset": 100.12345678, "TokenB": 50.0}


# Send a message to the user or interaction
async def send_message_to_discord(channel_id, message):
    channel = bot.get_channel(int(channel_id))
    await channel.send(message)


# Verify transaction
async def verify_transaction(txid, address, amount):
    transaction = call_rpc("gettransaction", [txid])
    if transaction is None or "result" not in transaction or not transaction["result"]:
        return False

    details = transaction["result"]["details"]
    for detail in details:
        if detail["address"] == address and detail["category"] == "send" and detail["amount"] == -amount:
            return True

    return False


# Sends random message from Random Messages Global Variable
async def send_random_message(channel_id):
    channel = bot.get_channel(channel_id)
    random_message = random.choice(random_messages)
    await channel.send(random_message)


# Retrieve or create message
async def retrieve_or_create_message(bot):
    global UPDATE_MSG_ID
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print("Channel not found.")
        return

    try:
        if UPDATE_MSG_ID:
            return await channel.fetch_message(UPDATE_MSG_ID)
        else:
            message = await channel.send("Initializing asset tracking...")
            UPDATE_MSG_ID = message.id
            return message
    except discord.NotFound:
        # Message not found, send a new one
        message = await channel.send("Initializing asset tracking...")
        UPDATE_MSG_ID = message.id
        return message


# Update listing message
async def update_listing_message(bot, asset_name, listed_price, last_sold_price, last_purchase_time, last_amount_purchased):
    message = await retrieve_or_create_message(bot)
    content = f"**Asset Name:** {asset_name}\n" \
              f"**Listed Price:** {listed_price}\n" \
              f"**Last Sold Price:** {last_sold_price}\n" \
              f"**Last Purchased Time:** {last_purchase_time}\n" \
              f"**Last Amount Purchased:** {last_amount_purchased} units"
    await message.edit(content=content)


# Timer to reset on sale - NOT USED
async def timer_reset_on_sale(bot):
    while True:
        # This should be triggered by an event when a sale is made
        last_purchase_time = datetime.now()
        # Update the listing message with the last purchase time
        await update_listing_message(bot, "AssetName", 100, 95, last_purchase_time.strftime("%Y-%m-%d %H:%M:%S"), 10)
        await asyncio.sleep(60)  # Check every minute if you need to reset


# Example of usage inside an event - NOT USED
async def on_sale_made(bot, asset_name, sale_price, units_sold):
    # Call update function with new details
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    await update_listing_message(bot, asset_name, 100, sale_price, current_time, units_sold)


# Upload and mint process - Monitors and checks the created address for assets from the user
async def monitor_asset_transfer(interaction, new_address, user_address):
    print(f"Running monitor assets.")
    print(f"Entering loop for address: {new_address} for user: {user_address}.")
    for _ in range(10):  # 10 minutes loop
        print(f"Loop Entered.")

        asset_name, asset_balance = await wait_for_asset_balance(new_address)
        print(f"Wait for asset = PASSED")
        print(f"RESULTS OF WAITING: BALANCE: {asset_balance} ASSET NAME: {asset_name} at NEW ADDRESS: {new_address}.")
        print(f"Lets see if this asset {asset_name} has been Listed at NiftyRaven before.")

        if asset_balance:
            await interaction.followup.send(
                f'Processing the listing... Checking to see if this asset: {asset_name} has ever been listed before at NFTRVN.')
            asset_data = await call_rvn_rpc("getassetdata", [asset_name])  # Use dynamic asset name
            print(asset_data)

            # Check if 'result' key exists and is a dictionary
            if 'result' in asset_data and isinstance(asset_data['result'], dict):
                result_data = asset_data['result']
                # Filter out unwanted keys using dictionary comprehension
                extracted_data = {key: result_data.get(key, '') for key in ['name', 'units', 'amount', 'ipfs_hash', 'has_ipfs', 'reissuable']}
                print(f"Extracted data: {extracted_data}")
            else:
                extracted_data = {'name': '', 'units': 0, 'amount': 0, 'ipfs_hash': '', 'has_ipfs': 0, 'reissuable': 0}
                print("No result data found.")

            print(f"Lets see if this asset {asset_name} has been Listed at NiftyRaven before. CHECKING ACCOUNTS")
            units = extracted_data['units']
            account_address = await get_or_create_asset_account(extracted_data['name'], new_address)  # Use dynamic asset name
            # Convert units to decimal
            decimal_units = 10 ** (-units)
            await interaction.followup.send(
                f"Asset Data:\n"
                f"- Name: {extracted_data['name']}\n"
                f"- Units: {decimal_units} ({units})\n"
                f"- IPFS Hash: {extracted_data['ipfs_hash']}\n"
                f"- Total Supply: {extracted_data['amount']}{decimal_units}\n"
                f"- NiftyDEX Address: {account_address}"
            )

            print(
                f"Checking the user's listing price for {asset_name} at {account_address} for seller: {user_address}."
            )

            lot_price = await ask_for_price(interaction, asset_balance)
            print(f"Lot_Price: {lot_price}")
            price_per_unit = lot_price / asset_balance

            total_price = price_per_unit * asset_balance
            print(f"Total price for {asset_balance} units: {total_price}")

            # Ask the user for confirmation before listing at the specified price
            confirmation_message = (
                f"Do you want to list the following assets?\n"
                f"- Asset: {extracted_data['name']}\n"
                f"- Quantity: {asset_balance} units\n"
                f"- Price per {decimal_units} {extracted_data['name']}: {price_per_unit} RVN\n"
                f"- Total price: {total_price} RVN\n"
                f"Type 'yes' to confirm."
            )
            await interaction.followup.send(confirmation_message)

            def check(message):
                return message.author == interaction.user and message.channel == interaction.channel

            # Wait for user confirmation
            confirm = await bot.wait_for('message', timeout=160.0, check=check)

            if confirm.content.lower() == 'yes':
                account = await transfer_asset(extracted_data['name'], new_address, asset_balance, account_address, channel=interaction.channel)
                print(account)
                await interaction.followup.send(f'Assets Transferred to {account}, This address for all {extracted_data["name"]} Tokens listed on NFTRVN. Processing the listing... Even further')
                await asyncio.sleep(10)
                # Handle confirmation logic

                channel = bot.get_channel(1213694827305238528)  # Channel ID for the listings
                author = interaction.user.display_name  # Use interaction's user attribute
                asset = extracted_data['name']
                supply = extracted_data['amount']
                units = extracted_data['units']
                reissuable = extracted_data['reissuable']
                has_ipfs = extracted_data['has_ipfs']
                ipfs_hash = extracted_data['ipfs_hash']

                # Convert units to decimal
                decimal_units = 10 ** (-units)

                await interaction.followup.send(
                    f"{author}, Your asset {asset} Listing has been confirmed. Listing {asset_balance} of {asset}  TOTAL SUPPLY: {supply / decimal_units:.8f}. PRICE: {price_per_unit} RVN per {decimal_units} of {asset}  for a TOTAL: {total_price} RVN.")
                await asyncio.sleep(10)

                if channel:
                    # Create an embed object for the message
                    embed = discord.Embed(
                        title=f"NiftyDEX: New SELL Order placed - {asset}",
                        description=f"🌟 A new asset is being listed on our NFTRVN Marketplace! 🌟",
                        color=0xFFFF00,  # Yellow
                        url=f"https://discord.com/channels/939095886993195048/1237637061855547463"
                        # Link to the listing
                    )

                    # Add fields to the embed
                    embed.add_field(name="Asset Name", value=asset, inline=False)
                    embed.add_field(name="Total Supply", value=supply, inline=False)
                    embed.add_field(name="Price Per Unit (RVN)", value=price_per_unit, inline=False)
                    embed.add_field(name="Units", value=units, inline=False)
                    embed.add_field(name="Total Sale of Listing (RVN)", value=total_price, inline=False)
                    embed.add_field(name="Listed by", value=author, inline=True)
                    embed.add_field(name="Sellers Address", value=user_address, inline=False)
                    embed.add_field(name="Asset Address", value=account_address, inline=False)
                    embed.add_field(name="IPFS HASH", value=ipfs_hash, inline=False)
                    embed.add_field(name="Reissuable (If yes, more of this asset can be issued/minted into existance.", value="Yes" if reissuable else "No", inline=False)  # Include reissuable field

                    if has_ipfs:
                        embed.set_image(
                            url=f"https://nftrvn.mypinata.cloud/ipfs/{ipfs_hash}?pinataGatewayToken={api_token}")  # IPFS image link

                    # Send the embed to the specified channel
                    await channel.send(embed=embed)

                # Update asset data with listing information
                update_data = {
                    "Asset Name": asset,
                    "last_txid": result_data.get('txid', 0),  # Add txid from asset data
                    "ipfs_hash": result_data.get('ipfs_hash', 0),  # Add ipfs_hash from asset data
                    "amt_transferred": asset_balance,
                    "ppa": price_per_unit,
                    "units": units,
                    "Account Address": account_address,
                    "transaction_type": "SellOrder",
                    "total_price": total_price,
                    "seller_address": user_address,
                    "seller": interaction.user.display_name,  # Use the user's display name from the interaction
                    "reissuable": result_data.get('reissuable', 0),  # Add reissuable from asset data
                    "supply": result_data.get('amount', 0),  # Add supply from asset data
                    "amount_listed": asset_balance  # Assuming this is the amount being listed
                }
                update_asset_data(asset, update_data)
                await asyncio.sleep(3)
                await save_listing_info("NFTRVN.json", asset, supply, asset_balance, units, price_per_unit, total_price, account_address, user_address, interaction.user.display_name)  # Pass the dynamic asset name
                await asyncio.sleep(2)
                await update_or_create_listing_embed(interaction, bot)  # Ensure this function also handles dynamic asset names
                await asyncio.sleep(5)

                await interaction.followup.send(f"Listing for {asset} confirmed and saved.")
                await asyncio.sleep(5)
                # Announce the new listing
                await announce_new_listing(interaction, asset, ipfs_hash)

            else:
                await interaction.followup.send("Listing cancelled. Start over if you wish to attempt again.")
                result = await transfer_asset(asset, new_address, asset_balance, user_address, channel)
                if result:
                    await interaction.followup.send("Asset transferred back to original address.")
                    return result
                elif result is None:
                    result = await transfer_asset(asset, account_address, asset_balance, user_address, channel)
                    if result:
                        await interaction.followup.send("Asset transferred back to original address.")
                    else:
                        await interaction.followup.send("Error transferring asset back to original address.")

                else:
                    if result is not None and "result" in result:
                        txid = result["result"]
                        if txid in result:
                            await interaction.followup.send(f"Error Listing {asset} sent back to original address. TXID: {txid}")
                            return
                        elif txid is None:
                            await interaction.followup.send(f"Error transferring {asset} sent back to original address.")
                            return
                        else:
                            await interaction.followup.send(f"Contact @admin concerning listing: {asset}. Tried to send back to original address. TXID: {txid[0]}")
                return

            username = interaction.user.display_name


            await interaction.followup.send(f"Listing for {asset} Completed: https://discord.com/channels/939095886993195048/1237637061855547463 .")
            await asyncio.sleep(1)

            await interaction.followup.send(f"Listed Asset: {asset}.")
            await asyncio.sleep(1)

            await interaction.followup.send(f"Listed Price:{price_per_unit}/{decimal_units} {asset}.")
            await asyncio.sleep(1)

            await interaction.followup.send(f"Total Supply: {result_data.get('amount', 0)}.")
            await asyncio.sleep(1)

            await interaction.followup.send(f" If all: {asset} listed sell for {price_per_unit} RVN for every Unit of {asset}: {total_price} RVN.")
            await asyncio.sleep(1)

            await interaction.followup.send(f"Listed seller: {username}.")
            await asyncio.sleep(1)

            await interaction.followup.send(f"Listed seller address: {user_address}.")
            await asyncio.sleep(1)

            await interaction.followup.send(f"Listed Nifty-AssetDEX Address: {account_address}.")
            await asyncio.sleep(1)

            await interaction.followup.send(f"This is the address/account for the {asset_name} listed. All listed {asset} will be sent to this address/account: {account_address}.")

            return
        else:
            if i < 9:  # Only send waiting message if not the last iteration
                await interaction.followup.send(f'No assets detected yet. Checking again in 1 minute. {9 - i} checks remaining.')
            await asyncio.sleep(60)  # Wait for 1 minute before next check

    await interaction.followup.send('No assets detected after 10 minutes. Please check the transaction and try again.')
    return

    # Start monitoring process in a separate task to allow bot to handle other commands
    bot.loop.create_task(monitor_asset_transfer())


# Upload and mint process - Announce new listing
async def announce_new_listing(interaction, asset_name, ipfs_hash):
    try:
        channel = bot.get_channel(1026693374301974558)

        if not channel:
            raise ValueError("Listing channel not found!")

        encoded_asset_name = custom_url_encode(asset_name)


        embed = discord.Embed(
            title=f"New Listing: {asset_name}",
            description=f"🌟 A new asset has been listed on NFTRVN marketplace! 🌟",
            color=0xD4ED31,
            url=f"https://ravencoin.asset-explorer.net/a/{encoded_asset_name}"  # Link to the asset on Ravencoin Asset Explorer
        )
        embed.add_field(name="Asset Name", value=asset_name, inline=False)
        embed.set_image(url=f"https://nftrvn.mypinata.cloud/ipfs/{ipfs_hash}?pinataGatewayToken={api_token}")  # IPFS image link

        await channel.send(embed=embed)
        await interaction.followup.send("Your listing was announced successfully! Check it in the channel!")
    except Exception as e:
        fallback_channel = bot.get_channel(1155533165679611964)
        if fallback_channel:
            await fallback_channel.send(f"Failed to announce new asset {asset_name}: {str(e)}")
        else:
            print(f"Error: {str(e)}")  # Log error or send it to a logging service


# Upload and mint process - Ask the user for the price of the asset
async def ask_for_price(interaction, asset_balance):
    """
    Prompts the user for the price for the entire lot of assets received.
    """
    await interaction.channel.send(f"Please enter the price for the entire lot of {asset_balance} assets received:")
    price_response = await bot.wait_for('message', timeout=160.0, check=lambda m: m.author == interaction.user and m.channel == interaction.channel)
    return float(price_response.content)


# Upload and mint process - Gets a new Ravencoin Address
async def get_new_address():
    result = await call_rvn_rpc("getnewaddress", [])
    return result['result']


# Upload and mint process - Checks asset balance of an address
async def check_asset_balance(address):
    if isinstance(address, str):  # Ensure address is a string
        return await call_rvn_rpc("listassetbalancesbyaddress", [address, False, 1, 0])
    elif isinstance(address, dict) and 'result' in address:
        return await call_rvn_rpc("listassetbalancesbyaddress", [address['result'], False, 1, 0])
    else:
        raise ValueError("Invalid Raven address: address must be a string or a dictionary with 'result' key")


# Upload and mint process - Wait for asset balance at an address
async def wait_for_asset_balance(address, timeout_minutes=15, check_interval_seconds=30):
    start_time = time.time()
    print(f"Entering Loop now, Checking asset balance for {address}")
    while True:
        print(f"Start of Loop: Checking asset balance for {address}")

        asset_balances = await check_asset_balance(address)
        print(asset_balances)
        if asset_balances and isinstance(asset_balances, dict):
            for asset_name, balance in asset_balances['result'].items():  # Access 'result' key of the response
                print(balance)
                if balance is not None and isinstance(balance, (int, float)):
                    print(f"Ensuring the {balance} > 0 at {address}")

                    if balance > 0:
                        # Fetch asset data using getassetdata RPC
                        asset_data = await call_rvn_rpc("getassetdata", [asset_name])  # Use dynamic asset name
                        print(asset_data)

                        # Check if 'result' key exists and is a dictionary
                        if 'result' in asset_data and isinstance(asset_data['result'], dict):
                            result_data = asset_data['result']
                            asset = result_data.get('name', '')
                            units = result_data.get('units', 0)
                            amount = result_data.get('amount', 0)
                            ipfs_hash = result_data.get('ipfs_hash', '')
                            has_ipfs = result_data.get('has_ipfs', 0)
                            reissuable = result_data.get('reissuable', 0)  # Include reissuable key
                        else:
                            units = 0
                            amount = 0
                            ipfs_hash = ''
                            has_ipfs = 0
                            reissuable = 0

                        # Replace invalid filename characters in asset name
                        safe_asset_name = asset.replace('/', '-').replace('#', '_')
                        file_name = f"{safe_asset_name}.json"
                        if not os.path.exists(file_name):
                            # Determine the asset type based on the asset name
                            if "/" not in asset and "#" not in asset:
                                asset_type = "MAIN ASSET"
                            elif "/" in asset:
                                asset_type = "SUB-ASSET TOKEN"
                            elif "#" in asset:
                                asset_type = "UNIQUE-ASSET (NFT)"

                            # Create a new JSON file for the asset if it doesn't exist
                            asset_data = {
                                "name": asset,
                                "supply": amount,
                                "units": units,
                                "reissuable": reissuable,
                                "has_ipfs": has_ipfs,
                                "ipfs_hash": ipfs_hash,
                                "last_txid": "",
                                "amt_transferred": 0,
                                "transaction_type": "",
                                "selling_user": "",
                                "buying_user": "",
                                "ath_price": 0,
                                "atl_price": 0,
                                "asset_type": asset_type
                            }
                            with open(file_name, 'w') as file:
                                json.dump(asset_data, file, indent=4)
                        return asset, float(balance)
        if time.time() - start_time > timeout_minutes * 60:
            raise TimeoutError("Timed out waiting for asset balance")
        await asyncio.sleep(check_interval_seconds)


# Upload and mint process - Get or create asset account
async def get_or_create_asset_account(asset_name, new_address):
    """
    Retrieves an existing asset account address or creates a new one if it doesn't exist.
    """
    # Try to get the existing account address for the asset.
    account_response = await call_rvn_rpc("getaccountaddress", [f"{asset_name}_dex"])

    # Check if the response has a valid address.
    account_address = account_response.get('result')
    if not account_address:
        # If no address exists, associate the new address with the asset account.
        await call_rvn_rpc("setaccount", [new_address, f"{asset_name}_dex"])
        return new_address  # Return new address as the account address.

    return account_address  # Return the existing account address.


# Upload and mint process - Transfers the asset 
async def transfer_asset(asset_name, from_address, quantity, to_address, channel):
    call_rpc("walletpassphrase", ["135790", 6000])  # Unlock the wallet for 60 seconds
    # Check if the from_address is a dictionary and extract the address
    if isinstance(from_address, dict):
        fromaddress = from_address['result']
    else:
        fromaddress = from_address

    asset = str(asset_name)
    fromaddy = str(fromaddress)
    toaddy = str(to_address)

    # Check if the quantity is a valid number
    if not isinstance(quantity, (int, float)):
        raise ValueError("Invalid quantity: quantity must be a number")

    # Prepare the RPC parameters
    rpc_params = [asset, fromaddy, quantity, toaddy, "", 0, "", fromaddy]
    #await call_rvn_rpc("walletpassphrase", ["Password1!", 60000000000])  # Unlock the wallet for 60 seconds
    # Call the RPC to transfer the asset
    transfer_response = call_rpc("transferfromaddress", rpc_params)

    # Debug logs
    print(f"Transfer Response: {transfer_response}")

    # Check if the transfer was successful
    if 'result' in transfer_response and transfer_response['result']:
        transfer_txid = transfer_response['result']
        await channel.send(f"Transfer successful. Transaction ID: {transfer_txid}")
    else:
        await channel.send("Error while transferring assets.")
    # Lock the wallet after the transfer
    call_rpc("walletlock", [])
    return transfer_response  # Return the response from the RPC call


# Upload and mint process - Saves the listing info
async def save_listing_info(file_name: str, asset_name: str, supply: float, asset_balance: float, units: float, price_per_unit: float, total_price: float, listing_address: str, user_address: str, user_name: str):
    """
    Save or update listing information in a JSON file.
    """
    try:
        # Load existing data from file if exists, otherwise start with an empty list
        with open(file_name, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Assume listing_address is a simple string containing the address
    list_Addy = listing_address

    # Append new listing data
    data.append({
        "asset_name": asset_name,
        "supply": supply,
        "asset_balance": asset_balance,
        "units": units,
        "price_per_unit": price_per_unit,
        "total_price": total_price,
        "listing_address": list_Addy,
        "NiftyRaven Member": user_name,  # Add the user's name
        "user_address": user_address
    })

    # Sort data by asset name and price per unit for easier browsing and consistency
    data.sort(key=lambda x: (x["asset_name"], x["price_per_unit"]))

    # Write the updated data back to the file
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


# Add functions for RPC calls, balance updates, and transaction verification here
async def load_listings():
    try:
        with open('NFTRVN.json', 'r') as file:
            listings = json.load(file)
        return listings
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


#verify transaction
async def verify_transaction(txid, amount, user_id):
    # Implement the actual RPC call to verify the transaction
    return True  # Placeholder for actual verification logic


# Transfer assets
async def transfer_assets(interaction, selected_listing):
    # Implement the asset transfer logic here
    seller_id = selected_listing['user_address']
    buyer_id = interaction.user.id
    asset_amount = selected_listing['asset_balance']
    transaction_amount = selected_listing['total_price']

    seller_roles = [role.id for role in interaction.guild.get_member(seller_id).roles]
    no_fee_roles = [1145495368839204925, 1015723816921612308]

    if any(role in seller_roles for role in no_fee_roles):
        seller_amount = transaction_amount
    else:
        seller_amount = transaction_amount * 0.94
        rewards_amount = transaction_amount * 0.06
        await send_rvn(REWARDS_WALLET, rewards_amount)

    await send_rvn(seller_id, seller_amount)
    await send_asset(buyer_id, selected_listing['asset_name'], asset_amount)

    buyer_bonus_tokens = 0.5 * 0.875 * transaction_amount
    seller_bonus_tokens = 0.5 * 0.4375 * transaction_amount

    await send_niftyraven_tokens(buyer_id, buyer_bonus_tokens)
    await send_niftyraven_tokens(seller_id, seller_bonus_tokens)


# Send rvn
async def send_rvn(address, amount):
    # Implement the logic to send RVN to the specified address
    pass


# Send asset
async def send_asset(address, asset_name, amount):
    # Implement the logic to send the specified asset to the address
    pass


# Send NiftyRaven tokens
async def send_niftyraven_tokens(address, amount):
    # Implement the logic to send NIFTYRAVEN.COM tokens to the address
    pass


# Gets the RVN price from a channel
async def get_rvn_price_from_channel(bot, channel_id):
    try:
        channel = bot.get_channel(channel_id)
        # Example channel name: "$RVN: $0.02809"
        price_str = channel.name.split('$')[-1]  # Extract the last part after '$'
        return float(price_str)
    except Exception as e:
        print(f"Failed to get RVN price from channel: {str(e)}")
        return None  # Return None if there's an error


# Upload and mint process - Update or create listing embed
async def update_or_create_listing_embed(interaction, bot):
    channel = bot.get_channel(1237637061855547463)
    message_id = 1240098908038893599  # Updated message ID

    try:
        message = await channel.fetch_message(message_id)
    except discord.NotFound:
        # If message not found, send a new one
        message = None

    listings = await load_listings()
    if not listings:
        if message:
            await message.edit(content="No current listings available.", embed=None, view=None)
        else:
            await channel.send("No current listings available.")
        return

    grouped_listings = defaultdict(list)
    for listing in listings:
        grouped_listings[listing['asset_name']].append(listing)

    sorted_assets = []
    for asset_name, groups in grouped_listings.items():
        lowest_price = min(group['price_per_unit'] for group in groups)
        ath_price = max(group.get('ath_price', 0) for group in groups)
        atl_price = min(group.get('atl_price', float('inf')) for group in groups)
        last_sold_price = groups[-1]['price_per_unit']
        sorted_assets.append({
            'asset_name': asset_name,
            'lowest_price': lowest_price,
            'ath_price': ath_price,
            'atl_price': atl_price,
            'last_sold_price': last_sold_price,
            'groups': groups
        })

    view = AssetActionView(sorted_assets)
    embed = view.generate_embed()
    if message:
        await message.edit(embed=embed, view=view)
    else:
        message = await channel.send(embed=embed, view=view)
        view.message = message  # Assign the message to the view for later editing

    view.message = message  # Store the message object in the view for future updates


##
#ASYNCRONOUS DEFINITIONS END
#################################################
#################################################
# DEFINITIONs END
############################################################################################################
############################################################################################################
########################################################################################################################
########################################################################################################################
# CLASSES START
#################################################
#################################################
############################################################################################################

# Market information view
class MarketInfoView(View):
    def __init__(self, ctx, url):
        super().__init__(timeout=180)  # Set timeout as needed
        self.ctx = ctx
        self.url = url

    # Button callback for refreshing market data
    @discord.ui.button(label='Refresh', style=discord.ButtonStyle.green)
    async def refresh(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Ensure the user clicking the button is the one who invoked the command
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("You cannot use this button.", ephemeral=True)
            return

        # Fetch new market data
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                if response.status == 200:
                    data = await response.json()
                    embed = self.format_market_data(data)
                    await interaction.response.edit_message(content=None, embed=embed, view=self)
                else:
                    await interaction.response.send_message("Failed to fetch market information.", ephemeral=True)

    def format_market_data(self, data):
        embed = discord.Embed(title="Ravencoin Market Information", color=discord.Color.blue())
        embed.add_field(name="Max Price (in BTC)", value=f"{float(data['max_price']):.8f} BTC", inline=False)
        embed.add_field(name="Average Price (in BTC)", value=f"{float(data['avg_price']):.8f} BTC", inline=False)
        embed.add_field(name="Volume (in RVN)", value=f"{int(float(data['volume_coin'])):,} RVN", inline=False)
        embed.add_field(name="24h Change", value=f"{data['percent_change']}%", inline=False)

        exchange_rates = "\n".join([f"{metric['exchange']}: {self.format_price(metric['latest'])} BTC" for metric in data['metrics'] if metric['latest'] is not None])
        embed.add_field(name="Exchange Rates (Top exchanges)", value=exchange_rates or "N/A", inline=False)

        return embed

    def format_price(self, price):
        # Convert scientific notation to float then to string to avoid scientific notation
        if price is not None:
            return f"{float(price):.8f}"
        return "None"

# Upload and mint process - Mint asset information modal
class MintAssetModal(discord.ui.Modal, title="Mint Asset Information"):
    def __init__(self):
        super().__init__()
        self.ipfs_hash = discord.ui.TextInput(label="IPFS Hash", placeholder="Enter the IPFS hash for the asset...", required=True)
        self.add_item(self.ipfs_hash)
        self.asset_name = discord.ui.TextInput(label="Asset Name", placeholder="Enter the name for the asset...", required=True)
        self.add_item(self.asset_name)

    async def on_submit(self, interaction: discord.Interaction):
        ipfs_hash = self.ipfs_hash.value
        asset_name = self.asset_name.value
        # Defer the interaction as processing begins
        await interaction.response.defer(ephemeral=True)
        await mint_auto(interaction, ipfs_hash, asset_name)


# Upload and mint process - Handling interactions separately
class UploadPinMintButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Upload+Pin & Mint", style=discord.ButtonStyle.primary, custom_id="upload_pin_mint")

    async def callback(self, interaction: discord.Interaction):
        user_id = interaction.user.id
        user_address = get_user_address(user_id)

        if not user_address:
            await interaction.response.send_message(
                "Your address could not be found. Please enter your address to register.",
                ephemeral=True
            )
            message = await interaction.original_response()
            await message.channel.send(
                "Please reply with your Ravencoin address to register."
            )

            def check(m):
                return m.author.id == user_id and m.channel == message.channel

            response_message = await self.bot.wait_for('message', check=check)
            user_data = load_user_data()
            user_data["users"][str(user_id)] = {"address": response_message.content}
            save_user_data(user_data)
            user_address = response_message.content
            await interaction.followup.send(
                "Thank you! Your address has been registered. You can now proceed with minting."
            )

            if not user_address:
                await interaction.followup.send(
                    "You don't have a Ravencoin wallet? Get one for free here: https://niftyraven.com/wallet-self-custody",
                    ephemeral=True
                )
        print("Getting User Address.")
        # Use defer if processing will take time
        await interaction.response.defer(ephemeral=True)
        print("Handling Payment.")
        await handle_payment(interaction, user_address)
        print("Attempting to proceed with minting, payment received.")
        await upload_and_mint_process(interaction, user_address)
        await interaction.followup.send("Minting initiated!")


# Upload and mint process - Modal dialog for asset information
class IssueAssetModal(Modal):
    def __init__(self):
        super().__init__(title="Issue Asset")

        self.asset = TextInput(label="Asset Name", placeholder="Enter the asset name", required=True)
        self.qty = TextInput(label="Quantity", placeholder="Enter the quantity", required=True)
        self.units = TextInput(label="Units", placeholder="Enter the units (decimal places)", required=True)
        self.reissuable = TextInput(label="Reissuable", placeholder="True or False", required=True)

        self.add_item(self.asset)
        self.add_item(self.qty)
        self.add_item(self.units)
        self.add_item(self.reissuable)

    async def callback(self, interaction: discord.Interaction):
        try:
            # Extract the values from the modal
            asset_name = self.asset.value
            quantity = float(self.qty.value)
            units = int(self.units.value)
            reissuable = self.reissuable.value.lower() == 'true'

            # Get the issuing address
            address = await get_address()

            # Issue the asset
            success, result = await mint_mainasset(asset_name, quantity, units, reissuable, address)

            if success:
                # Send success message
                await interaction.response.send_message(
                    f"**Asset Issuance Details**\n"
                    f"**Asset Name:** {asset_name}\n"
                    f"**Quantity:** {quantity}\n"
                    f"**Units:** {units}\n"
                    f"**Reissuable:** {'Yes' if reissuable else 'No'}\n"
                    f"**Issuing Address:** {address}\n\n"
                    f"Asset {asset_name} issued successfully! Transaction ID: {result}",
                    ephemeral=True
                )
            else:
                await interaction.response.send_message(f"An error occurred: {result}", ephemeral=True)

        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {e}", ephemeral=True)


# Upload and mint process - Button to issue asset
class IssueAssetButton(Button):
    def __init__(self):
        super().__init__(label="Issue Asset", style=discord.ButtonStyle.success)

    async def callback(self, interaction: discord.Interaction):
        modal = IssueAssetModal()
        await interaction.response.send_modal(modal)


# Upload and mint process - View containing the button
class IssueAssetView(View):
    def __init__(self):
        super().__init__(timeout=180)  # Timeout for the view in seconds
        self.add_item(IssueAssetButton())


# Upload and mint process - Button to mint with IPFS hash
class MintWithIPFSButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Mint with IPFS HASH", style=discord.ButtonStyle.primary, custom_id="mint")

    async def callback(self, interaction: discord.Interaction):
        # Immediately respond with a modal
        await interaction.response.send_modal(MintAssetModal())


# Upload and mint process - View containing the button
class MyView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(UploadPinMintButton())
        self.add_item(IssueAssetButton())


# NFTRVN command - Paginator for listing assets
class ReactionPaginator:
    def __init__(self, ctx, pages):
        self.ctx = ctx
        self.pages = pages
        self.current_page = 0
        self.message = None

    async def start(self):
        self.message = await self.ctx.send(embed=self.pages[self.current_page])
        await self.add_reactions()

        def check(reaction, user):
            return user == self.ctx.author and reaction.message.id == self.message.id and str(reaction.emoji) in ['◀️', '▶️']

        while True:
            try:
                reaction, user = await self.ctx.bot.wait_for('reaction_add', timeout=60.0, check=check)

                if str(reaction.emoji) == '◀️' and self.current_page > 0:
                    self.current_page -= 1
                    await self.message.edit(embed=self.pages[self.current_page])
                    await self.message.remove_reaction(reaction, user)

                elif str(reaction.emoji) == '▶️' and self.current_page < len(self.pages) - 1:
                    self.current_page += 1
                    await self.message.edit(embed=self.pages[self.current_page])
                    await self.message.remove_reaction(reaction, user)

                else:
                    await self.message.remove_reaction(reaction, user)

            except asyncio.TimeoutError:
                await self.message.clear_reactions()
                break

    async def add_reactions(self):
        if len(self.pages) > 1:
            await self.message.add_reaction('◀️')
            await self.message.add_reaction('▶️')


# NFTRVN command - Buttons for List or Buy
class TokenActionView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=1200)  # Timeout for button interaction

    @discord.ui.button(label="Buy", style=discord.ButtonStyle.green, custom_id="buy")
    async def buy_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        listings = await load_listings()
        asset_names = list({listing['asset_name'] for listing in listings})
        view = AssetSelectView(asset_names)
        await interaction.response.send_message("Select the asset you want to buy:", view=view, ephemeral=True)


    @discord.ui.button(label="List", style=discord.ButtonStyle.danger, custom_id="list")
    async def list_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("You chose to list tokens. Please wait...", ephemeral=True)
        user_address = get_user_address(interaction.user.id)
        if not user_address:
            await interaction.followup.send("No address found. Please register your address first.")
            return

        await interaction.followup.send(f"Your registered address at NIFTYRAVEN.COM is: {user_address}")
        new_address = await get_new_address()
        await interaction.followup.send(
            f"Please send the asset you want to list to the following address: {new_address}")

        # Attach the view with the "Done" button
        view = ConfirmTransferView(new_address, user_address)
        await interaction.followup.send('Click "I\'ve sent the assets" once you have completed the transfer.', view=view)


# NFTRVN command - Buttons for Confirm Transfer
class ConfirmTransferView(discord.ui.View):
    def __init__(self, new_address, user_address):
        super().__init__()
        self.new_address = new_address
        self.user_address = user_address

    @discord.ui.button(label="I've sent the assets", style=discord.ButtonStyle.green, custom_id="confirm_transfer")
    async def confirm_transfer(self, interaction: discord.Interaction, button: discord.ui.Button):
        # Acknowledge the user's action and begin monitoring asset transfer
        await interaction.response.send_message("Thank you! We are now checking for the asset transfer. Please wait...", ephemeral=True)
        print(f"Button clicked confirming assets sent, trying to run monitor asset transfer")
        await monitor_asset_transfer(interaction, self.new_address, self.user_address)


# NFTRVN command - Buttons for Asset Select
class AssetSelectView(discord.ui.View):
    def __init__(self, asset_names):
        super().__init__(timeout=600)
        self.asset_select = discord.ui.Select(placeholder="Choose an asset to buy")
        for asset in asset_names:
            self.asset_select.add_option(label=asset, value=asset)
        self.asset_select.callback = self.asset_select_callback
        self.add_item(self.asset_select)

    async def asset_select_callback(self, interaction: discord.Interaction):
        selected_asset = self.asset_select.values[0]
        listings = await load_listings()
        asset_listings = [listing for listing in listings if listing['asset_name'] == selected_asset]
        view = SellOrderSelectView(asset_listings)
        await interaction.response.send_message("Select a sell order:", view=view, ephemeral=True)


# NFTRVN command - Buttons for Sell Order Select
class SellOrderSelectView(discord.ui.View):
    def __init__(self, asset_listings):
        super().__init__(timeout=600)
        self.sell_order_select = discord.ui.Select(placeholder="Choose a sell order to buy from")
        for listing in asset_listings:
            label = f"{listing['asset_name']} - {listing['price_per_unit']} RVN/unit - {listing['asset_balance']} units"
            self.sell_order_select.add_option(label=label, value=str(asset_listings.index(listing)))
        self.sell_order_select.callback = self.sell_order_select_callback
        self.add_item(self.sell_order_select)

    async def sell_order_select_callback(self, interaction: discord.Interaction):
        selected_index = int(self.sell_order_select.values[0])
        asset_listings = self.sell_order_select.options
        selected_listing = asset_listings[selected_index]
        view = ConfirmPurchaseView(selected_listing)
        await interaction.response.send_message("Confirm your purchase:", view=view, ephemeral=True)


# NFTRVN command - Buttons for Confirm Purchase
class ConfirmPurchaseView(discord.ui.View):
    def __init__(self, selected_listing):
        super().__init__(timeout=600)
        self.selected_listing = selected_listing
        self.confirm_button = discord.ui.Button(label="Confirm Purchase", style=discord.ButtonStyle.green)
        self.confirm_button.callback = self.confirm_button_callback
        self.add_item(self.confirm_button)

    async def confirm_button_callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"Send {self.selected_listing['total_price']} RVN to {self.selected_listing['listing_address']}. "
            "Type 'done' with your transaction ID once completed.", ephemeral=True)
        self.stop()

        def check(m):
            return m.author == interaction.user and m.channel == interaction.channel and m.content.startswith("done")

        try:
            txid_response = await bot.wait_for('message', timeout=300.0, check=check)
            txid = txid_response.content.split()[1]
            # Verify transaction and send assets
            transaction_valid = await verify_transaction(txid, self.selected_listing['total_price'], interaction.user.id)

            if transaction_valid:
                await transfer_assets(interaction, self.selected_listing)
                await interaction.followup.send("Purchase successful!")
            else:
                await interaction.followup.send("Transaction verification failed. Please check the transaction ID and try again.")
        except asyncio.TimeoutError:
            await interaction.followup.send("Timeout. Please try the command again.")


# NFTRVN command - Buttons for Asset Action
class AssetActionView(discord.ui.View):
    def __init__(self, assets, page=0):
        super().__init__(timeout=None)  # Set to None for no timeout or use a very long timeout
        self.assets = assets
        self.page = page
        self.max_items = 10

    def generate_embed(self):
        start_index = self.page * self.max_items
        end_index = start_index + self.max_items
        current_assets = self.assets[start_index:end_index]

        embed = discord.Embed(title="NiftyDEX Listings", description="Current asset listings, sorted by price", color=0xFFFF00)
        for asset in current_assets:
            embed.add_field(
                name=f"{asset['asset_name']} - {sum(group['asset_balance'] for group in asset['groups'])} units",
                value=(
                    f"Lowest Price: {asset['lowest_price']:.8f} RVN\n"
                    f"Last Sold Price: {asset['last_sold_price']:.8f} RVN\n"
                    f"ATH Price: {asset['ath_price']:.8f} RVN\n"
                    f"ATL Price: {asset['atl_price']:.8f} RVN\n"
                    f"Listed By: {asset['groups'][-1].get('NiftyRaven Member', 'N/A')}\n"
                    f"NiftyDEX Address: {asset['groups'][-1]['listing_address']}\n"
                    f"More Details: Type `?assetinfo {custom_url_encode(asset['asset_name'])}` for more info",
                ),
                inline=False
            )
        embed.set_footer(text=f"Page {self.page + 1} of {len(self.assets) // self.max_items + 1}")
        return embed

    @discord.ui.button(label="⬅️", style=discord.ButtonStyle.grey, custom_id="previous_page")
    async def previous_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.page > 0:
            self.page -= 1
            await interaction.response.edit_message(embed=self.generate_embed(), view=self)

    @discord.ui.button(label="➡️", style=discord.ButtonStyle.grey, custom_id="next_page")
    async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if self.page < len(self.assets) // self.max_items:
            self.page += 1
            await interaction.response.edit_message(embed=self.generate_embed(), view=self)

    async def on_timeout(self):
        for item in self.children:
            item.disabled = False
        await self.message.edit(view=self)


############################################################################################################
# CLASSES END
############################################################################################################
#################################################
########################################################################################################################
########################################################################################################################
# COMMANDS START
############################################################################################################

# List transactions command
@bot.command()
async def listtransactions(ctx):
    transactions = call_rpc("listtransactions", ["*", 4])  # Fetch the last 100 transactions
    if transactions is None or "result" not in transactions or not transactions["result"]:
        await ctx.send("Error calling RPC method listtransactions")
        return

    response = f'Transactions:\n\n'
    for tx in transactions["result"]:
        response += f'Transaction ID: {tx["txid"]}\n'
        response += f'Amount: {tx["amount"]} RVN\n'
        response += f'Category: {tx["category"]}\n'
        response += f'Date and time: {datetime.datetime.fromtimestamp(tx["time"]).strftime("%Y-%m-%d %H:%M:%S")}\n'
        response += f'\n'

    await ctx.send(response)


# Market information command - Solus
@bot.command()
async def marketinfo(ctx):
    url = "https://rvn.cryptoscope.io/api/getmarketinfo/"
    view = MarketInfoView(ctx, url)

    # Initial fetch for market data
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                embed = view.format_market_data(data)
                await ctx.send(embed=embed, view=view)
            else:
                await ctx.send("Failed to fetch market information.")


# Command to get the top 10 holders of an asset, provide a chart, and save the data to a JSON file
@bot.command()
async def addresses(ctx, asset_name: str):
    # Inform the user that the process has started
    await ctx.send(f"Fetching the number of addresses holding {asset_name}...")

    # Assuming call_rpc is an existing function that calls your RPC server
    response = call_rpc("listaddressesbyasset", [asset_name, True])
    if 'result' not in response:
        await ctx.send("Failed to retrieve data. Please try again later.")
        return

    total_addresses = response['result']

    # Inform the user about the total number of addresses
    await ctx.send(f"Total number of addresses holding {asset_name}: {total_addresses}")

    addresses_response = call_rpc("listaddressesbyasset", [asset_name, False])
    if 'result' not in addresses_response:
        await ctx.send("Failed to retrieve data. Please try again later.")
        return

    addresses_with_balances = addresses_response['result']
    sorted_addresses = sorted(addresses_with_balances.items(), key=lambda x: x[1], reverse=True)

    asset_data_response = call_rpc("getassetdata", [asset_name])
    if 'result' not in asset_data_response:
        await ctx.send("Failed to retrieve asset data. Please try again later.")
        return

    total_tokens = asset_data_response['result']['amount']

    top_holders = []
    labels = []
    sizes = []
    for address, balance in sorted_addresses[:10]:
        percentage = (balance / total_tokens) * 100
        top_holders.append(f"{address}: {balance} ({percentage:.2f}%)")
        labels.append(address[-5:])  # Display last 5 chars of address for readability
        sizes.append(percentage)

    message = "\n".join(top_holders)
    await ctx.send(f"Top 10 holders of {asset_name}:\n{message}")

    # Generating bar chart
    fig, ax = plt.subplots()
    ax.bar(labels, sizes)
    plt.xticks(rotation=45)  # Rotate labels to prevent overlapping
    plt.xlabel('Addresses (Last 5 Characters)')
    plt.ylabel('Percentage of Total Tokens')
    plt.title(f'Top 10 Holders of {asset_name}')
    plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close(fig)  # Close the figure to free memory

    # Send the chart as an image in Discord
    await ctx.send(file=discord.File(buffer, 'top_holders_chart.png'))


# Command to register a Ravencoin address with the bot
@bot.command()
async def myaddy(ctx, address: str):
    user_id = str(ctx.author.id)  # Convert user ID to string to use as JSON key
    if not is_valid_ravencoin_address(address):
        await ctx.send("Invalid Ravencoin address.")
        return

    # Load user data from the JSON file
    try:
        # Use aiofiles if available for true async file operations
        user_data = await asyncio.get_event_loop().run_in_executor(None, load_user_data)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        await ctx.send("Error loading user data. Please try again later.")
        print(e)  # Log the error for debugging
        return

    # Ensure user_data is initialized correctly
    if "users" not in user_data:
        user_data["users"] = {}

    # Update the user's address in the user data
    if user_id in user_data["users"]:
        user_data["users"][user_id]['address'] = address
    else:
        user_data["users"][user_id] = {"address": address}

    # Save the updated user data back to the JSON file
    await asyncio.get_event_loop().run_in_executor(None, lambda: save_user_data(user_data))

    await ctx.send(f"{ctx.author.mention} Ravencoin address registered.")


# Gets balance of an address
@bot.command()
async def get_balance(ctx, address: str):


    try:
        # Forming the RPC call
        rpc_params = [{"addresses": [address]}, True]
        print(f"RPC Request Params: {rpc_params}")  # Debugging print

        # Making the RPC call
        response = call_rpc("getaddressbalance", rpc_params)
        print(f"RPC Response: {response}")  # Debugging print

        if 'result' in response and response['result']:
            balance_info = response['result']
            embed = discord.Embed(title=f"Balance for {address}", color=discord.Color.gold())

            for asset in balance_info:
                asset_name = asset['assetName']
                asset_balance = asset['balance'] / 1e8
                received = asset['received'] / 1e8
                spent = asset_balance - received

                # Determine the type of asset
                if "#" in asset_name:
                    asset_type = "NFT"
                elif "/" in asset_name:
                    asset_type = "Subasset"
                else:
                    asset_type = "Main Asset"

                # Fetch asset details using 'getinfo' command
                await ctx.invoke(bot.get_command('getinfo'), asset_name=asset_name)

                # Build the line with asset link
                line = f"- **[{asset_name}]({base_info_url}{asset_name}) ({asset_type}):** Balance: {asset_balance} - Received: {received} - Spent: {spent}\n"
                embed.add_field(name="\u200b", value=line,
                                inline=False)  # \u200b: Zero-width space for better formatting

            await ctx.send(embed=embed)

        else:
            await ctx.send(f"No assets found for address {address}.")

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


# Command to get transaction details of an address
@bot.command()
async def gettxs(ctx, address: str):
    transactions = await fetch_transactions(address)
    if not transactions:
        await ctx.send("An error occurred while fetching transactions. Please try again later.")
        return

    txs = transactions.get('txs', [])
    if not txs:
        await ctx.send(f"No transactions found for {address}.")
        return

    txs.sort(key=lambda tx: tx.get('time', tx.get('blockheight')), reverse=True)
    message = f"Transactions for {address}:\n"

    for tx in txs[:20]:  # Limit to the first 20 transactions
        tx_details = await fetch_transaction_details(tx['txid'])
        if not tx_details:
            message += f"\nTransaction ID: {tx['txid']} - Transaction details not available\n"
            continue

        message += f"\nTransaction ID: {tx['txid']}\n"
        message += parse_transaction_details(tx_details, address)

        if len(message) >= 1800:  # Check if message is too long
            await send_large_message(ctx, message)
            message = ""  # Reset message for the next batch

    if message:  # Send any remaining part of the message
        await send_large_message(ctx, message)


# Command to give the user help information and commands that can be used within discord
@bot.command(name='helpme')
async def helpme(ctx):
    # Create an embed object with a vibrant color and detailed description.
    help_embed = discord.Embed(
        title="🚀 Nifty Minter Help Desk 🚀",
        description="Unlock your Nifty potential! Here are the commands you can use:",
        color=0x1E90FF  # A deep sky blue color.
    )
    help_embed.set_thumbnail(url="https://ipfs.io/ipfs/QmbZK2MGtgR5DSfszBMdFULNiZJR9wS3hAdhfWWosJuhfV")
    help_embed.set_image(url="https://ipfs.io/ipfs/QmQGkHyXKdWLLKusPc9TMUtzhjZz6RB9WKzqDPYBEXBWGv/ipfs/QmSNQFKwaX9qY6xaVGY2menLpqRA7Z61KdY482rUC4P4EX?filename=NR-LOGO.gif")

    # Adding fields with emojis to make the commands more visually distinct.
    help_embed.add_field(
        name="🔗 ?myaddy [address]",
        value="Register your Ravencoin address. Don’t have one? [Get Started Here!](https://niftyraven.com/wallet-self-custody)",
        inline=False
    )
    help_embed.add_field(
        name="📊 ?NFTRVN",
        value="List or Buy Assets/NFTs within NiftyRaven Discord and many other discords!",
        inline=False
    )
    help_embed.add_field(
        name="🎨 ?mint",
        value="Mint your own unique NFT.",
        inline=False
    )
    help_embed.add_field(
        name="📜 ?listtransactions",
        value="List the last 4 transactions of NFTRVN.net",
        inline=False
    )
    help_embed.add_field(
        name="🔍 ?getinfo [asset_name]",
        value="Retrieve detailed information about a specific asset.",
        inline=False
    )
    help_embed.add_field(
        name="📊 ?gettxs [address]",
        value="Display a list of transaction IDs for assets and RVN received at a specified address.",
        inline=False
    )
    help_embed.add_field(
        name="🏆 ?leaderboard",
        value="See who's leading in minting under the NFTRVN Asset.",
        inline=False
    )
    help_embed.add_field(
        name="📌 ?pinlist",
        value="Review pinned items within NiftyRaven Pinata (Admins only).",
        inline=False
    )
    help_embed.add_field(
        name="🔢 ?addresses [asset_name]",
        value="Show total number of holders and a Top 10 List for a specific asset.",
        inline=False
    )
    help_embed.add_field(
        name="🌐 ?marketinfo",
        value="Get the latest market information for Ravencoin.",
        inline=False
    )
    help_embed.add_field(
        name="💹 ?marketcap",
        value="Retrieve the current market capitalization of Ravencoin.",
        inline=False
    )
    help_embed.add_field(
        name="👥 ?guildcount",
        value="Find out how many guilds NiftyMinter is participating in.",
        inline=False
    )
    help_embed.add_field(
        name="🛡️ ?guildinfo",
        value="Access information about the current Discord guilds' registered addresses for minting rewards (Admins).",
        inline=False
    )

    # Sending the embed to the channel where the command was called.
    await ctx.send(embed=help_embed)


# Command to start the asset issuance process
@bot.command(name='issue_asset_view')
async def issue_asset_view_command(ctx):
    """
    Command to start the asset issuance process.

    This command sends a view with a button that allows the user to initiate
    the asset issuance process.
    """
    await ctx.send("Click the button below to issue an asset:", view=IssueAssetView())


# Command to start the minting process
@bot.command()
async def mint(ctx):
    call_rpc("walletpassphrase", ["135790", 1200])  # Unlock the wallet for 60 seconds

    """Sends a button to the user for selecting the minting process."""
    await ctx.send("Choose the minting process:", view=MyView())


# Updated issue_asset_command to be callable
@bot.command(name='issue_asset')
async def issue_asset_command(ctx, asset: str, qty: float, units: int, reissuable: bool = False):
    """
    Command to issue a new asset on the Ravencoin blockchain.

    Args:
        ctx: The context in which the command was executed.
        asset (str): The name of the asset to be issued.
        qty (float): The quantity of the asset to be issued.
        units (int): The number of decimal places for the asset.
        reissuable (bool): Whether the asset can be reissued. Defaults to False.

    Usage:
        ?issue_asset <asset_name> <quantity> <units> <reissuable>

    Example:
        ?issue_asset "MYASSET" 1000 8 True
    """
    try:
        # Log the command usage
        print(f"Issuing asset: {asset}, Quantity: {qty}, Units: {units}, Reissuable: {reissuable}")

        # Get the issuing address
        address = ravencoin_issuance.get_address()
        print(f"Issuing address: {address}")

        # Issue the asset
        ravencoin_issuance.issue_asset(asset, qty, units, reissuable, address)
        await ctx.send(
            f"**Asset Issuance Details**\n"
            f"**Asset Name:** {asset}\n"
            f"**Quantity:** {qty}\n"
            f"**Units:** {units}\n"
            f"**Reissuable:** {'Yes' if reissuable else 'No'}\n"
            f"**Issuing Address:** {address}\n\n"
            f"Asset {asset} issued successfully!"
        )
    except Exception as e:
        print(f"Error issuing asset: {e}")
        await ctx.send(f"An error occurred while issuing the asset: {e}")


# Command to get a list of Ravencoin Nodes - Solus
@bot.command()
async def getnodes(ctx):
    url = "https://rvn.cryptoscope.io/api/getaddnodelist/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                # Split data into manageable parts and create pages
                nodes = data.split('\n')
                chunk_size = 10
                chunks = ['\n'.join(nodes[i:i + chunk_size]) for i in range(0, len(nodes), chunk_size)]
                pages = [discord.Embed(description=f"```{chunk}```", color=discord.Color.blue()) for chunk in chunks]

                paginator = ReactionPaginator(ctx, pages)
                await paginator.start()
            else:
                await ctx.send("Failed to fetch addnode list.")


# Command to fetch transaction details for a given transaction ID
@bot.command()
async def fetch_transaction_details(txid):
    try:
        # Fetch the raw transaction data
        raw_tx_response = rpc_call("getrawtransaction", [txid, False])  # False for getting hex string
        if not raw_tx_response or 'result' not in raw_tx_response:
            print(f"Failed to fetch raw transaction for txid: {txid}")
            return None

        # Extract the hex string of the transaction
        tx_hex = raw_tx_response['result']

        if not tx_hex:
            print(f"No hex string found in transaction data for txid: {txid}")
            return None

        # Decode the raw transaction using the hex string
        decoded_tx_response = rpc_call("decoderawtransaction", [tx_hex])
        if not decoded_tx_response or 'result' not in decoded_tx_response:
            print(f"Failed to decode transaction for txid: {txid}")
            return None

        # The result itself is the decoded transaction details
        tx_details = decoded_tx_response['result']
        return tx_details
    except Exception as e:
        print(f"Exception in fetch_transaction_details: {str(e)}")
        return None


# Command to get messages of an address
@bot.command()
async def getmsgs(ctx, address: str, since: int = None):
    # Prompt for DMs
    await ctx.send("Do you want to receive the asset messages in DM? (Yes/No)")
    try:
        confirmation = await bot.wait_for('message', timeout=30.0, check=lambda
            m: m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ["yes", "no"])
    except asyncio.TimeoutError:
        await ctx.send("You didn't reply in time, please try the command again.")
        return

    send_in_dm = confirmation.content.lower() == "yes"
    target_channel = ctx.author.dm_channel if send_in_dm else ctx.channel

    if send_in_dm and not target_channel:
        target_channel = await ctx.author.create_dm()

    await target_channel.send(f"Fetching messages for address {address}. This may take a moment...")

    url = f"https://rvn.cryptoscope.io/api/getaddressmessages/?address={address}"
    if since:
        url += f"&since={since}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                if data['result'] == 'success' and data['data']:
                    messages = data['data']
                    response_text = "Asset messages received:\n\n"
                    for msg in messages:
                        # Correctly use the timestamp from the message
                        timestamp = int(msg['timestamp'])
                        est_timezone = pytz.timezone('US/Eastern')
                        datetime_est = datetime.datetime.fromtimestamp(timestamp, tz=pytz.utc).astimezone(est_timezone)
                        formatted_time = datetime_est.strftime("%Y-%m-%d %H:%M:%S EST")

                        ipfs_link = msg.get('ipfs_link', 'No IPFS link available')
                        response_text += f"Timestamp: {formatted_time}\nTransaction: {msg['tx']}\nAsset: {msg['asset']}\nMessage: {msg['message']}\nIPFS Link: {ipfs_link}\n\n"

                    # Handle message length limitation
                    for chunk in [response_text[i:i + 2000] for i in range(0, len(response_text), 2000)]:
                        await target_channel.send(chunk)
                else:
                    await target_channel.send("No messages found for the specified address.")
            else:
                await target_channel.send("Failed to reach the Ravencoin Explorer API.")


# Command to get a users balance inside the Guild
@bot.command()
async def balance(ctx):
    user_id = str(ctx.author.id)

    # Load user data from the JSON file
    try:
        user_data = await asyncio.get_event_loop().run_in_executor(None, load_user_data)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        await ctx.send("Error loading user data. Please try again later.")
        print(e)  # Log the error for debugging
        return

    if user_id in user_data["users"]:
        user_info = user_data["users"][user_id]
        balance = user_info.get('tokens', 0)  # Default to 0 if 'tokens' not present
        address = user_info.get('address', 'Address not registered')
        vip_status = user_info.get('vip', 'No VIP status')  # Default message if 'vip' not present

        await ctx.send("Looking up your NiftyRaven address history with me...please hold.")
        await asyncio.sleep(1)  # pause for 1 second
        await ctx.send("Ah, there you are!")
        await ctx.send(f"Your balance is {balance} NIFTYRAVEN.COM tokens.")
        await ctx.send(f"Your Ravencoin address is: {address}.")
        await ctx.send(f"VIP Status: {vip_status}.")
    else:
        await ctx.send("You have not registered a Ravencoin address.")


# Command to get the market capitalization of Ravencoin
@bot.command()
async def marketcap(ctx):
    url = "https://rvn.cryptoscope.io/api/getmarketcapitalization/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                embed = discord.Embed(title="Market Capitalization", color=discord.Color.gold())
                for currency, value in data.get("currencies", {}).items():
                    embed.add_field(name=currency.upper(), value=value, inline=True)
                await ctx.send(embed=embed)
            else:
                await ctx.send("Failed to fetch market capitalization.")


# Command to get detailed asset information including IPFS content
@bot.command()
async def info(ctx, name: str, withtopholders: int = 0):
    encoded_name = name.replace('#', '%23').replace('&', '%26')
    api_url = f"https://rvn.cryptoscope.io/api/getassetinfo/?name={encoded_name}&withtopholders={withtopholders}"
    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                data = await response.json()
                if data['result'] == 'success':
                    asset_data = data['data']
                    embed = discord.Embed(title=f"Asset Information: {asset_data.get('name', 'Unknown')}", color=discord.Color.blue())
                    embed.add_field(name="Total Supply", value=f"{asset_data.get('supply', 'Unknown')} units", inline=False)
                    embed.add_field(name="Reissuable", value="Yes" if asset_data.get('reissuable') else "No", inline=False)
                    embed.add_field(name="Holders", value=str(asset_data.get('holders_count', 'Unknown')), inline=False)
                    if 'ipfs' in asset_data and asset_data['ipfs']:
                        ipfs_hash = asset_data['ipfs']
                        ipfs_url = f"https://ipfs.io/ipfs/{ipfs_hash}"
                        embed.add_field(name="IPFS Link", value=f"[View IPFS Content]({ipfs_url})", inline=False)
                        # Download and send IPFS content if needed (Example for images)
                        async with session.get(ipfs_url) as ipfs_response:
                            if ipfs_response.status == 200 and ipfs_response.content_type.startswith('image'):
                                img_data = await ipfs_response.read()
                                file = discord.File(io.BytesIO(img_data), filename="ipfs_content.png")
                                await ctx.send(embed=embed, file=file)
                            else:
                                await ctx.send(embed=embed)
                    else:
                        await ctx.send(embed=embed)
                else:
                    await ctx.send("Failed to fetch asset information. Please check the asset name.")
            else:
                await ctx.send("Failed to reach the Ravencoin Explorer API.")


# Command to get messages from an address
@bot.command()
async def getmessages(ctx, address: str, since: int = None):
    # Ensure the command's response is sent as a DM to maintain privacy
    if ctx.channel.type != discord.ChannelType.private:
        await ctx.author.send("Fetching your asset messages. This may take a few moments...")

    url = f"https://rvn.cryptoscope.io/api/getaddressmessages/?address={address}"
    if since:
        url += f"&since={since}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                if data['result'] == 'success':
                    messages = data['data']
                    if messages:
                        response_text = "Asset messages received:\n\n"
                        for msg in messages:
                            response_text += f"Timestamp: {msg['timestamp']}\nTransaction: {msg['tx']}\nAsset: {msg['asset']}\nMessage: {msg['message']}\n\n"
                        await ctx.author.send(response_text[:2000])  # Discord has a 2000 character limit per message
                    else:
                        await ctx.author.send("No messages found for the specified address and time frame.")
                else:
                    await ctx.author.send("Failed to fetch asset messages. Please check the address and/or timestamp.")
            else:
                await ctx.author.send("Failed to reach the Ravencoin Explorer API.")


# Manual upload pin and mint command
@bot.command(name='upload_and_mint')
async def upload_and_mint_process(ctx_or_interaction, user_address):
    addy = user_address
    print(f"{addy}")
    # Determine if the object is a context from a command or an interaction from a button click
    if isinstance(ctx_or_interaction, commands.Context):
        ctx = ctx_or_interaction
        user = ctx.author
        channel = ctx.channel
    elif isinstance(ctx_or_interaction, discord.Interaction):
        ctx = None  # There is no context when handling interactions
        user = ctx_or_interaction.user
        channel = ctx_or_interaction.channel
    else:
        raise ValueError("Invalid argument passed to upload_and_mint_process.")

    if not user_address:
        message = "Your address could not be found. Please register your address first."
        if isinstance(ctx_or_interaction, discord.Interaction):
            if ctx_or_interaction.response.is_done():
                await ctx_or_interaction.followup.send(message, ephemeral=True)
            else:
                await ctx_or_interaction.response.send_message(message, ephemeral=True)
        else:
            await ctx.send(message)
        return

    message_content = "Please type the name you want for your asset. Use '_' for spaces, '.' is allowed, no special characters."

    if isinstance(ctx_or_interaction, discord.Interaction):
        if ctx_or_interaction.response.is_done():
            await ctx_or_interaction.followup.send(message_content, ephemeral=True)
        else:
            await ctx_or_interaction.response.send_message(message_content, ephemeral=True)
    else:
        await ctx.send(message_content)

    def check_for_name(m):
        return m.author == user and m.channel == channel

    try:
        name_msg = await bot.wait_for('message', check=check_for_name, timeout=300)  # 5 minutes timeout
        asset_custom_name = name_msg.content.lower().replace(' ', '_')  # Normalize input
        if ctx:
            await ctx.send(f"Asset name received: {asset_custom_name}")
    except asyncio.TimeoutError:
        if ctx:
            await ctx.send("Asset naming timed out. Please try the command again and provide an asset name promptly.")
        return
    # Determine if the object is a context from a command or an interaction from a button click
    send = None
    if isinstance(ctx_or_interaction, commands.Context):
        ctx = ctx_or_interaction
        send = ctx.send
        user = ctx.author
    elif isinstance(ctx_or_interaction, discord.Interaction):
        ctx = None
        user = ctx_or_interaction.user
        send = ctx_or_interaction.response.send_message if not ctx_or_interaction.response.is_done() else ctx_or_interaction.followup.send

    if send is None:
        raise ValueError("Could not determine the method to send messages.")

    await send("Please upload the image you want to mint.")

    def check_for_image(m):
        return m.author == user and m.channel == ctx_or_interaction.channel and len(m.attachments) > 0

    try:
        image_msg = await bot.wait_for('message', check=check_for_image,
                                       timeout=300)  # 5 minutes timeout for image upload
        if not image_msg.attachments:
            await send("No image found. Please upload an image.")
            return

        image_url = image_msg.attachments[0].url
        ipfs_hash = await pin_image_to_ipfs_from_url(image_url)  # Assuming this function exists and properly implemented
        if ipfs_hash:


            full_asset_name = f"{user.name.lower().replace(' ', '_')}_{asset_custom_name}"  # Ensure this name adheres to Ravencoin naming conventions

            print(f"{full_asset_name}")

            mint_success, tx_id_or_error = await mintasset(full_asset_name, ipfs_hash, user_address)  # Assuming this function exists and properly implemented
            if mint_success:
                await send(
                    f"Asset {full_asset_name} minted and sent successfully! Transaction ID: {tx_id_or_error}")

            else:
                await send(f"There was an issue minting your asset: {tx_id_or_error}")
        else:
            await send("Failed to pin the image to IPFS. Please try again.")
    except asyncio.TimeoutError:
        await send("Image upload timed out. Please try the command again and upload an image promptly.")


# Command to list all the tokens for a user - NOT USED
@bot.command(name='listtokens')
async def list_tokens(ctx):
    user_id = str(ctx.author.id)
    address = get_user_address(user_id)
    if not address:
        await ctx.send("No Ravencoin address registered. Please register your address first.")
        return

    try:
        # Fetch tokens and their balances from the user's address
        asset_balances = await fetch_tokens_for_user(address)
        if not asset_balances:
            await ctx.send("No tokens found for your address.")
            return

        messages = []
        current_message = "Your Ravencoin Tokens:\n"

        for asset, balance in sorted(asset_balances.items()):
            # Fetch detailed asset data
            asset_data_response = await call_rpc("getassetdata", [asset])
            asset_data = asset_data_response.get("result", {})

            # Handle unit precision and IPFS hash
            ipfs_hash = asset_data.get("ipfs_hash", "")
            ipfs_url = f"https://nftrvn.mypinata.cloud/ipfs/{ipfs_hash}?pinataGatewayToken={api_token}" if ipfs_hash else ""

            line = f"  - **[{asset}]({ipfs_url})**" if ipfs_url else f"  - **{asset}**: {balance:.8f} Token(s)\n"

            if len(current_message) + len(line) > 2000:
                messages.append(current_message)
                current_message = ""

            current_message += line

        if current_message:
            messages.append(current_message)

        for message in messages:
            await ctx.send(message)

    except Exception as e:
        await ctx.send(f"Error retrieving asset balances: {e}")


# Command to mint an NFT - Not used
@bot.command(name='mintnft')
async def mint_nft_logic(ctx, interaction, address):
    call_rpc("walletpassphrase", ["135790", 6000])  # Unlock the wallet for 60 seconds
    user_id = ctx.author.id
    user_address = get_user_address(user_id)

    if not user_address:
        await ctx.send("Your address could not be found. Please register your address first.")
        return

    price = 30  # Set the price for minting an asset
    payment_received, payment_address = await gen_and_check_payment(ctx, price)
    if not payment_received:
        return  # Exit if payment was not received successfully

    await ctx.send("Payment received. Please type the name you want for your asset. Use '_' for spaces, '.' is allowed, no special characters.")

    def check_for_name(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        name_msg = await bot.wait_for('message', check=check_for_name, timeout=300)  # 5 minutes timeout
        asset_custom_name = name_msg.content.lower().replace(' ', '_')  # Convert to lowercase and replace spaces with underscores
        await ctx.send(f"Asset name received: {asset_custom_name}")
    except asyncio.TimeoutError:
        await ctx.send("Asset naming timed out. Please try the command again and provide an asset name promptly.")
        return

    await ctx.send("Please upload the image you want to mint.")

    def check_for_image(m):
        return m.author == ctx.author and m.channel == ctx.channel and len(m.attachments) > 0

    try:
        image_msg = await bot.wait_for('message', check=check_for_image, timeout=300)  # 5 minutes timeout for image upload
        if not image_msg.attachments:
            await ctx.send("No image found. Please upload an image.")
            return

        image_url = image_msg.attachments[0].url
        ipfs_hash = await pin_image_to_ipfs_from_url(image_url)
        if ipfs_hash:
            # Generate the full asset name in lowercase
            author_prefix = f"{ctx.author.name}".lower().replace(' ', '_')
            full_asset_name = f"{author_prefix}_{asset_custom_name}"  # Ensure this name adheres to Ravencoin naming conventions

            mint_success, tx_id_or_error = await mint_asset(ctx, full_asset_name, ipfs_hash, user_address)
            if mint_success:
                await ctx.send(f"Asset {full_asset_name} minted and sent successfully! Transaction ID: {tx_id_or_error}")
            else:
                await ctx.send(f"There was an issue minting your asset: {tx_id_or_error}")
        else:
            await ctx.send("Failed to pin the image to IPFS. Please try again.")
    except asyncio.TimeoutError:
        await ctx.send("Image upload timed out. Please try the command again and upload an image promptly.")


# Command to buy a specific token - Not used
@bot.command(name='buytoken')
async def buy_token(ctx, token_name: str, quantity: int):
    user_id = str(ctx.author.id)
    address = get_user_address(user_id)
    if not address:
        await ctx.send("You must have a registered Ravencoin address to buy tokens.")
        return

    token_data = load_token_data()
    if token_name in token_data and token_data[token_name]["listings"]:
        listing = token_data[token_name]["listings"][0]  # Example: Using the first listing
        if quantity > listing["quantity"]:
            await ctx.send("Not enough tokens available.")
            return

        # Simulate transaction success
        log_token_sale(token_name, listing["seller_id"], user_id, listing["price"], quantity)
        await ctx.send(f"Successfully purchased {quantity} units of {token_name} from {listing['seller_id']}.")
    else:
        await ctx.send("Token not available for sale.")


# Command to process a sale - Not used
@bot.command()
async def process_sale(ctx, listed_address, buyer_address, seller_address, asset_name, sale_price_rvn, token_amount):
    # Assume 'nifty' and 'nifty_address' are globally available or replace with appropriate values
    net_amount = sale_price_rvn * 0.94  # Calculate the net amount after a 6% fee

    # Transfer RVN to the seller
    rvn_response = await call_rvn_rpc("sendfromaddress", [listed_address, seller_address, net_amount, "Website Sale RVN to SELLER", True, ""])
    if rvn_response is None or "result" not in rvn_response:
        await bot.get_channel(1155533165679611964).send("Error sending RVN.")
        return
    #await call_rvn_rpc("walletpassphrase", ["Password1!", 60000000000])  # Unlock the wallet for 60 seconds
    # Transfer the token to the buyer
    token_response = await call_rvn_rpc2("transferfromaddress", [asset_name, listed_address, token_amount, buyer_address, "", 0, "", listed_address])
    if token_response is None or "result" not in token_response:
        await bot.get_channel(1155533165679611964).send("Error sending token.")
        return

    # Log the transaction
    log_token_sale(asset_name, seller_address, buyer_address, sale_price_rvn, token_amount)
    sent_rvn_txid = rvn_response['result']
    sent_token_txid = token_response['result']

    # Send a confirmation message to the appropriate channel
    channel = bot.get_channel(1213694827305238528)
    if channel:
        embed = discord.Embed(title="Token Sale Transaction Completed", description="Details of the transaction", color=0x00ff00)
        embed.add_field(name="Asset Name", value=asset_name, inline=False)
        embed.add_field(name="Amount RVN", value=net_amount, inline=True)
        embed.add_field(name="Seller Address", value=seller_address, inline=True)
        embed.add_field(name="Buyer Address", value=buyer_address, inline=True)
        embed.add_field(name="RVN Transaction ID", value=sent_rvn_txid, inline=False)
        embed.add_field(name="Token Transaction ID", value=sent_token_txid, inline=False)
        await channel.send(embed=embed)

    await ctx.send(f"Sale processed successfully. RVN and {asset_name} have been transferred.")


# Command to get information about an asset on Ravencoin 
@bot.command()
async def getinfo(ctx, asset_name: str):
    result = call_rpc("getassetdata", [asset_name])
    if result is None:
        await ctx.send("Oops! Something went wrong. We couldn't get the information right now.")
        return
    if 'error' in result and result['error']:
        await ctx.send(f"Whoops! There was a problem: {result['error']['message']}")
        return

    asset_data = result.get('result', {})
    if not asset_data:
        await ctx.send(f"Hmm, we couldn't find any data for {asset_name}. Are you sure that's the right name?")
        return

    # Assuming call_rpc is an existing function that calls your RPC server
    response = call_rpc("listaddressesbyasset", [asset_name, True])
    if 'result' not in response:
        await ctx.send("Failed to retrieve data. Please try again later.")
        return

    total_addresses = response['result']

    encoded_asset_name = custom_url_encode(asset_name)


    default_amount = "It's a secret"  # Set the default message without complicating the f-string
    embed = discord.Embed(title=f"Details for {asset_data.get('name', 'a mystery asset')}", color=discord.Color.blue())
    embed.add_field(name="Name", value=f"[{asset_data.get('name', 'Unknown')}]https://ravencoin.asset-explorer.net/a/{encoded_asset_name})")
    embed.add_field(name="Total Amount", value=f"{asset_data.get('amount', default_amount)} units")
    embed.add_field(name="Smallest Unit", value=f"1/{10 ** asset_data.get('units', 0)} of a unit")
    embed.add_field(name=f"# of Address HODLING {asset_name}", value=f"{total_addresses}")
    reissuable = "Yes" if asset_data.get('reissuable') else "No"
    embed.add_field(name="Can Make More?", value=reissuable)
    has_ipfs = "Yes" if asset_data.get('has_ipfs') else "No"
    embed.add_field(name="ipfs/txid attached?", value=has_ipfs)

    if asset_data.get('has_ipfs') and 'ipfs_hash' in asset_data:
        ipfs_hash = asset_data['ipfs_hash']
        ipfs_url = f"https://nftrvn.mypinata.cloud/ipfs/{ipfs_hash}?pinataGatewayToken={api_token}"
        embed.set_image(url=ipfs_url)  # Optionally set an image or video preview if applicable
        embed.add_field(name="View Full Content", value=f"[Click Here]({ipfs_url})", inline=False)

    await ctx.send(embed=embed)


# Command to pin an IPFS hash
@bot.command()
async def pin(ctx, ipfs_hash: str):
    print(f"Pin command invoked by {ctx.author} with IPFS hash: {ipfs_hash}")

    try:
        ipfs_url = f"https://nftrvn.mypinata.cloud/ipfs/{ipfs_hash}/?pinataGatewayToken={api_token}"

        response = requests.head(ipfs_url, timeout=10)
        file_size = int(response.headers.get('content-length', 0))
        print(f"File size fetched: {file_size} bytes")

        if file_size > MAX_FILE_SIZE:
            await ctx.send(f"File size exceeds {MAX_FILE_SIZE // 1_000_000} MB limit.")
            return
    except requests.RequestException as e:
        await ctx.send(f"Error fetching file size: {e}")
        print(f"Error in fetching file size: {e}")
        return

    await ctx.send("Enter the NFT name:")
    try:
        nft_name_msg = await bot.wait_for('message', timeout=60.0,
                                          check=lambda message: message.author == ctx.author)
        nft_name = nft_name_msg.content
        print(f"NFT name received: {nft_name}")
    except asyncio.TimeoutError:
        await ctx.send("Timeout. NFT name not provided.")
        print("Timeout in receiving NFT name.")
        return

    success, pin_response = pin_item(ipfs_hash, nft_name)
    if success:
        await ctx.send(f"Pinned successfully: {pin_response['ipfsHash']}")
        print(f"Pin response: {pin_response}")
        # Rest of your code to handle file download and upload to Discord...

        # Download the file from IPFS
        file_response = requests.get(ipfs_url)
        if file_response.status_code == 200:
            file_extension = determine_file_extension(file_response.headers.get('content-type'))
            file_name = f"{ipfs_hash}.{file_extension}"
            print(f"Downloading file: {file_name}")

            with open(file_name, 'wb') as file:
                file.write(file_response.content)

            # Check if file is small enough to send on Discord
            if os.path.getsize(file_name) <= MAX_FILE_SIZE:
                with open(file_name, 'rb') as file:
                    await ctx.send("Pinned file:", file=discord.File(file, file_name))
                    print(f"File sent to Discord: {file_name}")
            else:
                await ctx.send("File pinned, but too large to upload to Discord.")
                print(f"File too large to upload to Discord: {file_name}")

            # Delete the file from local storage
            os.remove(file_name)
            print(f"File deleted from local storage: {file_name}")
        else:
            await ctx.send("Failed to download the file from IPFS.")
            print(f"Failed to download file from IPFS: {ipfs_url}")
    else:
        await ctx.send("Error during pinning. Please try again.")
        print(f"Error in pinning: Response - {pin_response}")


# Command to list all the pinned items on NFTRVN Pinata
@bot.command()
async def pinlist(ctx, page: int = 1):
    # List of allowed user IDs
    allowed_users = ["152984492116672512", "1153405725381509120", "971210087752413255", "817625651879477258", "927814688409014292", "586827968387612682"]
    # Check if the user is allowed to use this command
    if str(ctx.author.id) not in allowed_users:
        await ctx.send("You do not have permission to use this command.")
        return
    user = ctx.message.author  # Get the user who invoked the command
    keep_fetching = True

    while keep_fetching:
        headers = {
            "pinata_api_key": PINATA_API_KEY,
            "pinata_secret_api_key": PINATA_API_SECRET
        }

        params = {
            'pageLimit': 10,  # Number of items per page
            'pageOffset': (page - 1) * 10  # Calculate offset for pagination
        }

        response = requests.get(f"{API_BASE_URL}/data/pinList", headers=headers, params=params)
        if response.status_code == 200:
            pin_list = response.json()
            dm_message = f"Pinned Files on Page {page}:\n"
            for pin in pin_list['rows']:
                dm_message += f"- {pin['ipfs_pin_hash']} (Name: {pin['metadata']['name'] if 'name' in pin['metadata'] else 'N/A'})\n"

            # Send DM to the user
            await user.send(dm_message)

            # Ask in DM if the user wants to fetch the next page
            await user.send(f"Displayed page {page}. Type 'next' to view the next page, or 'stop' to end.")
            try:
                next_page_msg = await bot.wait_for('message', timeout=60.0, check=lambda
                    message: message.author == ctx.author and message.content.lower() in ['next',
                                                                                          'stop'] and isinstance(
                    message.channel, discord.DMChannel))
                if next_page_msg.content.lower() == 'next':
                    page += 1
                else:
                    keep_fetching = False
            except asyncio.TimeoutError:
                await user.send("Timed out waiting for response. Stopping pagination.")
                keep_fetching = False
        else:
            await user.send(f"Failed to retrieve pin list for page {page}.")
            keep_fetching = False

    # Send a final message in the channel to confirm command execution
    await ctx.send(f"{ctx.author.mention}, check your DMs for the pin list.")


# Command to payout bounties
@bot.command()
async def payout(ctx, amt_rvn: float, thread_id: int):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("🔒 You must be an admin to use this command.")
        return

    try:
        thread = await ctx.guild.fetch_channel(thread_id)
    except:
        await ctx.send("❌ Thread not found. Please check the thread ID.")
        return

    file_path = "C:/Users/NFTRVN/Documents/NFTRVN Token Bot/user_data.json" # Revise this to your user_data.json path

    eligible_users = []
    async for message in thread.history(limit=None):
        thumbs_up_count = sum([react.count for react in message.reactions if str(react.emoji) == "👍"])
        if thumbs_up_count >= 5:
            address = get_user_address(message.author.id)
            if address:
                eligible_users.append((message.author.id, message.author.display_name, address))
                # Remove reactions
                for reaction in message.reactions:
                    await message.clear_reaction(reaction.emoji)

    if not eligible_users:
        await ctx.send("ℹ️ No eligible users found in this thread for a payout.")
        return

    # Process payouts
    for user_id, username, address in eligible_users:
        txid = call_rpc("sendfromaddress", ["R9ssT21TmkgDsdJYCcmfv3qnuoREzzZvzk", address, amt_rvn])

        if txid:
            tx_link = f"https://rvn.cryptoscope.io/tx/?txid={txid}"
            await ctx.send(f"✅ Sent {amt_rvn} RVN to **{username}**. [Transaction Details]({tx_link})")

    # Notify role about bounty completion
    role = ctx.guild.get_role(939101943375220746)
    if role:
        await ctx.send(f"{role.mention} Bounty payout completed. Check transactions above.")

    # Make announcement in the thread
    if thread:
        await thread.send(f"{role.mention} Bounties paid, and REACTIONS REMOVED FROM THIS POINT ON, DO NOT REACT TO A POST ABOVE THIS POST")

    # Make announcement in the announcement channel
    announcement_channel = ctx.guild.get_channel(1213694827305238528)
    if announcement_channel:
        embed = Embed(title="🎉 Bounty Payout Completed", description="Details about the recent bounty payout.")
        embed.set_image(url="https://nftrvn.mypinata.cloud/ipfs/QmRr15opH2rgCrjxuUhPV2xxdWwGhHSmNn5vvmzKpvafqd")
        embed.set_thumbnail(url="https://nftrvn.mypinata.cloud/ipfs/QmRr15opH2rgCrjxuUhPV2xxdWwGhHSmNn5vvmzKpvafqd")
        # Optionally add more fields to embed with further details
        await announcement_channel.send(embed=embed)


# NFTRVN Command for listing and buying tokens
@bot.command(name='NFTRVN', help='Starts the token listing or buying process.')
async def nftrvn(ctx):
    view = TokenActionView()
    await ctx.send("Are you looking to **buy** or **list** tokens?", view=view)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        response = await bot.wait_for('message', timeout=560.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send('🕒 Timeout. Please try the command again if you wish to buy or list tokens.')
        # Delete the buttons here
        await interaction.message.delete()
        return
    else:
        if response.content.lower() == 'buy':
            await ctx.send('You chose to buy tokens. [Placeholder for further process]')
        elif response.content.lower() == 'list':
            await ctx.send('Starting the listing process. Please wait...')

            user_address = await get_user_address(ctx.author.id)
            if user_address:
                await ctx.send(f"Your registered address is: {user_address}")
            else:
                await ctx.send("No address found. Please register your address first.")
                return

            new_address = await get_new_address()
            await ctx.send(f"Please send the asset you want to list to the following address: {new_address}")
            await ctx.send('Please type "done" once you have sent the assets. We will start checking the balance.')


# Command to unlockwallet
@bot.command()
async def unlockwallet(ctx):
    try:
        # Call the RPC function to unlock the wallet
        response = call_rpc("walletpassphrase", ["135790", 6000])
        # Check if the RPC call was successful
        if response.get('result') == 'success':
            await ctx.send("The wallet has been successfully unlocked for 100 minutes.")
        else:
            await ctx.send(f"Failed to unlock the wallet: {response.get('data')}")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")


# NFTRVN Command process - Get a listed assets information
@bot.command()
async def assetinfo(ctx, encoded_asset_name: str):
    decoded_name = urllib.parse.unquote(encoded_asset_name)
    file_name = f"{decoded_name.replace('/', '-').replace('#', '_')}.json"
    try:
        with open(file_name, 'r') as file:
            asset_data = json.load(file)

        embed = discord.Embed(title=f"Asset Details: {decoded_name}", description="Comprehensive information about the asset:", color=discord.Color.gold())
        embed.add_field(name="Asset Name", value=asset_data.get('name', 'Unknown'), inline=False)
        embed.add_field(name="Total Supply", value=f"{asset_data['supply']} units", inline=True)
        embed.add_field(name="Price per Unit", value=f"{asset_data.get('ppa', 'N/A')} RVN", inline=True)
        embed.add_field(name="Total Listed", value=f"{asset_data.get('amount_listed', 0)} units", inline=True)
        embed.add_field(name="Seller", value=asset_data.get('seller', 'N/A'), inline=True)
        embed.add_field(name="Seller Address", value=asset_data.get('seller_address', 'N/A'), inline=False)
        embed.add_field(name="Transaction Type", value=asset_data.get('transaction_type', 'N/A'), inline=False)
        embed.add_field(name="All-Time High Price", value=f"{asset_data.get('ath_price', 'N/A')} RVN", inline=True)
        embed.add_field(name="All-Time Low Price", value=f"{asset_data.get('atl_price', 'N/A')} RVN", inline=True)
        embed.add_field(name="Asset Type", value=asset_data.get('asset_type', 'Unknown'), inline=False)
        embed.add_field(name="Reissuable", value="Yes" if asset_data.get('reissuable', 0) else "No", inline=True)
        embed.add_field(name="IPFS Attached", value="Yes" if asset_data.get('has_ipfs', 0) else "No", inline=True)
        if asset_data.get('has_ipfs', 0):
            ipfs_url = f"https://ipfs.io/ipfs/{asset_data.get('ipfs_hash', '')}"
            embed.add_field(name="IPFS Link", value=f"[View IPFS Content]({ipfs_url})", inline=False)

        await ctx.send(embed=embed)
    except FileNotFoundError:
        await ctx.send(f"No detailed data available for {decoded_name}.")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Not working minting command
@bot.command()
async def nft(ctx, ipfs_hash: str, asset_name: str):
    user_id = str(ctx.author.id)
    # Define a path to your file, adjust according to your actual file location
    file_path = "C:/Users/neron/Documents/NFTRVN Token Bot/user_data.json"

    # Load user data from the JSON file
    try:
        # Use aiofiles if available for true async file operations
        user_data = await asyncio.get_event_loop().run_in_executor(None, lambda: load_user1_data(file_path))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        await ctx.send("Error loading user data. Please try again later.")
        print(e)  # Log the error for debugging
        return

    if user_id in user_data["users"]:
        balance = user_data["users"][user_id]['tokens']
        user_address = user_data["users"][user_id]['address']
    if not user_address:
        await ctx.send("No Ravencoin address found for this user. Please register your address using ?myaddy command.")
        return
    if len(asset_name) > 23:
        await ctx.send("Asset name is too long. Maximum length is 23 characters.")
        return

    mint_address = "RDDMomZXmKpoejwRBYDPxXLvdLH3k3V7Hc"
    await ctx.send(f"Please send 20 RVN to the following address, once sent paste the txid below:")
    await ctx.send(f"{mint_address}")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        msg = await bot.wait_for("message", check=check, timeout=300)  # Wait for the user's message for 5 minutes
    except asyncio.TimeoutError:
        await ctx.send("Timed out. Please try again.")
        return

    txid = msg.content
    if txid in processed_txids:
        await ctx.send("This transaction ID has already been processed. Please provide a different transaction ID.")
        return

    processed_txids.add(txid)

    raw_tx = call_rpc("getrawtransaction", [txid])
    if raw_tx is None or "result" not in raw_tx:
        await ctx.send("Invalid transaction ID. Please provide a valid transaction ID.")
        return

    decoded_tx = call_rpc("decoderawtransaction", [raw_tx["result"]])
    if decoded_tx is None or "result" not in decoded_tx or "vout" not in decoded_tx["result"]:
        await ctx.send("Error decoding transaction. Please try again.")
        return

    sent_amount = 0
    for output in decoded_tx["result"]["vout"]:
        if output["scriptPubKey"]["addresses"][0] == mint_address:
            sent_amount += output["value"]

    if sent_amount != 20.0:
        await ctx.send("Incorrect amount sent. Please send exactly 20 RVN.")
        return

    asset_tags = [asset_name]
    if ipfs_hash != "":
        ipfs_hashes = [ipfs_hash]
        result = call_rpc("issueunique", ["NFTRVN", asset_tags, ipfs_hashes])
    else:
        result = call_rpc("issueunique", ["NFTRVN", asset_tags])

    if result is None or "result" not in result:
        await ctx.send("Error minting NFT. Please try again.")
        return
    print(f"result = {result}")

    asset_txid = result["result"]

    # Update successful mints count for the user
    user_id_str = str(ctx.author.id)
    if user_id_str not in user_data:
        user_data[user_id_str] = {"mints": 0}

    user_data[user_id_str]["mints"] += 1
    save_user_data()

    await ctx.send(f"NFT minted successfully! Please allow up to 3 minutes for confirmation, asset will be sent after confirmations. Asset: NFTRVN#{asset_name}, Transaction: {result}")

    # Send NIFTYRAVEN.COM/TOKEN_2.0 immediately
    from_address = "RG3RxHpUQm14vY1mDZvHNCkfH4eZhjS6eZ"
    #await call_rvn_rpc("walletpassphrase", ["Password1!", 60000000000])  # Unlock the wallet for 60 seconds
    token_2_0_result = call_rpc("transferfromaddress", ["NIFTYRAVEN.COM", from_address, 15, user_address, "", 0, "", from_address])
    if token_2_0_result is None or "result" not in token_2_0_result:
        await ctx.send("Error sending NIFTYRAVEN.COM asset.")
        return

    token_2_0_txid = token_2_0_result['result']
    await ctx.send(f" You just received: (15) NIFTYRAVEN.COM! Transaction ID: <https://explorer.mangofarmassets.com/tx/{token_2_0_txid[0]}>")

    # Wait for 2 minutes
    await asyncio.sleep(180)



    result = call_rpc("transfer", [f"NFTRVN#{asset_name}", 1, user_address])
    if result is None or "result" not in result:
        await ctx.send("Error sending asset.")
        return

    sent_txid = result['result']
    await ctx.send(
        f"Asset NFTRVN#{asset_name} sent! Thank you for supporting the NFTRVN Community! Transaction ID: <https://explorer.mangofarmassets.com/tx/{sent_txid[0]}>")


    # Send 7.5 RVN to Token Helpers
    send_rvn_result = call_rpc("sendfromaddress", [mint_address, "RAE1u9GFjVd2M1Tbj2suvUrkx2qTCb9A1S", 7.5])
    if send_rvn_result is None or "result" not in send_rvn_result:
        await ctx.send("Error sending 7.5 RVN to RAE1u9GFjVd2M1Tbj2suvUrkx2qTCb9A1S.")
        return

    channel = bot.get_channel(1094831496566689802)
    if channel:
        # Send 7.5 RVN to Referral
        send_rvn_result = call_rpc("sendfromaddress", [mint_address, "RGETN7Mq6JZ8Whjvg45wUeFjeysj1gi2pN", 7.5])
        if send_rvn_result is None or "result" not in send_rvn_result:
            await ctx.send("Error sending 7.5 RVN to RGETN7Mq6JZ8Whjvg45wUeFjeysj1gi2pN.")
            return


    # Send 7.5 RVN to OWNER
    send_rvn_result = call_rpc("sendfromaddress", [mint_address, "RGETN7Mq6JZ8Whjvg45wUeFjeysj1gi2pN", 7.5])
    if send_rvn_result is None or "result" not in send_rvn_result:
        await ctx.send("Error sending 7.5 RVN to RGETN7Mq6JZ8Whjvg45wUeFjeysj1gi2pN.")
        return


# Command to set the active channel
@bot.command(name='setactivechannel')
@commands.has_permissions(administrator=True)
async def set_active_channel(ctx):
    active_channels = load_active_channels()
    active_channels[str(ctx.guild.id)] = ctx.channel.id
    save_active_channels(active_channels)
    await ctx.send(f"Active channel set to {ctx.channel.mention}!")


# Get the amount of guilds the bot is in and names of guilds
@bot.command(name='guildcount')
async def guild_count(ctx):
    guilds = bot.guilds
    if len(guilds) > 10:  # Arbitrary number, adjust based on what you feel is too many to display
        await ctx.send(f'I am in {len(guilds)} guilds. Here are the first 10:')
        guilds_list = "\n".join(guild.name for guild in guilds[:10])
        await ctx.send(guilds_list)
    else:
        await ctx.send(f'I am in {len(guilds)} guilds:')
        guilds_list = "\n".join(guild.name for guild in guilds)
        await ctx.send(guilds_list)


# Get the registered addresses for the guilds that invited the NiftyMinter
@bot.command(name='guildinfo')
async def guild_info(ctx):
    # Check if the user has the "Administrator" permission
    # Load guild info from JSON file
    with open("guilds_info.json", "r") as f:
        guild_info = json.load(f)

    # Get current guild ID as a string
    guild_id = str(ctx.guild.id)

    # Retrieve guild-specific addresses
    guild_addresses = guild_info.get("guilds", {}).get(guild_id, {})
    token_helpers_address = guild_addresses.get("token_helpers", "DefaultTokenHelpersAddress")
    guild_address = guild_addresses.get("guild", "DefaultGuildAddress")
    nftrvn_owner_address = guild_addresses.get("ref", "DefaultOwnerAddress")
    if ctx.author.guild_permissions.administrator:
        guild_id = str(ctx.guild.id)  # Convert the guild ID to string to match JSON keys
        if guild_id in guild_info:
            # Constructing the message
            info = guild_info[guild_id]

            message = f"Guild Information:\nToken Helpers: {info['token_helpers']}\nGuild: {info['guild']}\nRef: {info['ref']}"
            await ctx.send(message)
        else:
            await ctx.send("No information found for this guild.")
    else:
        await ctx.send("You do not have permission to use this command.")


# Command to get the leaderboard of minters - WIP
@bot.command()
async def leaderboard(ctx):
    with open(USER_DATA_FILE, "r") as f:
        user_data = json.load(f)["users"]  # Assuming "users" is a key in your JSON

    # Sort users by 'mints', handling cases where 'mints' might not exist
    leaderboard_data = sorted(user_data.items(), key=lambda x: x[1].get('mints', 0), reverse=True)
    leaderboard_text = "Top Minters in the world for NiftyMinter:\n"
    for i, (user_id, user_stats) in enumerate(leaderboard_data[:10], start=1):
        user = bot.get_user(int(user_id))  # Attempt to get user object
        user_name = user.name if user else "User not found"  # Handle case where user is None
        mints = user_stats.get('mints', 0)  # Handle case where 'mints' key does not exist
        leaderboard_text += f"{i}. {user_name} - {mints} mints\n"

    await ctx.send(leaderboard_text)


############################################################################################################
# COMMANDS END
############################################################################################################
#################################################
#################################################
########################################################################################################################
########################################################################################################################
# EVENTS & TASKS & LOOPS START
############################################################################################################

# Event to announce when a member joins the server
@bot.event
async def on_member_join(member):
    # Define the channel to send the welcome message
    welcome_channel = bot.get_channel(939095887576195076)  # Replace with your channel ID

    # Fetch user banner URL
    user = await bot.fetch_user(member.id)  # Fetch user details
    banner_url = user.banner.url if user.banner else None  # Check if the user has a banner

    # Create an embed for the welcome message
    embed = discord.Embed(title="Welcome to NiftyRaven Discord!", description=f"Hello {member.mention}, welcome to the community! We're glad to have you here.", color=discord.Color.blue())
    if banner_url:
        embed.set_image(url=banner_url)  # Set the user's banner as the image
    embed.set_thumbnail(url=member.avatar.url)  # Set the user's avatar as the thumbnail
    embed.add_field(name="Member Count", value=f"You are member #{member.guild.member_count}!")

    # Send the welcome message
    await welcome_channel.send(embed=embed)


# Routine to get IPFS hash from a message and view it
@app.route('/get_ipfs_url', methods=['GET'])
def get_ipfs_url():
    ipfs_hash = request.args.get('hash')
    api_token = "your_token"  # Your API token
    url = f"https://nftrvn.mypinata.cloud/ipfs/{ipfs_hash}?pinataGatewayToken={api_token}"
    return jsonify({'url': url})


# Routine to send a message to a Discord channel
@app.route('/send_discord_message', methods=['POST'])
def send_discord_message():
    channel_id = request.form.get('channel_id')
    message = request.form.get('message')
    asyncio.run_coroutine_threadsafe(send_message_to_discord(channel_id, message), bot.loop)
    return "Message sent!"


# Error handler for the 'setactivechannel' command
@set_active_channel.error
async def set_active_channel_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You must have administrator permissions to use this command.")
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("An unexpected error occurred while processing your command.")
    else:
        raise error


# Loop to clear messages inside of a channel specified by ID
@tasks.loop(hours=2)
async def clear_channel_messages():
    target_channel = bot.get_channel(1094831496566689802)  # Replace TARGET_CHANNEL_ID with the ID of the channel you want to clear
    if target_channel:
        await target_channel.purge()
    else:
        print(f"Unable to find channel with ID {TARGET_CHANNEL_ID}")


# Loop to post Ravencoin price every 20 minutes
@tasks.loop(minutes=20)  # Adjust the update interval as needed
async def post_ravencoin_price():
    message_channel = bot.get_channel(MESSAGE_CHANNEL_ID)
    price = get_ravencoin_price()
    await message_channel.send(f"Ravencoin Price: ${price:.5f}")
    print(f"Posted message: Ravencoin Price: ${price:.5f}")

    name_update_channel = bot.get_channel(NAME_UPDATE_CHANNEL_ID)
    await name_update_channel.edit(name=f"$RVN: ${price:.5f}")
    print(f"Updated channel name to: Ravencoin Price: ${price:.5f}")

    # Fetch RVN/BTC price
    rvn_btc_price = get_rvn_to_btc_price()

    # Update the RVN/BTC channel with the fetched price
    rvn_btc_channel = bot.get_channel(1153876135877292042)
    await rvn_btc_channel.edit(name=f"RVN/BTC: {rvn_btc_price:.8f}")  # Adjust the format as needed
    print(f"Updated LAMPA RVN/BTC channel name to: {rvn_btc_price:.8f}")

    # Update the RVN/BTC channel with the fetched price
    rvn_btc_channel = bot.get_channel(BTC_CHANNEL)
    await rvn_btc_channel.edit(name=f"RVN/BTC: {rvn_btc_price:.8f}")  # Adjust the format as needed
    print(f"Updated NIFTYRAVEN RVN/BTC channel name to: {rvn_btc_price:.8f}")


# Loop to send random messages to a channel
@tasks.loop(minutes=20)
async def random_message_loop():
    target_channel_id = 1094831496566689802  # Replace with the ID of the channel where you want to send random messages
    await send_random_message(target_channel_id)


# Command to execute a terminal command and send the output to a channel
@bot.event
async def on_message(message):
    if message.content.startswith('?'):
        # Extract the command without the prefix
        cmd = message.content[1:]

        # Check if the command is a recognized bot command
        context = await bot.get_context(message)
        if bot.get_command(cmd.split()[0]):
            # Use a StringIO to capture the command's output
            with contextlib.redirect_stdout(io.StringIO()) as f:
                await bot.invoke(context)
            output = f.getvalue()

            # Include user who ran the command
            user_info = f"Command run by: {message.author.mention}"

            # Send the captured output to the channel
            channel = bot.get_channel(1237939399380045886)  # Replace with your channel ID
            await channel.send(f"Command: `{cmd}`\nOutput:\n```\n{output}\n```\n{user_info}")
        else:
            # Handle unrecognized commands
            output = f"Error: `{cmd}` is not a recognized command."
            user_info = f"Command run by: {message.author.mention}"
            channel = bot.get_channel(1237939399380045886)  # Replace with your channel ID
            await channel.send(f"{output}\n\n{user_info}")
    else:
        await bot.process_commands(message)


# Event to initialize the bot when it's ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    guild_count = len(bot.guilds)  # Count how many guilds (servers) the bot is connected to
    print(f'The bot is in {guild_count} guilds.')
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    post_ravencoin_price.start()
    random_message_loop.start()  # Add this line to start the random message loop


############################################################################################################
# EVENTS & TASKS & LOOPS END
############################################################################################################
############################################################################################################
############################################################################################################
###################################################################################################
#######################################################################################
###########################################################################
################################################################
#################################################
############################################
#########################################
#####################################
#################################
##############################
##########################
######################
##################
################
##############
############################################################################################################
# MAIN START
############################################################################################################

# Start the main loop
if __name__ == '__main__':
    bot.run(TOKEN)


############################################################################################################
# MAIN END
############################################################################################################
##############
################
##################
######################
##########################
##############################
#################################
#####################################
#########################################
############################################
#################################################
################################################################
###########################################################################
#######################################################################################
###################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
#################################################
#################################################
#################################################
############################################################################################################
# EXTRA FUNCTIONS START
############################################################################################################


###WORKING GET MSGS###
"""@bot.command()
async def getmsgs(ctx, address: str, since: int = None):
    # Ensure the command's response is sent as a DM to maintain privacy
    if ctx.channel.type != discord.ChannelType.private:
        await ctx.author.send("Fetching your asset messages. This may take a few moments...")

    url = f"https://rvn.cryptoscope.io/api/getaddressmessages/?address={address}"
    if since:
        url += f"&since={since}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                if data['result'] == 'success':
                    messages = data['data']
                    if messages:
                        response_text = "Asset messages received:\n\n"
                        for msg in messages:
                            response_text += f"Timestamp: {msg['timestamp']}\nTransaction: {msg['tx']}\nAsset: {msg['asset']}\nMessage: {msg['message']}\n\n"
                        await ctx.author.send(response_text[:2000])  # Discord has a 2000 character limit per message
                    else:
                        await ctx.author.send("No messages found for the specified address and time frame.")
                else:
                    await ctx.author.send("Failed to fetch asset messages. Please check the address and/or timestamp.")
            else:
                await ctx.author.send("Failed to reach the Ravencoin Explorer API.")
"""


"""
@bot.command()
async def listaddresses(ctx, asset_name: str):
    addresses = call_rpc("listaddressesbyasset", [asset_name])
    if addresses is None or "result" not in addresses or not addresses["result"]:
        await ctx.send(f"No addresses found for asset: {asset_name}")
        return

    # Create the table header
    table_header = f"| {'Address':<34} | {'Asset Name':<20} | {'Quantity':<20} |\n"
    table_header += f"|{'-' * 34}|{'-' * 22}|{'-' * 22}|\n"

    # Add table rows for each address
    table_data = ""
    for address, balance in addresses["result"].items():
        table_data += f"| {address:<34} | {asset_name:<20} | {balance:<20} |\n"

    # Combine header and data
    table = table_header + table_data

    # Split the table into chunks of 1950 characters
    chunks = [table[i:i + 1950] for i in range(0, len(table), 1950)]

    # Send the chunks one by one
    for chunk in chunks:
        await ctx.send(f"```\n{chunk}\n```")
"""


"""@bot.command()
async def pin(ctx, ipfs_hash: str):
    if any(role.id in VIP_ELITE_ROLE_IDS for role in ctx.author.roles):
        # Fetch the file size from your IPFS gateway
        ipfs_url = f"https://nftrvn.mypinata.cloud/ipfs/{ipfs_hash}/?pinataGatewayToken={api_token}"
        try:
            response = requests.head(ipfs_url, timeout=10)
            file_size = int(response.headers.get('content-length', 0))
        except requests.RequestException:
            await ctx.send("Error fetching the file size from IPFS. Please try again later.")
            return

        if file_size > MAX_SIZE_BYTES:
            await ctx.send(f"The file size exceeds the limit of {MAX_SIZE_BYTES // 1000000}MB. Please provide a smaller file.")
            return

        # Ask the user for the NFT name
        await ctx.send("Please enter the name for the NFT:")
        try:
            nft_name_msg = await bot.wait_for('message', timeout=60.0, check=lambda message: message.author == ctx.author)
            nft_name = nft_name_msg.content
        except asyncio.TimeoutError:
            await ctx.send("You did not enter the NFT name in time.")
            return

        response = pin_item(ipfs_hash, nft_name)
        if response and "IpfsHash" in response:
            await ctx.send(f"Pinned successfully. IPFS Hash: {response['IpfsHash']}")
            # Download the file from your IPFS gateway
            file_response = requests.get(ipfs_url)
            if file_response.status_code == 200:
                file_extension = determine_file_extension(file_response.headers.get('content-type'))
                file_name = f"{ipfs_hash}.{file_extension}"

                with open(file_name, 'wb') as file:
                    file.write(file_response.content)

                # Send file to Discord channel if it's within the size limit
                if os.path.getsize(file_name) <= MAX_FILE_SIZE:
                    with open(file_name, 'rb') as file:
                        await ctx.send("Pinned file:", file=discord.File(file, file_name))
                else:
                    await ctx.send("Pinned successfully, but the file is too large to upload to Discord.")

                # Delete the file from local storage
                os.remove(file_name)

            await ctx.send(f"Pinned successfully. IPFS Hash: {ipfs_hash}")
        else:
            await ctx.send(f"Error pinning IPFS hash {ipfs_hash}. Please try again later.")
    else:
        await ctx.send("You do not have permission to use this command.")
"""


"""async def monitor_asset_transfer(interaction, new_address, user_address):
    async def check_assets():
        for i in range(10):  # 10 minutes loop
            asset_name, asset_balance = await wait_for_asset_balance(new_address)

            if asset_balance:
                await interaction.followup.send(f'Assets received: {asset_name}  Proceeding to process the listing...')
                asset_data = await call_rvn_rpc("getassetdata", [asset_name])  # Fetch dynamic asset data
                asset_units = asset_data['units']  # Extract asset units dynamically

                await interaction.followup.send(f'{asset_units} {asset_name} received at {new_address}. Processing the listing further...')
                # Now you have the asset data including its name, do whatever processing you need


                # Transfer assets to a dedicated account (needs to be handled carefully and securely)
                account_address = await get_or_create_asset_account(asset_name, new_address)
                await transfer_asset(asset_name, new_address, asset_balance, account_address, "Transferred for listing.")


                ipfs_hash = asset_data['ipfs_hash']
                price_per_unit = await ask_for_price(interaction)  # Implement ask_for_price to handle interaction

                await interaction.followup.send(f"Asset data: {asset_name} - Units: {units}, IPFS: {ipfs_hash}")
                total_price = price_per_unit * units
                await interaction.followup.send(f"The total listing price at {price_per_unit} per unit will be {total_price}. Confirm? [Yes/No]")

                try:
                    total_price = await after_price_set_and_user_confirms(ctx, asset_name, units, asset_balance,
                                                                          new_address, asset_data)
                    await save_listing_info("NFTRVN.json", asset_name, units, asset_balance, price_per_unit,
                                            new_address, ctx.author.display_name)
                    await update_or_create_listing_embed(ctx, bot)
                    await announce_new_listing(ctx, asset_name, new_address, ipfs_hash)
                    await interaction.followup.send(
                        "Listing confirmed and announced https://discord.com/channels/939095886993195048/1213694827305238528!")
                except TimeoutError as e:
                    print(e)  # or handle the timeout in some way
                    await interaction.followup.send("Listing cancelled.")
                return
                except TimeoutError as e:
                    print(e)  # or handle the timeout in some way
                    await interaction.followup.send("Listing cancelled.")
                return

            if i < 9:
                await interaction.followup.send(
                    f'No assets detected yet. Checking again in 1 minute. {9 - i} checks remaining.')
            await asyncio.sleep(60)

        await interaction.followup.send(
            'No assets detected after 10 minutes. Please check the transaction and try again.')

    # Start the checking process asynchronously to allow other operations
    asyncio.create_task(check_assets())
"""


"""async def update_or_create_listing_embed(interaction, bot):
    channel = bot.get_channel(1237637061855547463)  # Correct channel ID
    message_id = 1239351882309308417  # Update this as necessary

    listings = await load_listings()
    if not listings:
        await channel.send("No current listings available.")
        return

    embed = discord.Embed(title="NiftyDEX", description="Listings: (Sorted by Price)", color=0xFFFF00)
    for listing in listings:
        asset_name = listing['asset_name']
        encoded_asset_name = custom_url_encode(asset_name)

        # Link to trigger detailed info command
        asset_info_command = f"!assetinfo {encoded_asset_name}"

        embed.add_field(
            name=f"{asset_name} - {listing['asset_balance']} units",
            value=f"Price per unit: {listing['price_per_unit']} RVN\n"
                  f"Total Price: {listing['total_price']} RVN\n"
                  f"ATH Price: {listing.get('ath_price', 'N/A')} RVN\n"
                  f"ATL Price: {listing.get('atl_price', 'N/A')} RVN\n"
                  f"Listed By: {listing.get('NiftyRaven Member', 'N/A')}\n"
                  f"NiftyDEX address: {listing['listing_address']}\n"
                  f"MORE Details: Type `{asset_info_command}` for more info",
            inline=False
        )

    if message_id:
        message = await channel.fetch_message(message_id)
        await message.edit(embed=embed)
    else:
        await channel.send(embed=embed)
"""


#WORKING
"""
async def update_or_create_listing_embed(interaction, bot):
    channel = bot.get_channel(1237637061855547463)  # Correct channel ID
    message_id = 1239351882309308417  # Update this as necessary

    listings = await load_listings()
    if not listings:
        await channel.send("No current listings available.")
        return

    # Group listings by asset name
    grouped_listings = defaultdict(list)
    for listing in listings:
        grouped_listings[listing['asset_name']].append(listing)

    embed = discord.Embed(title="NiftyDEX", description="Listings: (Sorted by Price)", color=0xFFFF00)

    # Iterate over grouped listings
    for asset_name, grouped in grouped_listings.items():
        # Calculate the lowest price, ATH, ATL, and last sold price
        lowest_price = min(group['price_per_unit'] for group in grouped)
        ath_price = max(group.get('ath_price', 0) for group in grouped)
        atl_price = min(group.get('atl_price', float('inf')) for group in grouped)
        last_sold_price = grouped[-1]['price_per_unit']  # Assuming the last listing is the most recent sold

        # Create detailed info command
        encoded_asset_name = custom_url_encode(asset_name)
        asset_info_command = f"!assetinfo {encoded_asset_name}"

        embed.add_field(
            name=f"{asset_name} - {sum(group['asset_balance'] for group in grouped)} units",
            value=(
                f"Lowest Price: {lowest_price:.8f} RVN\n"
                f"Last Sold Price: {last_sold_price:.8f} RVN\n"
                f"ATH Price: {ath_price:.8f} RVN\n"
                f"ATL Price: {atl_price:.8f} RVN\n"
                f"Listed By: {grouped[-1].get('NiftyRaven Member', 'N/A')}\n"
                f"NiftyDEX Address: {grouped[-1]['listing_address']}\n"
                f"MORE Details: Type `{asset_info_command}` for more info"
            ),
            inline=False
        )

    # Update the existing message or send a new one
    if message_id:
        message = await channel.fetch_message(message_id)
        await message.edit(embed=embed)
    else:
        message = await channel.send(embed=embed)
"""


#load processed txids-temp
"""
def load_processed_txids():
    if not os.path.exists("processed_txids.txt"):
        with open("processed_txids.txt", "w") as f:
            pass

    with open("processed_txids.txt", "r") as f:
        return [txid.strip() for txid in f]
"""


############################################################################################################
# EXTRA FUNCTIONS END
############################################################################################################
