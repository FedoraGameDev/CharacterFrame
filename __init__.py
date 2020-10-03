# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from .Debug import Debug
from .ErrorHandling.ErrorHandler import ErrorHandler
from .DataManagement.SessionMemory import SessionMemory
from . import AutoLoad

bl_info = {
    "name": "Character Frame",
    "author": "Fedora Dev",
    "description": "Create characters from structural frames.",
    "blender": (2, 90, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Characters",
    "support": "COMMUNITY"
}


def Init() -> None:
    Debug.Init()
    SessionMemory.Init()
    AutoLoad.init()
    AutoLoad.register()


def register() -> None:
    ErrorHandler.Try(lambda: Init())


def unregister() -> None:
    ErrorHandler.Try(lambda: AutoLoad.unregister())
