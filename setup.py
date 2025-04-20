from cx_Freeze import setup, Executable

setup(
    name="Numeros Loteria",
    version="1.0.0",
    description="github.com/Filipi565",
    executables=[Executable("main.py", base="gui", icon="icon.ico")],
)