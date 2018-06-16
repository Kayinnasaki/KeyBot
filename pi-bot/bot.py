import socket, string, time
from evdev import UInput, ecodes as e

ui = UInput()

HOST = "chat.freenode.net"
PORT = 6667

NICK = "BottoTheBot"
IDENT = "Eeee"
REALNAME = "Botto"

s = socket.socket()
s.connect((HOST, PORT))
print("connecting")
s.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
s.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))
s.send(bytes("JOIN #bottesty\r\n", "UTF-8"));

def keytap (KEY):
    ui.write(e.EV_KEY, KEY, 1)
    ui.syn()
    time.sleep(0.55)
    ui.write(e.EV_KEY, KEY, 0)
    ui.syn()

def ping(): # respond to server Pings.
  ircsock.send(bytes("PONG :pingis\n", "UTF-8"))

while True:
    line = str(s.recv(1024))
    if "End of /NAMES list" in line:
        break

while True:
    text = s.recv(1024)
    data = text.decode('utf-8')
    if data.find('PING') != -1:
        s.send(str('PONG ' + data.split(':')[1] + '\r\n').encode())
        print('PONG sent \n') 

    for line in str(text).split('\\r\\n'):
        parts = line.split(':')
        if len(parts) < 3:
            continue

        if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
            message = parts[2][:len(parts[2])]

        usernamesplit = parts[1].split("!")
        username = usernamesplit[0]

        print(username + ": " + message)
        if message == "Hey":
            send_message("Welcome to my stream, " + username)

        if message == "up": keytap(e.KEY_UP)
        if message == "down": keytap(e.KEY_DOWN)
        if message == "left": keytap(e.KEY_LEFT)
        if message == "right": keytap(e.KEY_RIGHT)
        if message == "jump": keytap(e.KEY_A)
