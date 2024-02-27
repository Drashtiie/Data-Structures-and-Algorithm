def ff(image,sr,sc,color):
        q = [[sr,sc]]
        ic = image[sr][sc]
        v = [[0 for x in range(len(image[0]))] for y in range(len(image))]
        while q:
            d = q.pop(0)
            x = d[0]
            y = d[1]
            v[x][y] = 1
            image[x][y] = color
            l = [-1,0,1,0]
            l2 = [0,-1,0,1]
            for i in range(len(l)):
                
                        
                        x1 = x+l[i]
                        y1 = y+l2[i]
                        if x1 >=0 and x1 < len(image) and y1 >=0 and y1<len(image[0]) and image[x1][y1] == ic and v[x1][y1] == 0:
                            q.append([x1,y1])
                            # print(q)
        return image
print(ff([[1,1,1],[1,1,0],[1,0,1]],1,1,2))