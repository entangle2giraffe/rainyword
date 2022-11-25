import sender.player as player
import app
import sender.match_request as request


def quit(id:int):
    #app.Server.connections
    #print('print in quit')
    #print(app.Server.connections)
    #print(app.Server.get_connection(app.Server))
    #if app.Server.connections[player.find(id)] != "null":
        #app.Server.connections.pop(player.find(id))
    request.remove_request(id)
    player.remove_from_list(id)