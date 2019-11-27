from collections import defaultdict
adj_list =defaultdict(list)
file=open("Wiki-Vote.txt","r")
lines=file.readlines()
for line in lines:
    word=line.split()
    if word[1] not in adj_list[word[0]]:
        adj_list[word[0]].append(word[1])
file.close()
print(len(adj_list))

temp=[]
#find connected components
def printSCCs(a_list):

    stack = []
    # Mark all the vertices as not visited (For first DFS)
    visited =set()
    # Fill vertices in stack according to their finishing
    # times
    for i in list(a_list):
        if i not in visited:
            fillOrder(a_list,i, visited, stack)

    # Create a reversed graph
    gr = getTranspose(a_list)

         # Mark all the vertices as not visited (For second DFS)
    visit =set()

         # Now process all vertices in order defined by Stack
    while stack:
        i = stack.pop()
        if i not in visit:
            DFSUtil(gr,i, visit)

    print(len(temp))
def fillOrder(a_list,v,visited, stack):
    # Mark the current node as visited
    visited.add(v)

    adj_f=[i for i in a_list[v]]
    #Recur for all the vertices adjacent to this vertex
    for i in adj_f:
        if i not in visited:
            fillOrder(a_list, i, visited, stack)
    stack = stack.append(v)

def DFSUtil(a_list,v,visit):
    # Mark the current node as visited and print it
    visit.add(v)

    adj_v=[i for i in a_list[v]]
    temp.append(v)


    #Recur for all the vertices adjacent to this vertex
    for i in adj_v:
        print("prior to next component")
        if i not in visit:
            print(" next component")
            DFSUtil(adj_list,i,visit)


def getTranspose(a_list):
    adj_list_t =defaultdict(list)

    # Recur for all the vertices adjacent to this vertex
    for key in list(a_list):
        adj_v=[k for k in a_list[key]]
        for j in adj_v:
            adj_list_t[j].append(key)

    return adj_list_t

printSCCs(adj_list)
