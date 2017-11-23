from graphviz import Digraph

def connect(node_list,G):
    N = len(node_list)
    for number in range(N):
        if number is not 0:
                G.edge(str(node_list[number-1]),str(node_list[number]))

def create_parts(node,G):
    N = len(node)
    for number in range(N):
            G.node(str(node[number]),str(node[number]))

def Insert_key():
    all_node = []
    all_list = []
    print("Please enter a file name")
    file_names = input("Filename: ")
    print("Please enter a numeric value separated by a \",\"")
    while True:
        one_line = input("Input number: ")
        if one_line!="exit":
            one_list = one_line.split(",")
            all_node += one_list
            all_list.append(one_list)
        else:
            break
    return all_node,all_list,file_names

def main():
    G = Digraph(format="png")
    G.attr('node',shape='circle')

    all_node,all_list,Files = Insert_key()
    set_node = set(all_node)
    create_parts(list(set_node),G)

    for parts in(all_list):
        connect(parts,G)
    print(G)
    G.render(Files)

if __name__ == "__main__":
    main()
