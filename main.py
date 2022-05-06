from llist import dllist, dllistnode
import bunny

def check_for_death(bunny_list):
    for bunny in bunny_list:
        if bunny.is_alive == False:
            bunny_list.remove(bunny)

def reproduction():
    pass

def culling():
    pass

def main():
    bunny_list = dllist()
    pass