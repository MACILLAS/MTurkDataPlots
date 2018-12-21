import csv
import json

urls = list()
coords = list()

#This code bit gets the image urls and coordinate data from MTurk Results
with open ('Batch_3466302_batch_results.csv','r') as csvfile:
    all_data = csv.DictReader(csvfile)
    for row in all_data:
        #print(row['Input.img_url'],row['Answer.coordinates'])
        urls.append(row['Input.img_url'])
        coords.append(row['Answer.coordinates'])
csvfile.close()

#This method takes str input
#and outputs a list of all x_coordinates
def return_x (coords):
    coord_str = coords
    x_coords = list()
    d = json.loads(coord_str)
    #This nested for loop plots all points
    for y in range (0, len(d),1): #All polygons
        for x in range (0,len(d[y]),1): #All points
            x_coords.append(d[y][x]['x'])
    return x_coords

#This method takes str input
#and outputs a list of all y coordinates
def return_y (coords):
    coord_str = coords
    y_coords = list()
    d = json.loads(coord_str)
    #Need to nest for loop to account for length of d
    for y in range (0,len(d),1):
        for x in range (0,len(d[y]),1):
            y_coords.append(d[y][x]['y'])
    return y_coords

#This method takes str, int and int input
#and returns a float of the x_coordinates of 'point' in 'polygon'
def return_x_point (coords, polygon, point):
    coord_str = coords
    x_coords = list()
    d = json.loads(coord_str)
    for x in range (0, len(d[polygon]),1):
        x_coords.append(d[polygon][x]['x'])
    return x_coords[point]

#This method takes str, int and int input
#and returns a float of the y_coordinates of 'point' in 'polygon'
def return_y_point (coords, polygon, point):
    coord_str = coords
    y_coords = list()
    d = json.loads(coord_str)
    for x in range (0, len(d[polygon]),1):
        y_coords.append(d[polygon][x]['y'])
    return y_coords[point]

#Create a new method that plots coordinates against its respective img source
def plot_coord (index):
    import matplotlib.pyplot as plt
    img = plt.imread(""+urls[index])
    fig, ax = plt.subplots()
    ax.imshow(img)
    #ax.scatter(return_x(coords[index]), return_y(coords[index]))
    #This series of nexted for loops will plot the different polygons
    e = json.loads(coords[index]) #This is not the most efficient implementation... FUTURE IMPROVEMNT
    for i in range(0, len(e), 1):
        for j in range(0, len(e[i]), 1):
            if j == len(e[i])-1:
                x1, x2 = return_x_point(coords[index], i, j), return_x_point(coords[index], i, 0)
                y1, y2 = return_y_point(coords[index], i, j), return_y_point(coords[index], i, 0)
            else:
                x1, x2 = return_x_point(coords[index], i, j), return_x_point(coords[index], i, j+1)
                y1, y2 = return_y_point(coords[index], i, j), return_y_point(coords[index], i, j+1)
            ax.plot([x1, x2], [y1, y2], 'r-')
    plt.show()

#Call this function to plot x-y coordinates on photo
#This function takes the index of the plot you want view
plot_coord(5)


# with open('test2.txt', 'r') as f:
#    read_data = f.read()
#    print(read_data)
# f.close()
# d = json.loads(read_data)
#
#
# print(d)
# print()
# print(d[0][0]['x'])
# print(d[0][1]['x'])
# print (len(d[0])