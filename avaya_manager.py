import paramiko, time

class ParamikoConnect:
    """Manager of context for lib paramiko"""
    def __init__(self, config: dict) -> None:
        self.config = config
    def __enter__(self) -> 'connect':
        self.conn = paramiko.SSHClient()
        self.conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.conn.connect(**self.config,look_for_keys=False, allow_agent=False)
        self.new_conn = self.conn.invoke_shell()
        self.new_conn.send('enable\n')
        self.new_conn.send('terminal length 0\n')
        time.sleep(1)
        self.new_conn.recv(5000)
        return self.new_conn
    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.new_conn.close()



