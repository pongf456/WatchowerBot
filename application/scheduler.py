import asyncio
from application.types import Client
import schedule
import time
class Scheduler:
    def __init__(self, some_client:Client):
        self.client = some_client
        self._running_ = True
        schedule.every().hour.at(":50").do(self.__create_task__,self.client.pre_hell_finished)
        schedule.every().hour.at(":55").do(self.__create_task__,self.client.hell_finished)
        schedule.every().hour.at(":55").do(self.__create_task__,self.client.pre_hell_started)
        schedule.every().hour.do(self.__create_task__,self.client.hell_started)

    def __create_task__(self,fn):
        if not self._main_loop_:
            return
        return asyncio.run_coroutine_threadsafe(fn(),self._main_loop_)
    def _schedule_bucle_(self):
        print('Started scheduler task.')
        while self._running_:
            schedule.run_pending()
            time.sleep(1)
    async def start (self):
        self._main_loop_ = asyncio.get_event_loop()
        await asyncio.to_thread(self._schedule_bucle_)
    