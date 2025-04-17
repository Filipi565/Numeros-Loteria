from collections.abc import Callable
from urllib.error import HTTPError
from threading import Thread
from urllib import request
from tkinter import ttk
import tkinter as tk
from utils import *
import json
import time

def _get_games():
    url = request.Request("https://loteriascaixa-api.herokuapp.com/api", method="GET")
    try:
        with request.urlopen(url) as f:
            data = f.read()
    except HTTPError as e:
        return f"Erro ao conectar à loteria. Código de erro: {e.code}"
    
    return list[str](eval(data))

class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self, className="com.github.Filipi")
        self.geometry("600x400")
        self.title("Números da Loteria")
        self.resizable(False, False)

        self.calculate: Callable[[Window, tk.Event], None] = lambda *args: None
        self.concurso = tk.StringVar(self)
        self.numbers = tk.StringVar(self)
        self.output = tk.StringVar(self)
        self.game = tk.StringVar(self)
    
    def load_widgets(self):
        games = _get_games()
        if (isinstance(games, str)):
            label = ttk.Label(self, text=games)
            label.place(rely=.5, relx=.5, anchor=tk.CENTER)
            return

        label_jogo = ttk.Label(self, text="Selecionar a Modalidade:")
        label_jogo.place(relx=.5, rely=.13, anchor=tk.CENTER)

        menu = ttk.OptionMenu(self, self.game, games[0], *games)
        menu.place(relx=.5, rely=.2, anchor=tk.CENTER, relheight=.07)

        label_concurso = ttk.Label(self, text="Digite o Concurso:")
        label_concurso.place(relx=.5, rely=.33, anchor=tk.CENTER)

        concurso = ttk.Entry(self, textvariable=self.concurso)
        concurso.place(relx=.5, rely=.4, anchor=tk.CENTER, relwidth=.8)

        label_numeros = ttk.Label(self, text="Digite seus números separado por vírgula. Ex.: 01, 02, 15, 20, 30")
        label_numeros.place(relx=.5, rely=.53, anchor=tk.CENTER)

        numbers = ttk.Entry(self, textvariable=self.numbers)
        numbers.place(relx=.5, rely=.6, anchor=tk.CENTER, relwidth=.8)

        button = ttk.Button(self, text="Calcular Acertos", command=self._calculate)
        button.place(relx=.5, rely=.8, anchor=tk.CENTER)

        output = ttk.Label(self, textvariable=self.output)
        output.place(relx=.5, rely=.9, anchor=tk.CENTER)
    
    def _calculate(self, *args):
        self.calculate(self, *args)

def calcular_acertos(self: Window):
    dezenas_str = self.numbers.get()
    concurso = self.concurso.get()
    modalidade = self.game.get()

    if not dezenas_str:
        self.output.set("Por Favor digite os números das dezenas")
        return
    
    if not concurso:
        self.output.set("Por Favor digite o número do concurso")
        return
    
    dezenas = parse_numbers(dezenas_str, self.output.set)

    if not dezenas:
        return
    
    url = f"https://loteriascaixa-api.herokuapp.com/api/{modalidade}/{concurso}"
    try:
        with request.urlopen(url) as f:
            data_b: bytes = f.read()
    except HTTPError as e:
        self.output.set(f"Erro ao conectar à loteria. Código de erro: {e.code}")
        return

    if not data_b:
        self.output.set("Concurso Inválido. Por Favor insira um concurso válido")
        return
    
    data = json.loads(data_b)
    resultado_dezenas = (int(obj) for obj in data["dezenas"])

    acertos = get_rights(dezenas, resultado_dezenas)

    self.output.set("Você teve %d %s" % (acertos, "acerto" if acertos == 1 else "acertos"))

    def _clean():
        time.sleep(3)
        self.output.set("")

    t = Thread(target=_clean)
    t.start()

def main():
    window = Window()
    window.calculate = calcular_acertos

    t = Thread(target=window.load_widgets)
    t.start()

    window.mainloop()

if __name__ == "__main__":
    main()