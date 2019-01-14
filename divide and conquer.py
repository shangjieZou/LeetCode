# divide and conquer
def kClosest(points, K):
    import math
    middle = len(points)//2
    points_left = points[0:middle]
    points_right = points[middle]
    #list_index_left = [i for i in range(len(points_left))]
    #list_index_right = [j for j in range(len(points_right))]
    left_K_list = []
    right_K_list = []

    if K > len(points)//2:
        Selected_K_list = []
        for i in range(K):
            Selected_K_list.append(points[i])
        for j in range(K, len(points)):
            for k in range(K):
                if (math.sqrt(points[j][0] ** 2 + points[j][1] ** 2)) > (
                math.sqrt(Selected_K_list[k][0] ** 2 + Selected_K_list[k][1] ** 2)):
                    Selected_K_list.remove(Selected_K_list[k])
                    Selected_K_list.append(points[j])
    else:
        for i in range(K):
            left_K_list.append(points_left[i])
            right_K_list.append(points_right[i])
        for j in range(K, len(points_left)):
            for k in range(K):
                if (math.sqrt(points_left[j][0]**2+points_left[j][1]**2)) > (math.sqrt(left_K_list[k][0]**2+left_K_list[k][1]**2)):
                    left_K_list.remove(left_K_list[k])
                    left_K_list.append(points_left[j])
            for k in range(K):
                if (math.sqrt(points_right[j][0]**2+points_right[j][1]**2)) > (math.sqrt(right_K_list[k][0]**2+right_K_list[k][1]**2)):
                    right_K_list.remove(right_K_list[k])
                    right_K_list.append(points_right[j])

        All_selected_list = left_K_list+right_K_list
        Selected_K_list = []
        print(All_selected_list)
        for i in range(K):
            Selected_K_list.append(All_selected_list[i])
        for j in range(K, len(All_selected_list)):
            for k in range(K):
                if (math.sqrt(All_selected_list[j][0]**2+All_selected_list[j][1]**2)) > (math.sqrt(Selected_K_list[k][0]**2+Selected_K_list[k][1]**2)):
                    Selected_K_list.remove(Selected_K_list[k])
                    Selected_K_list.append(All_selected_list[j])

    for i in range(K):
        return Selected_K_list[i]




points = [[1,3],[-2,2]]
K = 1
print(kClosest(points, K))
