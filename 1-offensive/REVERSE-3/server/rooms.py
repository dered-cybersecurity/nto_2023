import uuid
import time
import ast
import random
import os
from player import Player
from graph import generate, check_moves

class Rooms:

    def __init__(self, capacity=2):
        """
        Handle rooms and set maximum rooms capacity
        """
        self.rooms = {}
        self.players = {}
        self.room_capacity = capacity

    def register(self, addr, udp_port):
        """
        Register player
        """
        player = None
        for registered_player in self.players.values():
            if registered_player.addr[0] == addr[0]:
                player = registered_player
                player.udp_addr = (addr[0], udp_port)
                break

        if player is None:
            player = Player(addr, udp_port)
            self.players[player.identifier] = player

        return player

    def join(self, player_identifier, room_id=None):
        """
        Add player to room
        """
        if player_identifier not in self.players:
            raise ClientNotRegistered()

        player = self.players[player_identifier]

        if room_id is None:
            for room_id in self.rooms.keys():
                if not self.rooms[room_id].is_full() and self.rooms[room_id].state == "Adding":
                    print("Join player", player_identifier, "to room",room_id)
                    self.rooms[room_id].players.append(player)
                    return room_id
                    break
            room_id = self.create()
            print("Created room", room_id)
            self.join(player_identifier, room_id)
            return room_id

        elif room_id in self.rooms:
            if not self.rooms[room_id].is_full():
                self.rooms[room_id].players.append(player)
                if len(self.rooms[room_id].players) == self.room_capacity:
                    print("Room",room_id, ": Game started")
                    self.rooms[room_id].state = "Game"
                    self.rooms[room_id].start_game()
                return room_id
            else:
                raise RoomFull()
        else:
            raise RoomNotFound()

    def leave(self, player_identifier, room_id):
        """
        Remove a player from a room
        """
        if player_identifier not in self.players:
            raise ClientNotRegistered()

        player = self.players[player_identifier]

        if room_id in self.rooms:
            self.rooms[room_id].leave(player)
        else:
            raise RoomNotFound()

    def create(self, room_name=None):
        """
        Create a new room
        """
        identifier = str(uuid.uuid4())
        self.rooms[identifier] = Room(identifier,
                                      self.room_capacity,
                                      room_name)
        return identifier

    def remove_empty(self):
        """
        Delete empty rooms
        """
        for room_id in list(self.rooms.keys()):
            if self.rooms[room_id].is_empty() or self.rooms[room_id].bot_only():
                print("Empty room", room_id, "deleted")
                del self.rooms[room_id]
    def remove_ended(self):
        """
        Delete ended rooms
        """
        for room_id in list(self.rooms.keys()):
            if self.rooms[room_id].state == "End" and self.rooms[room_id].flag_B:
                print("Ended room", room_id, "deleted")
                del self.rooms[room_id]
    def add_bots(self):
        """
        Add bots to those who waited enough
        """
        for room_id in list(self.rooms.keys()):
            if self.rooms[room_id].state == "Adding":
                print("Room", room_id, "adding bots")
                self.rooms[room_id].add_bots(False)

    def end_games(self):
        for room_id in list(self.rooms.keys()):
            if state.rooms[room_id].state == "Game":
                self.rooms[room_id].end_game(False)

    def send(self, identifier, room_id, message, sock):
        """
        Send data to all players in room, except sender
        """
        if room_id not in self.rooms:
            raise RoomNotFound()

        room = self.rooms[room_id]
        if not room.is_in_room(identifier):
            raise NotInRoom()

        for player in room.players:
            if player.identifier != identifier:
                player.send_udp(identifier, message)

    def sendto(self, identifier, room_id, recipients, message, sock):
        """
        Send data to specific player(s)
        """
        if room_id not in self.rooms:
            raise RoomNotFound()

        room = self.rooms[room_id]
        if not room.is_in_room(identifier):
            raise NotInRoom()
   
        if isinstance(recipients, str):
            recipients = [recipients]
            
        for player in room.players:
            if player.identifier in recipients:
                player.send_udp(identifier, message)


