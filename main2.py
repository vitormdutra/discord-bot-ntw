import discord
from discord.ext import commands
import os

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='/')

#remove the default help command so that we can write out own
bot.remove_command('help')

#register the class with the bot
#bot.add_cog(help_cog(bot))
bot.add_cog(music_cog(bot))

#start the bot with our token
bot.run("MTAyNjIzOTk1MzE2MTY4Mjk0NQ.G8QMtT.y1-RXvr2T2tW4Ug7hiTaKtYP9RkpmVZ2ZSGThs")
music_cog.dc