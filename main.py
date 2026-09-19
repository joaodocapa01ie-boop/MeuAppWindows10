import tkinter as tk

janela = tk.Tk()
janela.title("Meu App Windows")
janela.geometry("400x250")

texto = tk.Label(
    janela,
    text="Meu primeiro aplicativo!",
    font=("Arial", 18)
)
texto.pack(pady=80)

janela.mainloop()
