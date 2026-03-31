import math


def get_player_pos() -> tuple:
    rt = [0.0, 0.0, 0.0]
    while (1):
        coord_str = input("Enter new coordinates as "
                          "floats in format 'x,y,z': ")
        coord_str = coord_str.replace(" ", "")
        coord = coord_str.split(",")
        if (len(coord) != 3):
            print("Invalid syntax")
            continue
        i = 0
        while (i < 3):
            try:
                rt[i] = float(coord[i])
            except ValueError as err:
                print(f"Error on parameter '{coord[i]}': {err}")
                break
            i += 1
        else:
            break
    return (rt[0], rt[1], rt[2])


def coordinate_system() -> None:
    print("=== Gane Coordinate System ===\n")
    print("Get a first set of coordinates")
    c1 = get_player_pos()
    print(f"Got a first tuple: {c1}")
    print(f"It includes: X={c1[0]}, Y={c1[1]}, Z={c1[2]}")
    print("Distance to center: "
          f"{round(math.sqrt(c1[0] ** 2 + c1[1] ** 2 + c1[2] ** 2), 4)}\n")
    print("Get a second set of coordinates")
    c2 = get_player_pos()
    dis = math.sqrt((c2[0]-c1[0])**2 + (c2[1]-c1[1])**2 + (c2[2]-c1[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(dis, 4)}")


if __name__ == "__main__":
    coordinate_system()
