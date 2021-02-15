import discord

async def get(bot, payload):
            channel = bot.get_channel(payload.channel_id)
            message_id = payload.message_id
            message = await channel.fetch_message(message_id)
            message.
            user = payload.member
            emoji = payload.emoji
            return {'channel': channel, 'message': message, 'user': user, 'emoji': emoji}