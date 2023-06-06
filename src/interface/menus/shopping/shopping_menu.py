"""
shopping_menu.py

Configure MarcoNeo's shopping page.
"""

#-------------------------------------------------------------------#

from src.interface.menu_templates.left_grid import LeftGrid
from src.interface.menu_templates.right_grid import RightGrid
from src.utils.gui_utils import Frame

#-------------------------------------------------------------------#


class ShoppingMenu(Frame):
    """
    Menu for the shopping page.
    """
    def __init__(self, gui=None) -> None:
        super().__init__(gui)
        self.gui = gui
        self.propagate(False)

        # Setup the left grid for the navbar
        self.left_grid = LeftGrid(self)
        self.left_grid.pack(side="left", fill="both", expand=True)

        # Setup the right grid for the header, body and footer
        self.right_grid = RightGrid(self)
        self.right_grid.pack(side="right", fill="both", expand=True)

        # Setup the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)
        self.rowconfigure(0, weight=1)

    def retrieve_shopping_items(self, toggle:str) -> list:
        """
        Retrieves the items to display.
        """
        items = self.gui.app.config['Shopping'][toggle]['items']
        return items
