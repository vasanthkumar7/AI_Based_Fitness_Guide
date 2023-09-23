excersice4_url="https://www.youtube.com/watch?v=l4kQd9eWclE&ab_channel=Howcast"
openlinks(excersice4_url)
excersice1=Frame(root,bg="black")
jj1=mainImageFunction(1.5,"pics/excersice1.png")
excersice1Pic=Label(excersice1,image=jj1,bg="black")
excersice1Pic.grid(row=0,column=0)

messagebox.showinfo("Information", "Calories burned: "+str(round(calburned,2)))