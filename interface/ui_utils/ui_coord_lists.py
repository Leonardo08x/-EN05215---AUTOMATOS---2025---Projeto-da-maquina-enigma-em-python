paper_pos = (300, 100)
paper_pos_saida = (300, 150)
BASE_ROTOR_COORD = (1127, 264)  # Coordenada base inicial (exemplo: para o primeiro rotor)
rotor_window_pos = [
        (BASE_ROTOR_COORD[0] - 7, BASE_ROTOR_COORD[1] - 95),
        (BASE_ROTOR_COORD[0] + 0, BASE_ROTOR_COORD[1] + 150),
        (BASE_ROTOR_COORD[0] + 9, BASE_ROTOR_COORD[1] + 392)
    ]
rotor_areas = [
        (rotor_window_pos[0][0] - 50, rotor_window_pos[0][1] - 50, rotor_window_pos[0][0] + 50, rotor_window_pos[0][1] + 50),
        (BASE_ROTOR_COORD[0] - 50, BASE_ROTOR_COORD[1] + 100, BASE_ROTOR_COORD[0] + 50, BASE_ROTOR_COORD[1] + 200),
        (rotor_window_pos[2][0] - 50, rotor_window_pos[2][1] - 50, rotor_window_pos[2][0] + 50, rotor_window_pos[2][1] + 50)
    ]

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
        ' ': (BASE_COORD[0] + 500, BASE_COORD[1] + 0),
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
