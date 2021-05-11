class CommandHandler:

  def ping():
    return 'pong'

  commands = {
    'ping': ping
  }



  def run(self, cmd):
    cmd = cmd.split(" ")[3][1:][1:].rstrip()
    return self.commands[cmd]()
