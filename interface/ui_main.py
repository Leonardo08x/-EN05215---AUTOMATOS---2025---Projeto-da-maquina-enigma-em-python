from PIL import Image, ImageTk
import tkinter as tk
from .ui_utils.ui_coord_lists import *
from modulos.modulo_de_computação import computação
from .ui_utils.utils_functions import show_debug_modal

def interface():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)
    def on_mode_change(*args):
        if mode_var.get() == "Debug":
            show_debug_modal(root,f"{rotor_letters[0]}{rotor_letters[1]}{rotor_letters[2]}")
            mode_var.set("Criptografar")

    # Painel de seleção vertical à esquerda
    mode_var = tk.StringVar(root)
    mode_var.set("Criptografar")  # Modo padrão
    mode_panel = tk.OptionMenu(frame, mode_var, *modes)
    mode_var.trace("w", on_mode_change)
    mode_panel.pack(side=tk.RIGHT, padx=10, pady=10)
    root.geometry("1366x768")
    canvas = tk.Canvas(root, width=1366, height=768)
    canvas.pack()
    image = Image.open(r"interface\assets\enigma prototype.png")
    image = image.resize((1366, 768), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)
    root.bg_image = bg_image
    paper_text = ''
    paper_text_saida = ''
    paper_id = canvas.create_text(paper_pos, text=paper_text, anchor=tk.NW, font=('Courier', 12))
    paper_id_saida = canvas.create_text(paper_pos_saida, text=paper_text, anchor=tk.NW, font=('Courier', 12))
    rotor_letters = ['A', 'A', 'A']
    rotor_text_ids = []
    for i, pos in enumerate(rotor_window_pos):
        id = canvas.create_text(pos, text=rotor_letters[i], font=('Arial', 16), fill='black')
        rotor_text_ids.append(id)
  
    selected_rotor = None
    selected_indicator = None
    # Variável para rastrear o estado
    toggle_case = tk.BooleanVar()
    toggle_case.set(False)  # False = maiúsculo, True = minúsculo

    # Função para alternar o nome da lista e o texto do botão
    def toggle_key_case():
        global key_positions
        from .ui_utils.ui_coord_lists import key_positions as original
        if toggle_case.get():
            key_positions = original  # Volta para maiúsculo
            toggle_case_button.config(text="Caps lock ativado")  # Reverte o texto
            toggle_case.set(False)
        else:
            key_positions = {k.lower(): v for k, v in original.items()}  # Muda para minúsculo
            toggle_case_button.config(text="Caps lock desativado")  # Altera o texto
            toggle_case.set(True)

    # Botão para alternar, alinhado com mode_panel
    toggle_case_button = tk.Button(frame, text="Caps lock ativado", command=toggle_key_case)
    toggle_case_button.pack(side=tk.LEFT, padx=10, pady=10)
    def update_paper(char):
        nonlocal paper_text, paper_text_saida
        paper_text += char
        if len(paper_text) > 20:
            paper_text = paper_text[-20:]
        if len(paper_text_saida) > 20:
            paper_text_saida = paper_text_saida[-20:]
        canvas.itemconfig(paper_id, text=paper_text)
        paper_text_saida += computação(f"{rotor_letters[0]}{rotor_letters[1]}{rotor_letters[2]}",char,f"{mode_var.get()}")
        canvas.itemconfig(paper_id_saida, text=paper_text_saida)
        #debug
        print(f"Modo selecionado: {mode_var.get()}")
        print(f"Rotores: {rotor_letters}")
        print(f"Rotores: {rotor_letters[0]}{rotor_letters[1]}{rotor_letters[2]}")
        print(f"char:{char}")
    def on_click(event):
        nonlocal selected_rotor, selected_indicator
        for i, area in enumerate(rotor_areas):
            if area[0] < event.x < area[2] and area[1] < event.y < area[3]:
                if selected_indicator:
                    canvas.delete(selected_indicator)
                selected_indicator = canvas.create_rectangle(area, outline='red', width=2)
                selected_rotor = i
                return
        for letter, (x, y) in key_positions.items():
            if abs(event.x - x) < 20 and abs(event.y - y) < 20:
                update_paper(letter)
                return
    canvas.bind("<Button-1>", on_click)
    def on_key_press(event):
        nonlocal selected_rotor, selected_indicator, paper_text_saida, paper_text
        if selected_rotor is not None and event.char.isalpha():
            letter = event.char.upper()
            rotor_letters[selected_rotor] = letter
            canvas.itemconfig(rotor_text_ids[selected_rotor], text=letter)
            canvas.delete(selected_indicator)
            selected_indicator = None
            selected_rotor = None
            paper_text = ''
            paper_text_saida = ''
            canvas.itemconfig(paper_id, text=paper_text)
            canvas.itemconfig(paper_id_saida, text=paper_text_saida)
    root.bind("<Key>", on_key_press)
    root.mainloop()
