import tkinter as tk
from cpf_utils import gerar_numero_cpf, formatar_cpf


def iniciar_interface():
    janela = tk.Tk()
    janela.title('Gerador de CPF')
    janela.geometry('400x300')
    janela.configure(bg='#f0f0f0')

    # -------- FUNÇÕES DA UI -------- #

    def gerar_cpf():
        cpf = gerar_numero_cpf()
        texto = formatar_cpf(cpf)
        texto_cpf.config(text=texto)

    def gerar_varios_cpfs():
        lista = [formatar_cpf(gerar_numero_cpf()) for _ in range(10)]
        texto_cpf.config(text='\n'.join(lista))

    def copiar_cpf():
        cpf = texto_cpf.cget("text")
        if cpf:
            janela.clipboard_clear()
            janela.clipboard_append(cpf)

    # -------- COMPONENTES -------- #

    titulo = tk.Label(
        janela,
        text='Bem-vindo ao gerador de CPF',
        bg='#f0f0f0',
        font=('Arial', 14)
    )
    titulo.pack(pady=10)

    tk.Button(janela, text='Gerar CPF', command=gerar_cpf, width=20).pack(pady=5)
    tk.Button(janela, text='Gerar 10 CPFs', command=gerar_varios_cpfs, width=20).pack(pady=5)
    tk.Button(janela, text='Copiar CPF', command=copiar_cpf, width=20).pack(pady=5)

    texto_cpf = tk.Label(
        janela,
        text='',
        bg='#f0f0f0',
        font=('Arial', 16, 'bold'),
        fg='green',
        justify='center'
    )
    texto_cpf.pack(pady=20)

    janela.mainloop()