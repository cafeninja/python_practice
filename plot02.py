import matplotlib.pyplot as plt 

# line 1 points 
x1 = [1,2,3,4] 
y1 = [15,20,5,5] 
# plotting the line 1 points 
plt.plot(x1, y1, label = "Detected") 

# line 2 points 
x2 = [1,2,3,4] 
y2 = [0,0,1,3] 
# plotting the line 2 points 
plt.plot(x2, y2, label = "Deaths") 

# line 3 points 
x3 = [1,2,3,4] 
y3 = [0,5,19,50] 
# plotting the line 2 points 
plt.plot(x3, y3, label = "Recoveries") 

# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
# giving a title to my graph 
plt.title('Covid 19 Malta') 

# show a legend on the plot 
plt.legend() 

# function to show the plot 
plt.show() 
