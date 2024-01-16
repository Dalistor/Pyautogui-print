from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["cv2", "pyautogui", "pynput"]
}

setup(
    name="FHC",
    version="1.0",
    description="Sistema para auxiliar na busca de confidência",
    options={"build_exe": build_exe_options},
    executables=[Executable("FHC.py")],
)