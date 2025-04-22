import tkinter as tk  


class EraserApp:  
    def __init__(self, root, rows=10, cols=10, cell_size=40):  
        self.root = root  
        self.rows = rows  
        self.cols = cols  
        self.cell_size = cell_size  
        self.is_dragging = False  
        
        
        self.canvas = tk.Canvas(root, width=cols*cell_size, height=rows*cell_size, bg='white')  
        self.canvas.pack()  

        
        self.cells = {}  
        for row in range(rows):  
            for col in range(cols):  
                x1 = col * cell_size  
                y1 = row * cell_size  
                x2 = x1 + cell_size  
                y2 = y1 + cell_size  
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue', outline='black')  
                self.cells[cell] = (row, col)  

       
        self.eraser_size = 80  
        self.eraser_rectangle = self.canvas.create_rectangle(0, 0, self.eraser_size, self.eraser_size, fill='red', outline='black')  
        
       
        self.canvas.bind("<ButtonPress-1>", self.start_drag)  
        self.canvas.bind("<B1-Motion>", self.drag_eraser)  
        self.canvas.bind("<ButtonRelease-1>", self.stop_drag)  

    def start_drag(self, event):  
        """Start dragging the eraser."""  
        self.is_dragging = True  
        self.update_eraser_position(event.x, event.y)  

    def drag_eraser(self, event):  
        """Move the eraser and erase cells."""  
        if self.is_dragging:  
            self.update_eraser_position(event.x, event.y)  
            self.erase_cells()  

    def stop_drag(self, event):  
        """Stop dragging the eraser."""  
        self.is_dragging = False  

    def update_eraser_position(self, x, y):  
        """Update the position of the eraser rectangle."""  
        x1 = x - self.eraser_size / 2  
        y1 = y - self.eraser_size / 2  
        x2 = x1 + self.eraser_size  
        y2 = y1 + self.eraser_size  
        self.canvas.coords(self.eraser_rectangle, x1, y1, x2, y2)  

    def erase_cells(self):  
        """Erase the cells that intersect with the eraser."""  
        eraser_coords = self.canvas.coords(self.eraser_rectangle)  
        for cell in self.cells.keys():  
            cell_coords = self.canvas.coords(cell)  
           
            if (eraser_coords[2] > cell_coords[0] and  
                eraser_coords[0] < cell_coords[2] and  
                eraser_coords[3] > cell_coords[1] and   
                eraser_coords[1] < cell_coords[3]):      
                self.canvas.itemconfig(cell, fill='white')  


if __name__ == "__main__":  
    root = tk.Tk()  
    root.title("Eraser on Canvas")  
    app = EraserApp(root)  
    root.mainloop()  
















    