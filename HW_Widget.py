import tkinter as tk

def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        product = num1 * num2
        result_label.config(text=f"Product: {product}")
    except ValueError:
        result_label.config(text="Error: Invalid input. Please enter numbers.")

root = tk.Tk()
root.title("Getting Started with Widgets: Product Calculator")

lbl= tk.Label(text= "Welcome to the product calculator, this program multiplies any two numbers inputed by the user!")
lbl.pack()
label1 = tk.Label(root, text="Enter first number:",bg= "#1854e0", fg= 'white')
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:", bg= "#ee9e12", fg= 'white')
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

calculate_button = tk.Button(root, text="Calculate Product", command=calculate_product)
calculate_button.pack()

result_label = tk.Label(root, text="Product: ")
result_label.pack()

root.mainloop()
#I had to use google's help for some of this due to consistently getting an attribute error