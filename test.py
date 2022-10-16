import discord


class Session:
    def __init__(self, author, channel):
        self.author = author
        self.channel = channel

    def get_author_id(self):
        return self.author.id


class SessionTest(discord.Client):

    def __init__(self, **options):
        self.sessions = list()
        super().__init__(**options)

    async def on_ready(self):
        print('Bot ready.')

    async def on_message(self, message):
        if "!ses" in message.content:
            if any(s.get_author_id() == message.author.id for s in self.sessions):
                await message.channel.send("Session already exists.")
            else:
                session = Session(message.author, message.channel)
                msg = format("Session created for %s" % message.author.name)
                await message.channel.send(msg)
                self.sessions.append(session)
        elif "!dos" in message.content:
            ses = next((s for s in self.sessions if s.get_author_id() == message.author.id), None)
            if ses is not None:
                msg = format("Done something for %s" % message.author.name)
                await message.channel.send(msg)
            else:
                await message.channel.send("You don't have a session yet.")


client = SessionTest(intents="G")
client.run("", bot=True)