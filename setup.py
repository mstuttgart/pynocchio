from distutils.core import setup
from cx_Freeze import setup, Executable
exe = Executable(
    script="main.py",
    #base="Win32GUI", # Retirar comentario se for contruir um executavel para windows
    )
setup(
    name='pynocchio-comic-reader',
    version='1.0.0',
    # packages=['src'],
    url='http://mstuttgart.github.io/pynocchio-comic-reader/',
    license='GPLv3',
    author='Michell Stuttgart',
    description='Pynocchio is a image viewer specialized in manga/comic '
                'reading',
    # Devemos adicionar os .py que nao sao chamados explicitamente em nosso codigo
    options={"build_exe": {"includes": ["atexit", "color_button",
                                        "main_window_rc", "viewer"]}},
    executables=[exe],
)
