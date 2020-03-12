a = 5
b = 2



try:
    print("Resource Opened")
    print(a/b)
    k=int(input("Enter a number"))
    print(k)
# except Exception as err:
#     print("Cannot divide a Number by Zero:", err)

except ZeroDivisionError as err:
    print("Cannot divide a Number by Zero:", err)
except ValueError as err:
    print("Invalid Input Error:", err)
except Exception as err:
    print("Something went wrong:", err)
finally:
    print("Resource Closed")