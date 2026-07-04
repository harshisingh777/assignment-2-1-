import threading
class DatabaseConnection:
    _instance=None; _lock=threading.Lock()
    def __init__(self): self.conn='Shared'
    @classmethod
    def get_connection(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None: cls._instance=DatabaseConnection()
        return cls._instance
if __name__=='__main__':
 a=DatabaseConnection.get_connection(); b=DatabaseConnection.get_connection(); print(a is b)
