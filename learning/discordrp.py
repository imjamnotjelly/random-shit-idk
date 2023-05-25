from pypresence import Presence
import time

presopt = input("Which rich presence do you want to display?: ")

if presopt == "prodigy":
    server = input("What server are you playing on?: ")
    world = input("What world are you in?: ")
    element = input("What should the world icon be?: ")
    client_id = "796781322802561054"
    print("Starting status...")

    RPC = Presence(client_id)

    RPC.connect()
    stime = time.time()
    while True:
        RPC.update(state=f"In {world}",
                   details=f"Playing on: {server}",
                   start=stime,
                   large_image="logo",
                   small_image=element,
                   large_text="Prodigy",
                   small_text=world)

        time.sleep(15)
elif presopt == "zoom":
    client_id = "803747599710027826"
    stime = time.time()
    RPC = Presence(client_id)

    RPC.connect()

    while True:
        classopt = input("What class are you in?: ")
        print("Starting status... ")
        RPC.update(state=f"In {classopt}",
                   details="In a class",
                   start=stime,
                   large_image="logo",
                   large_text="Zoom")

        time.sleep(15)
else:
    print("Please enter a valid RP name.")
    time.sleep(5)

