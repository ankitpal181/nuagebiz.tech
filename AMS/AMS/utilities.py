import base64

def encrypt_data(data: str) -> str:
    return base64.b64encode(data.encode("UTF-8"))


class Logger:
    def __init__(self, app: str = "", module: str = "") -> None:
        self.app = app
        self.module = module
    
    def log(self, time: str, msg: str) -> None:
        with open("error_logs.txt", "a+") as file:
            file.write("{} {}:{} {}\n".format(time, self.app, self.module, msg))
