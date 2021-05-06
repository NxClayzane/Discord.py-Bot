import discord
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix='!S.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.status.online, activity=discord.Game('Help-!S'))
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('succesfull')

@client.command()
    async def _8ball(ctx, *, question):
        responses = ['its not right,baba boy!1',
                     'wow , it matched',
                     'no',
                     'yes',
                     'u gooses , u r a noob',
                     'ask the same later',
                     'i am programmed to say the truth,not lies',
                     'sry, i did not get u',
                     'go get a life', ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')

@commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

client.run('')
