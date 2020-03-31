import os
from dotenv import load_dotenv
load_dotenv()


def get_token():
    """
    Discord token
    """
    return os.getenv('DISCORD_TOKEN')


def get_app_id():
    """
    Wolfram app id
    """
    return os.getenv('WOLFRAM_APP_ID')
