def calculate_rectangle_area(length, width):
    """
    Calculates the area of a rectangle given its length and width.
    
    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    
    Returns:
        float: The area of the rectangle.
    """
    area = length * width
    return area

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    area = calculate_rectangle_area(length, width)
    
    print("The area of the rectangle is:", area)

if __name__ == "__main__":
    main()