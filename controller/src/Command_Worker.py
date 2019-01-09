import abc

from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot

from src.Defines import Command_Type


class QTWorker(QThread):
    sec_changed = pyqtSignal(str)
    _worker_list = []
    _command_list = []

    def __init__(self, sec=0, parent=None):
        super().__init__()
        self.main = parent
        self.working = True
        self.sec = sec

    def __del__(self):
        print(".... end thread.....")
        self.wait()

    def run(self):
        while self.working:
            try:
                for comm in self._command_list:
                    for work_list in self._worker_list:
                        cmd_type, args = comm
                        work_list.do_update(cmd_type, args)
                    self._command_list.remove(comm)

            except Exception as e:
                print(e)
                pass
            finally:
                self.sleep(0.05)

    @pyqtSlot()
    def add_list(self, v):
        self._worker_list.append(v)

    @pyqtSlot()
    def put(self, v):
        self._command_list.append(v)

class CommandObserver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def do_update(self, cmd: Command_Type, args: []):
        pass


class Command_Worker(object):
    __instance = None
    qt_worker = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance

    def init(self, parent):
        if self.qt_worker is None:
            self.qt_worker = QTWorker(parent)

    def start_worker(self):
        if self.qt_worker is not None:
            self.qt_worker.start()

    def add_worker(self, lst):
        self.qt_worker.add_list(lst)

    def put_command(self, cmd_type, args=None):
        cmd_obj = [cmd_type, args]
        self.qt_worker.put(cmd_obj)


CommandManager = Command_Worker.instance()