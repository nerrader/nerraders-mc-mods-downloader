# v3.3.0 - 19-5-2026
* Added logging and made `verbose_mode` (originally `show_detailed_logs`) configuration functional.
* Added a style for the questionary menus to increase contrast for important elements.
* Improved the UX by making incompatible mods with the mod loader disabled.
* Made the manual path prompt a more modern directory window for a more user-friendly experience.
* Added the functionality to set the default directory path to None.
* Fixed the behavior settings not being able to be disabled.
* Fixed mods being corrupted or not being downloaded.
* Heavily refactored the main functions in main.py
* Improved documentation in the code in general.
* Made private functions in builder.py actually private.
* Modified the configuration menu to handle CTRL + C cancellation in their submenus.
# v3.2.0 - 13-5-2026
* Added a feature that filters the mods that are incompatible with your launcher in the main selection mods screen.
* Added Multi-OS Compatibility, this tool now allows Linux, MacOS and other OSes to download mods as well. However, the smart pathfind system only works on Windows so other OSes have to manually type in their filepaths to download mods.
* Added a new module to help with the development of this tool: `platformdirs`
* Added dependabot to help resolve project dependency security vulnerabilities.
* Removed the max_workers during download, allowing for further concurrency.
* Updated README information to go along with the latest changes in this version
* Fixed some minor bugs present in older versions
# v3.1.1 - 04-05-2026
* Polished the mc-mods-downloader.exe icon
# v3.1.0 - 04-05-2026
* Removed Bandit dev dependency
* Added compatibility for multiple OSes
* Added a placeholder icon for the .exe
* Made it a .zip folder to prevent security warnings
* Slightly polished code on all files
# v3.0.0 - 03-04-2026
* Huge code polishing and refactor, removed the need for global variables, put constants in constants.py, and so much more.
* Uses rich.live to improve and polish the progress bars during downloading.
* Polished the UX of getting the user's download folder path.
* Added a summary table for the failed/incompatible mods at the end.
* Added a MIT License
* Added bandit, radon and vulture dev dependencies to speed up the future development of this project.
* Now uses the hatchling build system for packaging.
# v2.0.0 - 26-03-2026
* Introduced multithreadding to significantly speed up the tools moddata fetching and downloading processes
* Added progress bars to visualize the progress during the downloading section.
* Changed library mods in mods.json to be a list of slugs, as it wasn't required to be in the main menu anymore.
* Slightly changed and improved documentation across main.py
# v1.2.0 - 23-03-2026
* Now uses persistent API Sessions to make this tool significantly faster by removing the need to do a TCP handshake at the beginning of each.
# v1.1.0 - 22-03-2026
* Added more mod and more mod categories
* Polished and cleaned up the overall code
* Added core features for the tool such as the main menu, settings/configs, initial fetching and downloading process of mods.
# v1.0.0 - 22-03-2026
* Added configuration settings and the core features of the tool.
* The initial release of the tool.
