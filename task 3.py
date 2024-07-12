import matplotlib.pyplot as plt
#Data
x=["python","c","c++","Java"]
y=[75,64,60,80]
#Labels and title
plt.xlabel("language")
plt.ylabel("No. ")
plt.title("Bar Chart")
#Plotting the bar chart
plt.bar(x,y,label="bar chart")
plt.legend()
plt.show()