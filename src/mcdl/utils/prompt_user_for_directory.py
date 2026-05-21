from pathlib import Path
from tkinter import filedialog
import tkinter as tk

from mcdl import constants as const


def prompt_user_for_directory(
    prompt: str = "Select Default Mods Folder",
    mods_directory: Path = const.HOME_FILEPATH,
) -> Path | None:

    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Only apply the 'topmost' focus hack on Windows/Mac to prevent Linux window manager warnings
    if const.USER_OS in ("win32", "darwin"):
        try:
            root.wm_attributes("-topmost", True)
        except tk.TclError:
            pass

    selected_folder_path = filedialog.askdirectory(
        title=prompt, initialdir=mods_directory
    )

    root.destroy()

    return Path(selected_folder_path) if selected_folder_path else None
