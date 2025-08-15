from PIL import Image, ImageTk
import tkinter as tk

def interface():
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)
    # Painel de seleção vertical à esquerda
    mode_var = tk.StringVar(root)
    mode_var.set("Criptografar")  # Modo padrão
    modes = ["Criptografar", "Descriptografar", "Debug"]
    mode_panel = tk.OptionMenu(frame, mode_var, *modes)
    mode_panel.pack(side=tk.TOP, padx=10, pady=10)
    root.geometry("1366x768")
    canvas = tk.Canvas(root, width=1366, height=768)
    canvas.pack()
    image = Image.open(r"interface\assets\enigma prototype.png")
    image = image.resize((1366, 768), Image.LANCZOS)
    bg_image = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)
    root.bg_image = bg_image
    paper_text = ''
    paper_pos = (300, 100)
    paper_pos_saida = (300, 150)
    paper_id = canvas.create_text(paper_pos, text=paper_text, anchor=tk.NW, font=('Courier', 12))
    paper_id_saida = canvas.create_text(paper_pos_saida, text=paper_text, anchor=tk.NW, font=('Courier', 12))
    BASE_ROTOR_COORD = (1127, 264)  # Coordenada base inicial (exemplo: para o primeiro rotor)
    rotor_window_pos = [
        (BASE_ROTOR_COORD[0] - 7, BASE_ROTOR_COORD[1] - 95),
        (BASE_ROTOR_COORD[0] + 0, BASE_ROTOR_COORD[1] + 150),
        (BASE_ROTOR_COORD[0] + 9, BASE_ROTOR_COORD[1] + 392)
    ]
    rotor_letters = ['A', 'A', 'A']
    rotor_text_ids = []
    for i, pos in enumerate(rotor_window_pos):
        id = canvas.create_text(pos, text=rotor_letters[i], font=('Arial', 16), fill='black')
        rotor_text_ids.append(id)
    rotor_areas = [
        (rotor_window_pos[0][0] - 50, rotor_window_pos[0][1] - 50, rotor_window_pos[0][0] + 50, rotor_window_pos[0][1] + 50),
        (BASE_ROTOR_COORD[0] - 50, BASE_ROTOR_COORD[1] + 100, BASE_ROTOR_COORD[0] + 50, BASE_ROTOR_COORD[1] + 200),
        (rotor_window_pos[2][0] - 50, rotor_window_pos[2][1] - 50, rotor_window_pos[2][0] + 50, rotor_window_pos[2][1] + 50)
    ]
    selected_rotor = None
    selected_indicator = None
    BASE_COORD = (270, 570)  # Coordenada base inicial (exemplo: para 'Q')
    key_positions = {
        'Q': (BASE_COORD[0] + 0, BASE_COORD[1] + 0),
        'W': (BASE_COORD[0] + 50, BASE_COORD[1] + 0),
        'E': (BASE_COORD[0] + 100, BASE_COORD[1] + 0),
        'R': (BASE_COORD[0] + 150, BASE_COORD[1] + 0),
        'T': (BASE_COORD[0] + 200, BASE_COORD[1] + 0),
        'U': (BASE_COORD[0] + 250, BASE_COORD[1] + 0),
        'I': (BASE_COORD[0] + 300, BASE_COORD[1] + 0),
        'O': (BASE_COORD[0] + 350, BASE_COORD[1] + 0),
        'Y': (BASE_COORD[0] + 400, BASE_COORD[1] + 0),
        'P': (BASE_COORD[0] + 450, BASE_COORD[1] + 0),
        'A': (BASE_COORD[0] + 0, BASE_COORD[1] + 50),
        'S': (BASE_COORD[0] + 50, BASE_COORD[1] + 50),
        'D': (BASE_COORD[0] + 100, BASE_COORD[1] + 50),
        'F': (BASE_COORD[0] + 150, BASE_COORD[1] + 50),
        'G': (BASE_COORD[0] + 200, BASE_COORD[1] + 50),
        'H': (BASE_COORD[0] + 250, BASE_COORD[1] + 50),
        'J': (BASE_COORD[0] + 300, BASE_COORD[1] + 50),
        'K': (BASE_COORD[0] + 350, BASE_COORD[1] + 50),
        'L': (BASE_COORD[0] + 400, BASE_COORD[1] + 50),
        'Z': (BASE_COORD[0] + 10, BASE_COORD[1] + 100),
        'X': (BASE_COORD[0] + 60, BASE_COORD[1] + 100),
        'C': (BASE_COORD[0] + 110, BASE_COORD[1] + 100),
        'V': (BASE_COORD[0] + 160, BASE_COORD[1] + 100),
        'B': (BASE_COORD[0] + 210, BASE_COORD[1] + 100),
        'N': (BASE_COORD[0] + 260, BASE_COORD[1] + 100),
        'M': (BASE_COORD[0] + 310, BASE_COORD[1] + 100),
    }
    def update_paper(char):
        nonlocal paper_text
        paper_text += char.upper()
        if len(paper_text) > 20:
            paper_text = paper_text[-20:]
        canvas.itemconfig(paper_id, text=paper_text)
        canvas.itemconfig(paper_id_saida, text=paper_text)
        print(f"Modo selecionado: {mode_var.get()}")
        print(f"Rotores: {rotor_letters}")
        print(f"Rotores: {rotor_letters[0]}{rotor_letters[1]}{rotor_letters[2]}")
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
        nonlocal selected_rotor, selected_indicator
        if selected_rotor is not None and event.char.isalpha():
            letter = event.char.upper()
            rotor_letters[selected_rotor] = letter
            canvas.itemconfig(rotor_text_ids[selected_rotor], text=letter)
            canvas.delete(selected_indicator)
            selected_indicator = None
            selected_rotor = None
    root.bind("<Key>", on_key_press)
    root.mainloop()

interface()