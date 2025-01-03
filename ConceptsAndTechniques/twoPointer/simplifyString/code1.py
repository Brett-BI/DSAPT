def simplifyPath(path: str) -> str:
    n: int = len(path)
    p1: int = 0
    p2: int = p1 + 1
    tokens: [str] = []

    while p1 < p2:
        # path[p1], path[p2]
        p1 = p2
        p2 += 1
        # do stuff

    for i in range(n):
        for j in range(i+1, n):
            # do logic
            # /some/path/to/directory/
            # i = j

            # /some//path/./here -> /some//path/here
            break

    for i in range(n):
        #if path[i] == '/':
        if path[i] != '/':
            #print("Point 1 @{}: {}".format(i, path[i]))
            for j in range(i+1, n):
                
                if path[j] == '/': # add to tokens
                    print("Token (path[{}:{}]): {}".format(i, j, path[i:j]))
                    #print("Point 2 @{}: {}".format(j, path[j]))
                    #if path[i+1:j] == '..':
                    if path[i:j-1] == '..':
                        if len(tokens) > 0: tokens.pop(-1)
                    elif path[i:j-1] == '.':
                        None
                    else:
                        tokens.append(path[i:j-1])

                    # set index for i where j left off
                    i = j
                    #print(tokens)
                    break
                
    print("---------------")
    print("Path: {}".format(path))
    print(tokens)
    rString: str = ""
    for t in tokens:
        rString += "/{}".format(t)
    
    return rString

print(simplifyPath("/../"))
print(simplifyPath("/some/pathTo/../aDir/"))
print(simplifyPath("/home/"))
print(simplifyPath("/.../a/../b/c/../d/./"))
print(simplifyPath("/home//foo/"))
print(simplifyPath("/home/user/Documents/../Pictures"))