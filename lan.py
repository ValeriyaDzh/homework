class Data:

    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip

    def __repr__(self) -> str:
        return f"Data '{self.data}' for server {self.ip}"


class Server:

    IP = 0

    def __init__(self):
        self.ip: int = self._generate_ip()
        self.buffer: list[Data] = []

    def __repr__(self) -> str:
        return f"Server {self.ip}"

    def _generate_ip(self):
        Server.IP += 1
        return Server.IP

    def get_ip(self):
        return self.ip

    def send_data(self, data: Data):
        self.buffer.append(data)

    def accept_data(self, data):
        self.buffer.append(data)

    def get_data(self):
        data = self.buffer[:]
        self.buffer.clear()
        return data


class Router:

    def __init__(self):
        self.conected_servers: set[Server] = set()
        self.buffer: list[Data] = []

    def link(self, server: Server):
        self.conected_servers.add(server)

    def unlink(self, server: Server):
        self.conected_servers.discard(server)

    def accept_data(self, data: Data):
        self.buffer.append(data)

    def send_data(self):
        self._prepare_data()
        while self.buffer:
            data = self.buffer.pop()
            for server in self.conected_servers:
                if data.ip == server.get_ip():
                    server.accept_data(data)

    def _prepare_data(self):
        for server in self.conected_servers:
            self.buffer.extend(server.get_data())
