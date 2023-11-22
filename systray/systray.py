"""
pyCube:
    A program to insult you.

    Copyright (C) 2023 serverlinkdev@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>
"""


import logging
import threading
import time
import winsound

import pystray
from PIL import Image
from pystray import MenuItem as item

from mediator import BaseComponent


class Systray(BaseComponent):
    """
    A class using the Mediator design pattern.

    User's of this class should only:
    - Instantiate
    - Set mediator
    - Call in to this class using 'notify' method.
    """

    _app_icon = None
    _app_name = None
    _image = None
    mediator = None
    _menu = None
    _path_wav_1 = None
    _path_wav_2 = None
    _systray = None

    def __init__(self, app_icon, app_name, path_wav_1, path_wav_2):
        """
        Args:
        app_icon (str): the icon you want to see in your desktop OS
        app_name (str): the name of the app you want to see in OS notification's
        """
        super().__init__()

        # by default, PIL is chatty.
        logging.getLogger('PIL').setLevel(logging.WARNING)

        self._app_icon = app_icon
        self._app_name = app_name
        self._path_wav_1 = path_wav_1
        self._path_wav_2 = path_wav_2

        self._create_tray()

    def notify(self, sender, event):
        if sender == "ConcreteMediator":
            if event == "START":
                # start the systray thread and put the icon in user's OS tray
                self._lulz()
                self._start_systray()
                self._run_systray()

    def _blame_cube(self):
        """
        Plays a sound file using the Windows API every 10 minutes.
        """
        while True:
            winsound.PlaySound(self._path_wav_1, winsound.SND_FILENAME)
            time.sleep(600)

    def _create_tray(self):
        """
        Build the Systray
        """
        self._image = Image.open(self._app_icon)
        self._menu = (item('Quit', self._quit),)
        self._systray = pystray.Icon("name",
                                     self._image,
                                     self._app_name,
                                     self._menu)

    def _lulz(self):
        """
        Plays a sound file using the Windows API
        """
        winsound.PlaySound(self._path_wav_2, winsound.SND_FILENAME)

    def _quit(self):
        """
        Tell's ConcreteMediator that we need to quit the MainWindow.
        Stop's the Systray from running.
        """
        self._lulz()
        self._systray.visible = False
        self._systray.stop()
        logging.info("!cubelul")

    def _run_systray(self):
        """
        Runs the Systray continuously.
        """
        self._systray.run()

    def _start_systray(self):
        """
        Create a thread to run the Systray in
        """
        thread = threading.Thread(
            daemon=True,
            target=self._blame_cube
        )
        thread.start()