class Room:

    def __init__(self, identifier, capacity, room_name):
        """
        Create a new room on server
        """
        self.graph = None
        self.seed = int(random.randint(1,12345678))
        self.time_reference = time.time()
        self.capacity = capacity
        self.players = []
        self.identifier = identifier
        self.state = "Adding"
        self.flag_B = False
        self.bots_len = 0
        if room_name is not None:
            self.name = room_name
        else:
            self.name = self.identifier

    def join(self, player):
        """
        Add player to room
        """
        if not self.is_full():
            self.players.append(player)
        else:
            raise RoomFull()

    def leave(self, player):
        """
        Remove player from room
        """
        if player in self.players:
            self.players.remove(player)
        else:
            raise NotInRoom()

    def is_empty(self):
        """
        Check if room is empty or not
        """
        if len(self.players) == 0:
            return True
        else:
            return False

    def is_full(self):
        """
        Check if room is full or not
        """
        if len(self.players) == self.capacity:
            return True
        else:
            return False
    def add_bots(self, persistent):
        """
        Add bots
        """
        if self.is_full():
            return
        if self.time_reference + 30 < time.time() or persistent:
            for i in range(len(self.players), self.capacity):
                p = Player(('1234',122), 0)
                p.identifier = "BOT" + str(i)
                self.join(p)
            self.state = "Game"
            self.time_reference = time.time()
            self.start_game()

    def start_game(self):
        if len(self.players) != self.capacity:
            return
        self.graph, self.bots_len, self.seed = generate(self.seed)
        self.bots_len += 1
        print(self.identifier, "game started")
        self.state = "Game"
        self.time_reference = time.time()

    def get_seed(self, identifier):
        for i in self.players:
            if i.identifier == identifier:
                return str(self.seed)
        raise NotInRoom()

    def get_flag(self, i):
        i.niggers += 1
        if i.winner:
            return os.environ['FLAG']
        if i.niggers > 1999:
            return "Just F!#$ off lamer "+os.environ['FLAG']
        elif i.niggers > 999:
            return "oR nOt :-)0))))"
        elif i.niggers > 900:
            return "Yo're so close to flag..."
        elif i.niggers > 800:
            return "~flag is near~"
        elif i.niggers > 700:
            return "Okokok stop this shit flag is... Try harder :)"
        elif i.niggers > 600:
            return "Or not..."
        elif i.niggers > 500:
            return "Yes it is just reverse it :)"
        elif i.niggers > 100:
            return "You really thinks it is so easy?"
        elif i.niggers > 50:
            return "You'r not so good in ppc and reverse as I see"
        elif i.niggers > 10:
            return "Really you've just lost, take it easy bruh"
        else:
            return "No flag for losers"
        

    def try_end(self):
        count = 0
        for i in self.players:
            if "BOT" not in i.identifier:
                if i.ready == False:
                    print(i.identifier, i.ready)
                    count += 1
            i.ready = False
        if count == 0:
            self.end_game(True)
    
    def try_start(self):
        if self.state == "Game" or len(self.players) != self.capacity:
            return
        count = 0
        for i in self.players:
            if "BOT" not in i.identifier:
                if i.ready == False:
                    count += 1
                i.ready = False
        if count == 0:
            self.start_game()
    
    def is_ready(self, identifier):
        for i in self.players:
            if i.identifier == identifier:
                i.ready = True
        self.try_start()
        return self.state == "Game"

    def recive_nudes(self, identifier, payload):
        player = None
        for i in self.players:
            if identifier == i.identifier:
                player = i
        if player == None:
            raise NotInRoom()
        player.ready = True
        try:
            p = ast.literal_eval(payload)
        except:
            raise RoomNotFound()
        if type(p) != type([0,1,2]):
            raise RoomNotFound()
        if not check_moves(self.graph, p):
            raise RoomNotFound()
        else:
            player.chain = p
            player.chain_len = len(p)
            return "OK"
        
    def is_ended(self, identifier):
        for i in self.players:
            if i.identifier == identifier:
                i.ready = True
        self.try_end()
        return self.state == "End"

    def end_game(self, persistent):
        if self.time_reference + 10 < time.time() or persistent:
            mini = 1000000
            player = None
            for i in self.players:
                if "BOT" not in i.identifier and i.chain_len != 0:
                    temp = i.chain_len
                    if temp < mini:
                        mini = temp
                        player = i
            if mini < self.bots_len:
                print(player.addr[0], "WIN")
                player.winner = True
            else:
                print("BOT WIN")
            for i in self.players:
                self.leave(i)
            self.state = "End"
            self.flag_B = True
            print(self.identifier,"game ended")
    
    def bot_only(self):
        """
        Check if player is in room
        """
        in_room = True
        for player in self.players:
            if "BOT" not in player.identifier:
                in_room = False
                break
        return in_room
        

    def is_in_room(self, player_identifier):
        """
        Check if player is in room
        """
        in_room = False
        for player in self.players:
            if player.identifier == player_identifier:
                in_room = True
                break
        return in_room


class RoomFull(Exception):
    pass


class RoomNotFound(Exception):
    pass

class PlayerCheater(Exception):
    pass


class NotInRoom(Exception):
    pass


class ClientNotRegistered(Exception):
    pass
