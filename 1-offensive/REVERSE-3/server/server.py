#!/usr/bin/python

import argparse
import socket
import json
import time
from threading import Thread, Lock
from rooms import Rooms, RoomNotFound, NotInRoom, RoomFull,PlayerCheater, Room


def main_loop(tcp_port, udp_port, rooms):
    """
    Start udp and tcp server threads
    """
    lock = Lock()
    udp_server = UdpServer(udp_port, rooms, lock)
    tcp_server = TcpServer(tcp_port, rooms, lock)
    udp_server.start()
    tcp_server.start()
    is_running = True
#    print("Simple Game Server.")
#    print("--------------------------------------")
#    print("list : list rooms")
#    print("room #room_id : print room information")
#    print("user #user_id : print user information")
#    print("quit : quit server")
#    print("--------------------------------------")

#    while is_running:
#        cmd = input("cmd >")
#        if cmd == "list":
#            print("Rooms :")
#            for room_id, room in rooms.rooms.items():
#                print("%s - %s (%d/%d)" % (room.identifier,
#                                           room.name,
#                                           len(room.players),
#                                           room.capacity))
#        elif cmd.startswith("room "):
#            try:
#                id = cmd[5:]
#                room = rooms.rooms[id]
#                print("%s - %s (%d/%d)" % (room.identifier,
#                                           room.name,
#                                           len(room.players),
#                                           room.capacity))
#                print("Players :")
#                for player in room.players:
#                    print(player.identifier)
#            except:
#                print("Error while getting room informations")
#        elif cmd.startswith("user "):
#            try:
#                player = rooms.players[cmd[5:]]
#                print("%s : %s:%d" % (player.identifier,
#                                      player.udp_addr[0],
#                                      player.udp_addr[1]))
#            except:
#                print("Error while getting user informations")
#        elif cmd == "quit":
#            print("Shutting down  server...")
#            udp_server.is_listening = False
#            tcp_server.is_listening = False
#            is_running = False
#
#    udp_server.join()
#    tcp_server.join()


class UdpServer(Thread):
    def __init__(self, udp_port, rooms, lock):
        """
        Create a new udp server
        """
        Thread.__init__(self)
        self.rooms = rooms
        self.lock = lock
        self.is_listening = True
        self.udp_port = int(udp_port)
        self.msg = '{"success": %(success)s, "message":"%(message)s"}'

    def run(self):
        """
        Start udp server
        """
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_DGRAM)
        self.sock.bind(("0.0.0.0", self.udp_port))
        self.sock.setblocking(0)
        self.sock.settimeout(5)
        while self.is_listening:
            try:
                data, address = self.sock.recvfrom(1024)
            except socket.timeout:
                continue

            try:
                data = json.loads(data)
                try:
                    identifier = data['identifier']
                except KeyError:
                    identifier = None

                try:
                    room_id = data['room_id']
                except KeyError:
                    room_id = None

                try:
                    payload = data['payload']
                except KeyError:
                    payload = None

                try:
                    action = data['action']
                except KeyError:
                    action = None

                try:
                    if room_id not in self.rooms.rooms.keys():
                        raise RoomNotFound
                    self.lock.acquire()
                    try:
                        if action == "send":
                            try:
                                self.rooms.send(identifier,
                                                room_id,
                                                payload['message'],
                                                self.sock)
                            except:
                                pass
                        elif action == "sendto":
                            try:
                                self.rooms.sendto(identifier,
                                                  room_id,
                                                  payload['recipients'],
                                                  payload['message'],
                                                  self.sock)
                            except:
                                pass
                    finally:
                        self.lock.release()
                except RoomNotFound:
                    print("Room not found")

            except KeyError:
                print("Json from %s:%s is not valid" % address)
            except ValueError:
                print("Message from %s:%s is not valid json string" % address)

        self.stop()

    def stop(self):
        """
        Stop server
        """
        self.sock.close()


