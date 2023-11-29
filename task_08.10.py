def floodFill(self, image, sr, sc, newColor):
    s_color = image[sr][sc]
    x_len = len(image)
    y_len = len(image[0])
    def change(x,y):
        if x < 0 or x == x_len:
            return
        elif y < 0 or y == y_len:
            return
        elif image[x][y] == newColor:
            return
        elif image[x][y] == s_color:
            image[x][y] = newColor
            change(x - 1, y)
            change(x + 1, y)
            change(x, y - 1)
            change(x, y + 1)
        else:
            return
    change(sr - 1, sc)
    change(sr + 1, sc)
    change(sr, sc - 1)
    change(sr, sc + 1)
    return image


print(floodFill(None, [[0,0,0],[0,1,0]], 1, 1, 2))