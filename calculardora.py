# -*- coding: utf-8 -*-

import tkinter as tk
import customtkinter as ctk
import requests


class App:
    def __init__(self):
        # Criando janela
        self.root = tk.Tk()
        self.root.title("Calculadora Conversor")
        self.root.configure(background="gray")
        self.root.geometry("288x488")
        self.root.resizable(False, False)

        # Variáveis internas
        self.cotacao = None
        self.total = None

        # Criar interface
        self.criar_widgets()

        self.root.mainloop()

    def criar_widgets(self):

        # Título Dólar
        self.lb_dolar = ctk.CTkLabel(
            self.root,
            text="Valor Dólar",
            fg_color="white",
            text_color="gray",
            font=("Arial", 16, "bold"),
            width=150,
            height=40,
            corner_radius=15
        )
        self.lb_dolar.pack(pady=10)

        self.valor_dolar = tk.Entry(self.root, width=10)
        self.valor_dolar.pack(pady=5)

        self.label_dolar = tk.Label(
            self.root,
            text="Clique para ver a cotação",
            font=("Arial", 12)
        )
        self.label_dolar.pack(pady=10)

        self.botao_cotacao = ctk.CTkButton(
            self.root,
            text="Atualizar cotação",
            corner_radius=15,
            command=self.buscar_cotacao
        )
        self.botao_cotacao.pack()

        # Converter total
        self.label_calculo = tk.Label(
            self.root,
            text="Total Convertido em real",
            font=("Arial", 12)
        )
        self.label_calculo.pack(pady=10)

        self.botao_converter = ctk.CTkButton(
            self.root,
            text="Calcular em real",
            corner_radius=15,
            command=self.converter_real
        )
        self.botao_converter.pack()

        # Quantidade
        self.lb_quantidade = ctk.CTkLabel(
            self.root,
            text="Quantidade",
            fg_color="white",
            text_color="gray",
            font=("Arial", 16, "bold"),
            width=150,
            height=40,
            corner_radius=15
        )
        self.lb_quantidade.pack(pady=10)

        self.qt_numero = tk.Entry(self.root, width=10)
        self.qt_numero.pack(pady=5)

        self.label_quantidade = tk.Label(
            self.root,
            text="Valor por item",
            font=("Arial", 12)
        )
        self.label_quantidade.pack(pady=10)

        self.botao_dividir = ctk.CTkButton(
            self.root,
            text="Calcular",
            corner_radius=15,
            command=self.calcular_quantidade
        )
        self.botao_dividir.pack(pady=10)

    # ==============================
    # FUNÇÕES
    # ==============================

    def buscar_cotacao(self):
        try:
            resposta = requests.get(
                "https://economia.awesomeapi.com.br/last/USD-BRL"
            )
            dados = resposta.json()
            self.cotacao = float(dados['USDBRL']['bid'])

            self.label_dolar.config(
                text=f"O valor do dólar atual é: USD {self.cotacao:.2f}"
            )

        except Exception:
            self.label_dolar.config(
                text="Erro ao buscar cotação"
            )

    def converter_real(self):
        if self.cotacao is None:
            self.label_calculo.config(
                text="Atualize a cotação primeiro"
            )
            return

        try:
            valor = float(self.valor_dolar.get())
            self.total = valor * self.cotacao

            self.label_calculo.config(
                text=f"O valor TOTAL é: R$ {self.total:.2f}"
            )

        except ValueError:
            self.label_calculo.config(
                text="Digite um valor válido"
            )

    def calcular_quantidade(self):
        if self.total is None:
            self.label_quantidade.config(
                text="Calcule o total primeiro"
            )
            return

        try:
            quantidade = float(self.qt_numero.get())

            if quantidade == 0:
                self.label_quantidade.config(
                    text="Quantidade não pode ser zero"
                )
                return

            divisao = self.total / quantidade

            self.label_quantidade.config(
                text=f"O valor por item é: R$ {divisao:.2f}"
            )

        except ValueError:
            self.label_quantidade.config(
                text="Digite um número válido"
            )


# Executar aplicação
App()
