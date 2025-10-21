from dotenv import load_dotenv
from bot.main import Bot
load_dotenv()
import asyncio
from application.scheduler import Scheduler
from application.types import Client

async def main():
    bot = Bot()
    scheduler = Scheduler(bot.handler)
    try:
        bot_task = asyncio.to_thread(bot.start)
        await asyncio.gather(scheduler.start(),bot_task)
    except KeyboardInterrupt:
        print('Operación cancelada.')
        scheduler._running_ = False
asyncio.run(main())