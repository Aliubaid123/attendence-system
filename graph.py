'''import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([10,20])
ypoints=np.array([0,625])
plt.plot(xpoints,ypoints,'o')
plt.show()'''



'''import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array([1,7])
ypoints = np.array([3,7])
plt.plot(xpoints, ypoints)
plt.show()
'''


'''import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([7,10,20,26])
plt.plot(ypoints , marker= '|')
plt.show()'''

# g mean add a color 
'''import matplotlib.pyplot as plt
import numpy as np

ypoints=np.array([3,7,10,26])
plt.plot(ypoints , 'o-g') # g mean color
plt.show()'''
#  ms marker size   and mec marker edge color
'''import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,6,9,10])
ypoints=([5,9,20,34])
plt.plot(xpoints,ypoints,marker='o',ms=20,mec='r') #  ms marker size   and mec marker edge color
plt.show()'''
#  ms marker size   and mfc marker face color
'''import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,6,7,10])
ypoints=([5,9,17,34])
plt.plot(xpoints,ypoints,marker='o',ms=20,mfc='r') #  ms marker size   and mfc marker face color
plt.show()'''
# linestyle =dotted
'''import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,6,7,10])
ypoints=([5,9,17,34])
plt.plot(xpoints,ypoints,linestyle='dotted')# linestyle =dotted
plt.show()'''
# linestyle =dashed lined
'''import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,6,7,10])
ypoints=([5,9,17,34])
plt.plot(xpoints,ypoints,linestyle='dashed')# linestyle =dashed lined
plt.show()'''
# for line width 
'''import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5') # for line width 
plt.show()'''


'''import matplotlib.pyplot as plt
import numpy as np
y1=np.array([3,5,6,7])
y2=np.array([5,7,8,10])

plt.plot(y1)
plt.plot(y2)
plt.show()'''

# create a label for a plot
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x,y)
plt.title("This is a graph",loc='left') # title of the plot and location of the litle 
plt.xlabel("this is x-axix")
plt.ylabel("this is y-axix")
plt.show()'''


# add grid to a graph
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x,y)
plt.title(" This is a graph ",loc='left')
plt.xlabel("this is x_axis graph ")
plt.ylabel("this is y_axis graph")
plt.grid()
plt.show()'''

# add grid on x axis 
'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x,y)
plt.title(" This is a graph ",loc='left')
plt.xlabel("this is x_axis graph ")
plt.ylabel("this is y_axis graph")
plt.grid(axis='x')
plt.show()'''
#set line color ,linewidth and linestyle in grid

'''import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.plot(x,y)
plt.title(" This is a graph ",loc='left')
plt.xlabel("this is x_axis graph ")
plt.ylabel("this is y_axis graph")
plt.grid(color='yellow',linestyle='dotted' ,linewidth=2)
plt.show()'''

# sub plts 
'''import matplotlib.pyplot as plt
import numpy as np

# Plot 1
x = np.array([2, 4, 6, 8])
y = np.array([3, 5, 7, 9])
plt.subplot(1,2, 1)  # 1 row, 2 columns, 1st plot
plt.plot(x, y)
plt.title("Plot 1")

# Plot 2
x = np.array([1, 3, 5, 7])
y = np.array([2, 4, 6, 8])
plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd plot
plt.plot(x, y)
plt.title("Plot 2")

plt.show()'''
# many plots
'''import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 6, 3])
y = np.array([3, 7, 8, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)
plt.title('sales')
plt.grid()

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)
plt.title('purshase')
plt.grid()

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)
plt.title('shopkeeper')
plt.grid()

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.suptitle('MY Shop')
plt.show()'''
# scatter 

'''import matplotlib.pyplot as plt
import numpy as np 
x=np.array([10,12,14,15,24,28,30,40,45,50])
y=np.array([9,11,13,15,17,19,21,23,27,29])
plt.scatter(x,y) # scatter mean show only the points 
plt.show()'''
# compare plot in scatter 
'''import matplotlib.pyplot as plt
import numpy as np
#plot 1
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)
# plot 2 
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()'''
# different colors 
'''import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()'''
# marker om own size
'''import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes , alpha=0.5)

plt.show()'''
# matplotlib bars 

'''import matplotlib.pyplot as plt
import numpy as np
x=np.array(["A","B","C","D"])
y=np.array([10,20,5,15])
plt.bar(x,y)
plt.show()'''

'''import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 250)

plt.hist(x, 5)
plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt

# Generate 100,000 values with normal distribution
# mean = 5.0, standard deviation = 1.0
'''x = np.random.normal(5.0, 1.0, 100000)

# Plot histogram
plt.hist(x, bins=100, color='skyblue', edgecolor='black')
plt.title("Normal Distribution (Mean=5.0, Std=1.0)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()'''

import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(2.0, 1.0,100000)
plt.hist(x, 90)
plt.show()



















