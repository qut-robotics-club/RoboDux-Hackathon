import cmdhandler
import mobility

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
            elif "path" in command:
                curpath.append(command["path"])
            
            if len(curpath) > 0:
                isMoving = True
        else:
            pass
