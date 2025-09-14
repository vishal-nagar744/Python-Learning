def multiplication_table(number, upto=10):
    print(f"\nMultiplication Table for {number}\n")
    for i in range(1, upto + 1):
        print(f"{number} x {i} = {number * i}")


#Exmaple usage 
if __name__ == "__main__":
    num = int(input("Enter a number to generate its multiplication table: "))     
    limit = int(input("Enter the limit up to which you want the table (default is 10): ") or 10)
    multiplication_table(num, limit)   