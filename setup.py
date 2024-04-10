from setuptools import setup
import sys
import os

# Verifique se estamos em um ambiente Windows e use o executável correto do PyInstaller
if sys.platform.startswith('win'):
    exe_file = 'hamgnarok.exe'
else:
    exe_file = 'hamgnarok'

# Define os arquivos que devem ser incluídos no pacote final
additional_files = [
    ('modelos', ['modelos/Fase 1.jpg', 'modelos/Fase 2.jpg', 'modelos/Fase 3.jpg']),
    ('player', ['player/Fase 1 - Clique Para Pescar.png', 'player/Fase 2 - Toque para Recolher.png', 'player/Fase 3 - Captura de Peixe.png', 'player/Fase 4 - Standby.png']),
    ('', ['icone.ico'])  # Inclua o ícone da aplicação
]

# Configuração do setup
setup(
    name='Hamgnarok',
    version='1.0',
    description='Descrição da sua aplicação',
    options={
        'build_exe': {
            'packages': ['cv2', 'numpy', 'pyautogui', 'tkinter', 'PIL'],
            'include_files': additional_files
        }
    }
)
