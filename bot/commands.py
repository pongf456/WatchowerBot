import asyncio
from urllib import response
from telegram import Bot, Update
from telegram.ext import ContextTypes

class CommandHandler:
    def __init__(self,bot:Bot) -> None:
        self.clients: list[int] = []
        self.bot = bot
    async def start(self,update:Update,ctx:ContextTypes.DEFAULT_TYPE):
        response = (
        "<b>👋 ¡Hola! Soy Watchtower Bot!</b> \n"
        "Mi misión es enviarte alertas de <i>Infierno</i> prueba /enable para activar las notificaciones y /disable para desactivarlas"
        )
        if not update.message:
            return
        await update.message.reply_html(response)
    async def enable(self,update:Update,ctx:ContextTypes.DEFAULT_TYPE):
        response = (
                    "<b>🔔 Notificaciones Activadas 🔔</b> \n"
                    "🤖 El bot <b>Watchtower</b> ha iniciado su vigilancia. \n"
                    "Estás recibiendo:"
                    "\n&#8226; Alertas de <b>Infierno</b> (de cada hora). \n"
                    "&#8226; Avisos de <b>Reunión</b> de Gremio. \n"
                    "Para silenciarme, usa el comando \n /disable \n"
                )
        if update.message and not update.message.chat_id in self.clients:
            self.clients.append(update.message.chat_id)
        if not update.message:
            return
        await update.message.reply_html(response)
    async def disable(self,update:Update,ctx:ContextTypes.DEFAULT_TYPE):
        response = (
                    "<b>🔕 Notificaciones Desactivadas 🔕</b> \n"
                    "🤖 El bot <b>Watchtower</b> ha detenido su vigilancia. \n"
                    "Para volver a activarlas, usa el comando /enable."
                )
        if update.message and update.message.chat_id in self.clients:
            self.clients.remove(update.message.chat_id)
        if not update.message:
            return
        await update.message.reply_html(response)
        
    async def notify(self,message:str):
        tasks = []
        for client in self.clients:
            try:
                task = self.bot.sendMessage(client,message,)
                tasks.append(task)
            except:
                print('Ocurrió un error al enviar el mensaje')
        await asyncio.gather(*tasks)