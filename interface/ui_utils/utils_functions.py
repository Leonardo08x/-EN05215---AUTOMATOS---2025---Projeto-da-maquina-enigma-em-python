import tkinter as tk
import modulos.modulo_de_transições as transicoes

def show_debug_modal(root, chave):
    modal = tk.Toplevel(root)
    modal.title("Modo Debug Ativado")
    modal.geometry("400x600")
    
    # Centraliza o modal na tela
    modal.update_idletasks()
    width = modal.winfo_width()
    height = modal.winfo_height()
    x = (modal.winfo_screenwidth() // 2) - (width // 2)
    y = (modal.winfo_screenheight() // 2) - (height // 2)
    modal.geometry(f'{width}x{height}+{x}+{y}')

    # Label principal com o texto "Produção de..."
    label_producao = tk.Label(
        modal, 
        text=f"Produção de {chave}", 
        wraplength=180, 
        font=('Courier', 12, 'bold')
    )
    label_producao.pack(pady=10)

    # Obter produções
    producoes = transicoes.transicoes(chave, "Debug")
    itens = [f"{k} -> {v}" for k, v in producoes.items()]

    # Espaço em branco para o texto da transição
    espaco_texto = tk.Canvas(
        modal, 
        bg='white', 
        width=380, 
        height=450, 
        highlightthickness=1, 
        highlightbackground="black"
    )
    espaco_texto.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    # Coordenadas para colunas
    col_width = 180  # largura de cada coluna
    x_pos_col1 = 10
    x_pos_col2 = col_width + 20  # espaço entre colunas
    y_pos_col1 = 10
    y_pos_col2 = 10

    # Divide em duas metades
    metade = (len(itens) + 1) // 2
    primeira_coluna = itens[:metade]
    segunda_coluna = itens[metade:]

    # Desenha primeira coluna
    for linha in primeira_coluna:
        espaco_texto.create_text(
            x_pos_col1, 
            y_pos_col1, 
            anchor=tk.NW, 
            text=linha, 
            font=('Courier', 10)
        )
        y_pos_col1 += 15  # espaçamento vertical

    # Desenha segunda coluna
    for linha in segunda_coluna:
        espaco_texto.create_text(
            x_pos_col2, 
            y_pos_col2, 
            anchor=tk.NW, 
            text=linha, 
            font=('Courier', 10)
        )
        y_pos_col2 += 15

    # Botão OK
    ok_button = tk.Button(modal, text="OK", command=modal.destroy)
    ok_button.pack(pady=5)

    modal.transient(root)
    modal.grab_set()
    root.wait_window(modal)
