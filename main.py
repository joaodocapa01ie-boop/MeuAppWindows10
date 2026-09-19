import tkinter as tk

janela = tk.Tk()
janela.title("Win App")
janela.geometry("420x300")
janela.resizable(False, False)

titulo = tk.Label(
    janela,
    text="WIN APP",
    font=("Arial", 24, "bold")
)
titulo.pack(pady=25)

tk.Label(
    janela,
    text="ID ou endereço do seu PC:"
).pack()

entrada = tk.Entry(janela, width=35)
entrada.pack(pady=10)

status = tk.Label(
    janela,
    text="Status: Desconectado"
)
status.pack(pady=10)

def conectar():
    if entrada.get().strip():
        status.config(text="Status: Pronto para conectar")
    else:
        status.config(text="Digite o ID/endereço")

botao = tk.Button(
    janela,
    text="CONECTAR",
    command=conectar,
    width=20
)
botao.pack(pady=15)

janela.mainloop()
