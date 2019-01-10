from src.Command_Worker import CommandObserver, CommandManager
from src.Defines.Command_Type import Command_Type
from ui.main_config import Main_Config


class Main_Config_Worker(CommandObserver):

    def __init__(self, control_view: Main_Config):
        self.Control_View = control_view
        CommandManager.add_worker(self)

    def do_update(self, cmd: Command_Type, args: []):

        try:
            if cmd == Command_Type.CMD_CLOSE_UI_CONFIG:
                if self.Control_View.ui_config.isVisible() == True:
                    self.Control_View.content_frame.setVisible(False)
                    self.Control_View.ui_config.setVisible(False)
        except Exception as e:
            print(e)
