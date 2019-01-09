from ui.mainwindow import Main_Window
from src.Command_Worker import CommandObserver, CommandManager
from src.Defines.Command_Type import Command_Type


class Main_Window_Worker(CommandObserver):

    def __init__(self, control_view: Main_Window):
        self.Control_View = control_view
        CommandManager.add_worker(self)

    def do_update(self, cmd: Command_Type, args: []):
        if cmd == Command_Type.CMD_OPEN_UI:
            if self.Control_View.ui_config.isVisible() == False:
                self.Control_View.content_frame.setVisible(True)
                self.Control_View.ui_config.setVisible(True)
        elif cmd == Command_Type.CMD_CLOSE_UI:
            print('Command_Type.CMD_CLOSE_UI')
