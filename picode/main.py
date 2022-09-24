import cmdhandler
import mobility
import json

pathMode = True
curpath = []
isMoving = False

if __name__ == "__main__":
    networkingstuff = cmdhandler.cmdlink()
    networkingstuff.connect()
    while True:
        if not isMoving:
            command = networkingstuff.handleMsg()
            if "pathmode" in command:
                pathMode = command["pathmode"]
                print(pathMode)
            elif "path" in command:
                waypoints = command["path"]
                for waypoint in waypoints:
                    curpath.append(waypoint)
            
            if len(curpath) > 0:
                isMoving = True
        else:
            pass
