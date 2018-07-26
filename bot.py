import json
import aiohttp

from discord.ext import commands
from pathlib import Path


class InspireBot(commands.Bot):
    def __init__(self, *args, **kwargs):

        with open('config.json') as f:
            self.config = json.load(f)

        self.startup_ext = [x.stem for x in Path('cogs').glob('*.py')]

        super().__init__(command_prefix=commands.when_mentioned, pm_help=None, *args, **kwargs)

        # Make room for the help command
        self.remove_command('help')

    def run(self):
        super().run(self.config['token'])

    async def on_message(self, message):
        ctx = await self.get_context(message)
        await self.invoke(ctx)

    async def on_ready(self):
        self.ses = aiohttp.ClientSession()
        for ext in self.startup_ext:
            try:
                self.load_extension(f'cogs.{ext}')
            except Exception as e:
                print(f'Failed to load extension: {ext}\n{e}')
            else:
                print(f'Loaded extension: {ext}')

        print(f'Client logged in.\n'
              f'{self.user.name}\n'
              f'{self.user.id}\n'
              '--------------------------')
