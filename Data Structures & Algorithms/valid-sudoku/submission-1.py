class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_in_column = {}
        seen_in_box = {}
        for i in range(len(board)):
            row = board[i]
            seen_in_row = {}
            for j in range(len(row)):
                value = row[j]
                if value == '.':
                    continue
                if value in seen_in_row:
                    print("Because of row: ",i, value)
                    print(seen_in_row)
                    return False
                else:
                    seen_in_row[value] = i
                if value in seen_in_column:
                    if seen_in_column[value] == j:
                        return False
                    else:
                        seen_in_column[value] = j
                else:
                    seen_in_column[value] = j
                box_key = (i//3,j//3)
                if box_key in seen_in_box:
                    if value in seen_in_box[box_key]:
                        print("Because of box key: ",box_key , value)
                        print(seen_in_box)
                        return False
                    else:
                        seen_in_box[box_key].append(value)
                else:
                    seen_in_box[box_key] = [value]
        return True
            

        