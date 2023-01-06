#https://leetcode.com/problems/flipping-an-image/

class Solution(object):
    def flipAndInvertImage(self, image):
        for row in image:
            row.reverse()

        for i in range(len(image)):
            for j in range(len(image[i])):
                image[i][j] ^= 1
        return image


#
# a = [
#      [1,1,0],
#      [1,0,1],
#      [0,0,0]
# ]
#
#
#
# print([[1^q for q in row[::-1]] for row in a])