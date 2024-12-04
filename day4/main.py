def find_word(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == word[0]:
                for direction in directions:
                    x = i + direction[0]
                    y = j + direction[1]
                    if x < 0 or y < 0 or x >= rows or y >= cols:
                        continue
                    if matrix[x][y] == word[1]:
                        for k in range(2, len(word)):
                            x += direction[0]
                            y += direction[1]
                            if x < 0 or y < 0 or x >= rows or y >= cols:
                                break
                            if matrix[x][y] != word[k]:
                                break
                        else:
                            count += 1

    return count

def find_word_pt2(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "A":
                if i > 0 and i < rows -1 and j > 0 and j < cols - 1:
                    try:
                        if matrix[i-1][j-1] == "M" and matrix[i-1][j+1] == "S" and matrix[i+1][j-1] == "M" and matrix[i+1][j+1] == "S":
                            count += 1
                        elif matrix[i-1][j-1] == "M" and matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S" and matrix[i+1][j+1] == "S":
                            count += 1
                        elif matrix[i-1][j-1] == "S" and matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S" and matrix[i+1][j+1] == "M":
                            count += 1
                        elif matrix[i-1][j-1] == "S" and matrix[i-1][j+1] == "S" and matrix[i+1][j-1] == "M" and matrix[i+1][j+1] == "M":
                            count += 1
                    except IndexError:
                        continue

    return count


matrix = []

with open('input.txt') as f:
    for line in f:
        matrix.append([c for c in line.strip()])



print(find_word(matrix, "XMAS")) 
print(find_word_pt2(matrix)) 
