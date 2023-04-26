import discord
from discord.ext import commands

config = {
    'token': 'your-token',
    'prefix': '$',
}

bot = commands.Bot(command_prefix=config['prefix'])

@bot.command()
async def kick(ctx, user : discord.User(), *arg, reason='Причина не указана'):
    await bot.kick(user)
    await ctx.send('Пользователь {user.name} был изгнан по причине "{reason}"')

bot.run(config['token'])
