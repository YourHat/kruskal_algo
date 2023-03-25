import csv
import time


def main():

    ####### for time complexity ( report )  ################################
    #k_time = 0
    #p_time = 0
    #for i in range(10):
    #    adj, ite, dic, m_num, max_num = get_matrix("e2.csv")
    #    s_t = time.time()
    #    kruskal(adj,ite,dic, m_num, max_num)
    #    k_time += (time.time() - s_t)
    #    s_t = time.time()
    #    prim(adj,ite,dic, m_num, max_num)
    #    p_time += (time.time() - s_t)
    #print("kruskal ", k_time/10)
    #print("prim" , p_time/10)
    #########################################################################



    while(True):
        csv_file = input("\ntype a file name (type 'd' to terminate) : ")
        if csv_file == 'd':
            break
        adj, ite, dic, m_num, max_num = get_matrix(csv_file)
        alg = input("type a letter \n'k' - kruskal's algorithm\n'p' - prim's algorithm\n -> ")
        if alg == 'k':
            kruskal(adj,ite,dic, m_num, max_num)
        elif alg == 'p':
            prim(adj,ite,dic, m_num, max_num)
 


def prim(a_m, items, tree, mat_n, max_num):

    print("\nnode list\n")
    print(items)
    print("\nmatrix\n")
    for i in a_m:
        print(i)
    edg_li = []    
    edgelist = []
    min_num = max_num
    ind_mat = [0,0]
    for i in range(mat_n):
        for j in range(mat_n):
            if type(a_m[i][j]) == int:
                if min_num >= a_m[i][j]:
                    min_num = a_m[i][j]
                    ind_mat = [i,j]

    ori1 = ind_mat[0]
    ori2 = ind_mat[1]
    edgelist.append([items[ind_mat[0]],items[ind_mat[1]]])
    tree[ind_mat[1]] += tree[ind_mat[0]]
    tree[ind_mat[0]] = ind_mat[1]
    a_m[ori1][ori2],a_m[ori2][ori1] = None,None
    edg_li.append(ori1)
    edg_li.append(ori2)
    print(edgelist)

    while len(edg_li) < mat_n:
        min_num = max_num
        ind_mat = [0,0]
        for i in range(mat_n):
            for j in range(mat_n):
                if type(a_m[i][j]) == int:
                    if (i in edg_li) ^ (j in edg_li):
                        if min_num >= a_m[i][j]:
                            min_num = a_m[i][j]
                            ind_mat = [i,j]
        
        ori1 = ind_mat[0]
        ori2 = ind_mat[1]
        edgelist.append([items[ind_mat[0]],items[ind_mat[1]]])
        a_m[ori1][ori2],a_m[ori2][ori1] = None,None
        if ori1 not in edg_li:
            edg_li.append(ori1)
        else:
            edg_li.append(ori2)
        print(edgelist)


def kruskal(a_m, items, tree, mat_n, max_num):

    print("\nnode list\n")
    print(items)
    print("\nmatrix\n")
    for i in a_m:
        print(i)

    edgelist = []
    while max([ -1*x for x in tree]) < mat_n:
        min_num = max_num
        ind_mat = [0,0]
        for i in range(mat_n):
            for j in range(mat_n):
                if type(a_m[i][j]) == int:
                    if min_num >= a_m[i][j]:
                        min_num = a_m[i][j]
                        ind_mat = [i,j]
        

        node1 = tree[ind_mat[0]]
        node2 = tree[ind_mat[1]]
        ori1 = ind_mat[0]
        ori2 = ind_mat[1]

        while True:
            if node1 > 0:
                ind_mat[0] = node1
                node1 = tree[node1]
            if node1 < 0:
                break
                       
        
        while True:
            if node2 > 0:
                ind_mat[1] = node2
                node2 = tree[node2]
            if node2 < 0:
                break
   
        if ind_mat[0] != ind_mat[1]:
            edgelist.append([items[ori1],items[ori2]])
            if tree[ind_mat[0]] <= tree[ind_mat[1]]:
                tree[ind_mat[0]] += tree[ind_mat[1]]
                tree[ind_mat[1]] = ind_mat[0]
            else:
                tree[ind_mat[1]] += tree[ind_mat[0]]
                tree[ind_mat[0]] = ind_mat[1]
        a_m[ori1][ori2],a_m[ori2][ori1] = None,None
        print(edgelist)
            


def get_matrix(file):
    with open(file, mode="r") as cfile:
        csv_matrix = csv.reader(cfile)
        item_name = next(csv_matrix)
        a_matrix = []
        for line in csv_matrix:
            a_matrix.append(line)
    
    max_num = 0
    mat_num = len(a_matrix)
    for i in range(mat_num):
        for j in range(mat_num):
            if a_matrix[i][j] == '':
                a_matrix[i][j] = None
            else:
                a_matrix[i][j] = int(a_matrix[i][j])
                if a_matrix[i][j] >= max_num:
                    max_num = a_matrix[i][j]
    dict_tree = []
    for k in range(len(item_name)):
        dict_tree.append(-1)



    return a_matrix, item_name, dict_tree, mat_num, max_num




if __name__ == '__main__':
    main()