class TcpServer(Thread):
    def __init__(self, tcp_port, rooms, lock):
        """
        Create a new tcp server
        """
        Thread.__init__(self)
        self.lock = lock
        self.tcp_port = int(tcp_port)
        self.rooms = rooms
        self.is_listening = True
        self.msg = '{"success": "%(success)s", "message":"%(message)s"}'

    def run(self):
        """
        Start tcp server
        """
        self.sock = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM)
        self.sock.bind(('0.0.0.0', self.tcp_port))
        self.sock.setblocking(0)
        self.sock.settimeout(5)
        time_reference = time.time()
        time_reference1 = time.time()
        self.sock.listen(1)

        while self.is_listening:

            #  Clean empty rooms
            if time_reference + 60 < time.time():
                print("Cleaning empty")
                self.rooms.remove_empty()
                time_reference = time.time()
            if time_reference1 + 30 < time.time():
                print("Cleaning ended")
                self.rooms.remove_ended()
                self.rooms.add_bots()
                time_reference1 = time.time()
            try:
                conn, addr = self.sock.accept()
            except socket.timeout:
                continue

            data = conn.recv(1024)
            try:
                print("recived_data:", data)
                data = json.loads(data)
                action = None
                try:
                    action = data['action']
                except:
                    pass
                identifier = None
                try:
                    identifier = data['identifier']
                except:
                    pass  # Silently pass

                room_id = None
                try:
                    room_id = data['room_id']
                except:
                    pass  # Silently pass

                payload = None
                try:
                    payload = data['payload']
                except:
                    pass  # Silently pass
                self.lock.acquire()
                try:
                    self.route(conn,
                               addr,
                               action,
                               payload,
                               identifier,
                               room_id)
                finally:
                    self.lock.release()
            except KeyError:
                print("Json from %s:%s is not valid" % addr)
                conn.send(b"Json is not valid")
            except ValueError:
                print("Message from %s:%s is not valid json string" % addr)
                conn.send(b"Message is not a valid json string")

            conn.close()

        self.stop()

    def route(self,
              sock,
              addr,
              action,
              payload,
              identifier=None,
              room_id=None):
        """
        Route received data for processing
        """
        if action == "register":
            client = self.rooms.register(addr, int(payload))
            client.send_tcp(True, client.identifier, sock)
            return 0

        if identifier is not None:
            if identifier not in self.rooms.players.keys():
                print("Unknown identifier %s for %s:%s" % (identifier, addr[0], addr[1]))
                sock.send((self.msg % {"success": "False", "message": "Unknown identifier"}).encode())
                return 0

            # Get client object
            client = self.rooms.players[identifier]

            if action == "autojoin":
                room_id = self.rooms.join(identifier, room_id)
                client.send_tcp(True, room_id, sock)
            elif action == "debuggame":
                room_id = self.rooms.join(identifier, room_id)
                client.send_tcp(True, room_id, sock)
                self.rooms.rooms[room_id].add_bots(True)
            elif action == "isready":
                try:
                    if room_id not in self.rooms.rooms.keys():
                        raise RoomNotFound()
                    client.send_tcp(True, str(self.rooms.rooms[room_id].is_ready(identifier)), sock)
                except RoomNotFound:
                    client.send_tcp(False, room_id, sock)
                except NotInRoom:
                    client.send_tcp(False, room_id, sock)
                except:
                    client.send_tcp(False, room_id, sock)
            elif action == "sendans":
                try:
                    if room_id not in self.rooms.rooms.keys():
                        raise RoomNotFound()
                    if self.rooms.rooms[room_id].state == "Game":
                        client.send_tcp(True, self.rooms.rooms[room_id].recive_nudes(identifier, payload) , sock)
                    else:
                        client.send_tcp(False, "Wait until game started", sock)
                except RoomNotFound:
                    client.send_tcp(False, room_id, sock)
                except NotInRoom:
                    client.send_tcp(False, room_id, sock)
                except:
                    client.send_tcp(False, room_id, sock)
            elif action == "getseed":
                try:
                    if room_id not in self.rooms.rooms.keys():
                        raise RoomNotFound()
                    if self.rooms.rooms[room_id].state == "Game":
                        client.send_tcp(True, self.rooms.rooms[room_id].get_seed(identifier), sock)
                    else:
                        client.send_tcp(False, "Wait until game started", sock)
                except NotInRoom:
                    client.send_tcp(False, room_id, sock)
                except RoomNotFound:
                    client.send_tcp(False, room_id, sock)
                except:
                    client.send_tcp(False, room_id, sock)
            elif action == "isended":
                try:
                    if room_id not in self.rooms.rooms.keys():
                        raise RoomNotFound()
                    client.send_tcp(True, str(self.rooms.rooms[room_id].is_ended(identifier)), sock)
                except NotInRoom:
                    client.send_tcp(False, room_id, sock)
                except RoomNotFound:
                    client.send_tcp(False, room_id, sock)
                except:
                    client.send_tcp(False, room_id, sock)
            elif action == "getflag":
                try:
                    if room_id not in self.rooms.rooms.keys():
                        raise RoomNotFound()
                    if self.rooms.rooms[room_id].state == "End":
                        client.send_tcp(True, self.rooms.rooms[room_id].get_flag(client), sock)
                    else:
                        client.send_tcp(False, "Wait until game ended", sock)
                except NotInRoom:
                    client.send_tcp(False, room_id, sock)
                except RoomNotFound:
                    client.send_tcp(False, room_id, sock)
                except:
                    client.send_tcp(False, room_id, sock)
            else:
                sock.send((self.msg % {"success": "False",
                                        "message": "Not in ['autojoin','debuggame','getflag','isready','isended','getseed', 'sendans'] sequence"}).encode())
        else:
            sock.send((self.msg % {"success": "False",
                                        "message": "You must register"}).encode())

    def stop(self):
        """
        Stop tcp data
        """
        self.sock.close()


if __name__ == "__main__":
    """
    Start a game server
    """
    parser = argparse.ArgumentParser(description='Simple game server')
    parser.add_argument('--tcpport',
                        dest='tcp_port',
                        help='Listening tcp port',
                        default="1234")
    parser.add_argument('--udpport',
                        dest='udp_port',
                        help='Listening udp port',
                        default="1234")
    parser.add_argument('--capacity',
                        dest='room_capacity',
                        help='Max players per room',
                        default="3")

    args = parser.parse_args()
    rooms = Rooms(int(args.room_capacity))
    main_loop(args.tcp_port, args.udp_port, rooms)
