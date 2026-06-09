import random, discord
from discord.ext import commands
uni_list = ["meow", "mewo", "mrrow", "purr", "uni", "kitty", "cat", "moew", "nya", "bugbug", "bug bug"]
reply_list = ["mrrow~ :3", "\*rolls over*"]
reaction_list = ["🐱","😹","😽","😾","🙀","😸","😺","😼","😿","🐈","🐈‍⬛"]
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Uni(bot=bot))

class Uni(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        responded = False
        msg = message.content
        if message.author.bot:
            return
        if message.channel.id == 1510779795494146232:
            await message.reply(random.choice(reply_list))
            await message.add_reaction(random.choice(reaction_list))
            responded = True
        if not any(uni in msg.lower() for uni in uni_list):
            return
        if not responded:
            await message.add_reaction(random.choice(reaction_list))
        if random.randint(1,100) == 100 and not responded:
            await message.reply(random.choice(reply_list))