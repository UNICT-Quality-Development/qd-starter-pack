import asyncio
import yaml
from yaml.loader import SafeLoader
from pyrogram import Client
from pyrogram.raw import functions

with open('../config/config.yaml' , 'r' , encoding='UTF-8') as file:
    data = yaml.load(file, Loader = SafeLoader)


async def main(api_id, api_hash, username, phone_number):
    """Main function"""
    async with Client(username, api_id=api_id, api_hash=api_hash, phone_number=phone_number) as app:
        await app.invoke(query = functions.account.UpdateProfile(about="try"))

if __name__ == "__main__":
    asyncio.run(main(data['api_id'] , data['api_hash'] , data['username_account'], data['phone_number']))
