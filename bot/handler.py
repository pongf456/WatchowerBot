from types import CoroutineType
from typing import Any, Callable

from application.types import Client


class EventHandler(Client):
    def __init__(self, notifier: Callable[[str], CoroutineType[Any, Any, None]]):
        self.notifier = notifier
    def hell_started(self):
        return self.notifier(
            r"*🔥 Infierno Iniciado\!* ⏳ A farmear la fase en la próxima hora\. \[\/disable\]"
        )
    def pre_hell_finished(self):
        return self.notifier(
            r"*⏱️ ¡Infierno x5m\!* Última llamada para terminar la fase actual\. ¡Corre\! \[\/disable\]"
        )
    def hell_finished(self):
        return self.notifier(
            r"*✅ Infierno Finalizado\!* 😴 Tómate un respiro y prepárate para el siguiente\. \[\/disable\]"
        )
    def pre_hell_started(self):
        return self.notifier(
            r"*🚨 Infierno en 5 Minutos\!* Prepárate para iniciar la nueva fase a la hora en punto\. \[\/disable\]"
        )