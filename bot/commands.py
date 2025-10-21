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
            "*👋 ¡Hola\! Soy Watchtower Bot\!* \n"
            "Tu vigilante de gremio para Lords Mobile\.\n\n"
            "Mi misión es enviarte alertas de *Infierno* y otros eventos sin que tengas que mirar el juego\. \n\n"
            "Para empezar a recibir notificaciones \(incluyendo el aviso \), usa el comando:\n"
            "➡️ \/enable \n\n"
            "Para silenciarme:\n"
            "➡️ \/disable"
        )
        if not update.message:
            return
        await update.message.reply_markdown_v2(response)
    async def enable(self,update:Update,ctx:ContextTypes.DEFAULT_TYPE):
        response = (
        "*🔔 Notificaciones Activadas 🔔* \n"
        "🤖 El bot **Watchtower** ha iniciado su vigilancia\. \n"
        "Estás recibiendo:"
        "\• Alertas de **Infierno** \(de cada hora\)\. \n"
        "\• Avisos de **Reunión** de Gremio\. \n"
        "Para silenciarme, usa el comando \/disable \n"
        )
        if update.message and not update.message.chat_id in self.clients:
            self.clients.append(update.message.chat_id)
        if not update.message:
            return
        await update.message.reply_markdown_v2(response)
    async def disable(self,update:Update,ctx:ContextTypes.DEFAULT_TYPE):
        response = (
        "*🔔 Notificaciones Desactivadas 🔔* \n"
        "🤖 El bot **Watchtower** ha detenido su vigilancia\. \n"
        )
        if update.message and update.message.chat_id in self.clients:
            self.clients.remove(update.message.chat_id)
        if not update.message:
            return
        await update.message.reply_markdown_v2(response)
        
    async def notify(self,message:str):
        tasks = []
        for client in self.clients:
            try:
                task = self.bot.sendMessage(client,message,)
                tasks.append(task)
            except:
                print('Ocurrió un error al enviar el mensaje')
        await asyncio.gather(*tasks)