import sender.player as player
import app
import sender.match_request as request


def quit(id:int):
    player.remove_from_list(id)
    if app.Server.connections[player.find(id)] != "null":
        app.Server.connections.pop(player.find(id))
    request.remove_request(id)