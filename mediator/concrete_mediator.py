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


from mediator import Mediator
from systray import Systray


class ConcreteMediator(Mediator):
    """
    A class which implements the Mediator pattern.

    User's of this class should only:
    - Instantiate
    - Set mediator
    - Call in to this class using 'notify' method.
    """

    _app_icon = None
    _app_name = None
    _path_wav_1 = None
    _path_wav_2 = None
    _systray = None

    def __init__(self, app_icon, app_name, path_wav_1, path_wav_2):
        """
        Args:
        app_icon (str): the icon you want to see in your desktop OS
        app_name (str): the name of the app you want to see in OS notification's
        path_wav_1 (str): the path to the wav file
        path_wav_2 (str): the path to the wav file
        """
        super().__init__()
        self._app_icon = app_icon
        self._app_name = app_name
        self._path_wav_1 = path_wav_1
        self._path_wav_2 = path_wav_2

    def notify(self, sender, event):
        if sender == "Main":
            if event == "START":
                self._start_systray()

    def _start_systray(self):
        """
        Starts the Systray class.
        """
        self._systray = Systray(self._app_icon, self._app_name,
                                self._path_wav_1, self._path_wav_2)
        self._systray.mediator = self
        self._systray.notify("ConcreteMediator", "START")
