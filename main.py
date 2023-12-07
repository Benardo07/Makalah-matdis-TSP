from itertools import combinations

def held_karp_tsp(distance_matrix):
    n = len(distance_matrix)
    C = {}

    for k in range(1, n):
        C[(1 << k, k)] = (distance_matrix[0][k], 0)

    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + distance_matrix[m][k], m))
                C[(bits, k)] = min(res)
    
    bits = (2**n - 1) - 1
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + distance_matrix[k][0], k))
    opt, parent = min(res)

    path = [0]
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits
    path.append(0)

    return list(reversed(path)), opt


distance_matrix = [[0, 31278, 29741, 31041, 28908, 31707, 29159, 31249, 23949, 30979, 24674, 15765, 29457, 26758, 32002, 23125, 33014, 13570, 20226, 12665], 
                    [29535, 0, 1310, 1324, 3561, 3039, 12246, 1977, 3613, 3100, 6246, 4464, 5707, 4193, 3956, 3749, 3668, 5483, 6453, 6079], 
                    [28704, 1065, 0, 1599, 3459, 2936, 12540, 2759, 2782, 3226, 5415, 3626, 5605, 3362, 4250, 2918, 3572, 4652, 5622, 5248], 
                    [29611, 1054, 1387, 0, 3638, 3115, 13300, 3031, 3690, 4154, 6323, 4541, 5784, 4270, 5010, 3826, 2651, 5560, 6529, 6156], 
                    [27146, 4418, 2981, 4181, 0, 4847, 13710, 4666, 2979, 4396, 3857, 3890, 4355, 1791, 5420, 2155, 6154, 3873, 4069, 5040], 
                    [29224, 3342, 2742, 3105, 2657, 0, 15812, 5319, 5045, 6498, 5935, 5993, 4803, 3869, 7522, 4257, 5078, 5976, 6189, 7143],
                    [37194, 12248, 13231, 14410, 16063, 15540, 0, 10499, 12859, 9563, 15867, 12203, 17347, 13814, 8488, 14160, 14157, 16423, 16074, 15264],
                    [30944, 1977, 3287, 3180, 5538, 5016, 10498, 0, 4158, 1351, 7655, 3503, 7684, 5603, 2208, 5948, 3658, 7666, 7862, 7486],
                    [28866, 4239, 2824, 4003, 5655, 5133, 12263, 3375, 0, 2713, 5578, 1036, 7058, 3525, 3736, 2303, 5975, 4309, 5784, 3668],
                    [29848, 3100, 3924, 5103, 6755, 6233, 9569, 1351, 2938, 0, 6560, 2282, 8040, 4507, 1279, 4852, 5009, 6571, 6766, 6136], 
                    [24917, 7567, 8142, 7330, 6566, 6336, 18693, 9650, 8216, 9380, 0, 9780, 4784, 5158, 10403, 7102, 9303, 6495, 7569, 8612],
                    [29461, 4155, 3547, 4725, 6378, 5855, 11566, 3444, 970, 2346, 6172, 0, 7652, 4119, 3321, 3594, 6698, 5050, 6379, 3930],
                    [27432, 4839, 4239, 4603, 3838, 3609, 16947, 6817, 6216, 7633, 4169, 7127, 0, 4614, 8657, 5392, 6576, 7110, 6934, 8277],
                    [27622, 5504, 4903, 5267, 2151, 4273, 14600, 5557, 3869, 5286, 4333, 4780, 3533, 0, 6310, 3045, 7240, 4763, 4587, 5930],
                    [30864, 3956, 4940, 6118, 7771, 7248, 8505, 2208, 3904, 1271, 7576, 3249, 9056, 5523, 0, 5868, 5865, 7587, 7782, 7102],
                    [27830, 4673, 3257, 4436, 4626, 5566, 13348, 4776, 1819, 4505, 4542, 2114, 6008, 2475, 5529, 0, 6409, 2452, 3954, 3264], 
                    [31783, 3225, 3558, 2171, 5809, 5286, 14155, 3658, 5861, 5009, 8494, 6712, 7955, 6441, 5865, 5997, 0, 7731, 8701, 8327], 
                    [20405, 5986, 4571, 5750, 3415, 5537, 14587, 5544, 3133, 5273, 3307, 4045, 4798, 1253, 6297, 2309, 7722, 0, 2225, 3265], 
                    [20314, 6576, 5160, 6339, 3967, 6090, 15177, 6133, 3723, 5863, 3860, 4634, 5350, 1805, 6887, 2899, 8312, 2551, 0, 3855], 
                    [18723, 6952, 5536, 6715, 4794, 6916, 16186, 6922, 3936, 6652, 4686, 4090, 6176, 2632, 7676, 3274, 8688, 1422, 3604, 0]]


# Using Held-Karp algorithm to find the shortest route
shortest_route, total_distance = held_karp_tsp(distance_matrix)
print(shortest_route)
print(total_distance)

# import matplotlib.pyplot as plt
# import networkx as nx
# import numpy as np

# def draw_graph(path, distance_matrix):
#     G = nx.DiGraph()

#     # Add nodes and edges
#     for i in range(len(path) - 1):
#         G.add_edge(path[i], path[i + 1], weight=distance_matrix[path[i]][path[i + 1]])

#     # Custom positions for nodes in circular layout according to the path
#     # pos = {node: (np.cos(angle)*2, np.sin(angle)*2) for node, angle in zip(path, np.linspace(0, 2*np.pi, len(path), endpoint=False))}
#     # pos = nx.spring_layout(G)
#     # # Draw the graph
#     # nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=300)

#     # # Optionally, draw edge labels
#     # edge_labels = nx.get_edge_attributes(G, 'weight')
#     # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

#     # plt.show()
#     layout = nx.spring_layout(G)

# # Use a list for node_sizes
#     sizes = [200 for _ in range (20)]
#     nx.draw(G, layout, with_labels=True, node_size=sizes, node_color="yellow")

# # Get weights of each edge and assign to labels
#     labels = nx.get_edge_attributes(G, "weight")

#     # # Draw edge labels using layout and list of labels
#     nx.draw_networkx_edge_labels(G,pos=layout, edge_labels=labels)
#     plt.show()

# # Draw the graph
# draw_graph(shortest_route, distance_matrix)

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def draw_graph(path, distance_matrix, edge_length_factor=2.0):
    G = nx.DiGraph()

    # Add nodes and edges
    for i in range(len(path) - 1):
        G.add_edge(path[i], path[i + 1], weight=distance_matrix[path[i]][path[i + 1]])

    # Create a layout with custom node positions and longer edges
    layout = {}
    for i, node in enumerate(path):
        angle = i * (2 * np.pi / len(path))
        x = np.cos(angle) * edge_length_factor
        y = np.sin(angle) * edge_length_factor
        layout[node] = (x, y)

    # Draw the graph with longer edges
    nx.draw(G, layout, with_labels=True, node_size=200, node_color="lightblue")

    # Get weights of each edge and assign to labels
    labels = nx.get_edge_attributes(G, "weight")

    # Draw edge labels using layout and list of labels
    nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=labels)
    plt.show()

# Draw the graph with longer edges
draw_graph(shortest_route, distance_matrix, edge_length_factor=2.5)
