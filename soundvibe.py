#SoundVibe
import discord
from discord.ext import commands
import urllib.parse, urllib.request, re
import config
TOKEN = 'NzEwNzY0MzYxMDg1MzU0MDI2.Xr5M7A.e0tUZAvAxr8wFLSoFb4KIsY0luY'

client = discord.Client()
class Bot(commands.AutoShardedBot):

    def __init__(self):
        super().__init__(command_prefix='.')
        self.add_command(self.yt)

    @commands.command()
    async def yt(ctx, *, search):
        
        query_string = urllib.parse.urlencode({
            'search_query': search
        })
        html_content = urllib.request.urlopen(
            'https://www.youtube.com/results?' + query_string
        )
        search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
        await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

    def run(self):
        super().run('NzEwNzY0MzYxMDg1MzU0MDI2.Xr5M7A.e0tUZAvAxr8wFLSoFb4KIsY0luY')
if __name__ == '__main__':
    bot = Bot()
    bot.run()
