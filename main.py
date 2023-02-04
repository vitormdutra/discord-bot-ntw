import discord
from discord import app_commands


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.all())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=435263030113075200))
            self.synced = True
        print(f'We have logged in as {self.user}.')


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name="test", description="testing", guild=discord.Object(id=435263030113075200))
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(f'hello {name}! I was made with discord.py')

client.run('MTAyNjIzOTk1MzE2MTY4Mjk0NQ.G8QMtT.y1-RXvr2T2tW4Ug7hiTaKtYP9RkpmVZ2ZSGThs')

