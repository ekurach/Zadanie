import matplotlib.pyplot as plt # library with plots


def makeplot():
    x_axis = input('Enter x axis values: ') #user can input x axis values (but it return them as a string)
    y_axis = input('Enter y axis values: ') #user can input y axis values (but it return them as a string)
    
    try:    #catching exception when user didnt put number but str type ect
    
        x_numbers=list(map(int, x_axis.split()))    #adding numbers separated by spaces and retuning it as a list
        y_numbers=list(map(int, y_axis.split()))    #adding numbers separated by spaces and retuning it as a list

    except ValueError:
        print("Invalid number \n")
        return makeplot()#starting again
        
    if len(x_numbers)!=len(y_numbers): #checking if numbers of entered values are the same (they have to be, because they create points on the plot) 
        print('number of values in x axis and y axis must be the same, try again \n') 
        return makeplot() #starting again
        
    

    print(x_numbers) #displaying entered numbers (optional)
    print(y_numbers)
    
    plt.plot(x_numbers, y_numbers, 'ro') # plot with points
    
    product=0 
    sum_x=0
    sum_y=0
    power_x=0 
        
    for var_x, var_y in zip(x_numbers, y_numbers): #getting  single variables from lists
        product += var_x*var_y  # giving us Σ(X⋅Y) - a part of Least squares pattern
        sum_x+=var_x  #Sum of variables x
        sum_y+=var_y  #Sum of variables y
        power_x +=var_x*var_x #sum of powers of x
        
    
    avg_x=sum_x/len(x_numbers)  #Average for variable x 
    avg_y=sum_y/len(y_numbers)  #Average for variable y
    b=(product-len(x_numbers)*avg_x*avg_y)/(power_x-(len(x_numbers)*avg_x*avg_x))# part of Least squares pattern: Y=b*x+a 
   
    a=avg_y-b*avg_x # part of Least squares pattern: Y=b*x+a 
    x=[a for a in x_numbers] #for the plot
    function=[(b*x+a)for x in x_numbers] #least squares function created for entered values
    plt.plot(x, function, 'b') #adding implemented least squares function to the plot
    plt.show() #showing created plot
    
    cont=input("Press '0' to continue or anything else to exit: ") #press '0' to create another plot
    if cont=='0':
        return makeplot()
    else:
        pass
   
makeplot()
