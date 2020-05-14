def earliest_ancestor(ancestors, starting_node, count=None, hash_table=None):
    
    if type(ancestors) == list:
    
        """ converting a list of tuples into a hash of sets representing the graph """

        input_hash = {}
        my_set = set()

        for pair in ancestors:
            my_set.add(pair[0])
            my_set.add(pair[1])

        for node in my_set:
            input_hash[node] = set()

        for pair in ancestors:
            input_hash[pair[0]].add(pair[1])
            
        ancestors = input_hash


    """ count up the iterations and put them into a hash and take the max """
    
    if hash_table == None:
        hash_table = {}
    
    if count == None:
        count = 0 
    
    for vert in ancestors:
        children = list(ancestors[vert])
        if starting_node in children:
            count = count + 1 
            hash_table[count] = vert
            return earliest_ancestor(ancestors, vert, count, hash_table)
            
    if not hash_table:
        return -1 
    
    return hash_table[max(hash_table)]