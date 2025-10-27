# game 내의 객체들의 생성과 소멸을 관리하는 모듈입니다.

# world[0] : 0 layer
# world[1] : 1 layer
world = [[],[]] # 게임 내의 모든 객체를 담는 리스트입니다.

def add_object(o, depth = 0):
    world[depth].append(o)

def add_objects(ol, depth = 0):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

