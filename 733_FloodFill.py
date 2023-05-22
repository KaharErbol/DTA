def flood_fill(image: list[list[int]], sr:int, sc:int, color:int):
    if image[sr][sc] == color:
        return image
    
    fill(image, sr, sc, color, image[sr][sc])

    return image

def fill(image, sr, sc, color, cur):
    if sr < 0 or sr > len(image) or sc < 0 or sc > lem(image[0]):
        return
    if image[sr][sc] != cur:
        return
    image[sr][sc] = color

    fill(image, sr-1, sc, color, cur)
    fill(image, sr+1, sc, color, cur)
    fill(image, sr, sc-1, color, cur)
    fill(image, sr, sc+1, color, cur)