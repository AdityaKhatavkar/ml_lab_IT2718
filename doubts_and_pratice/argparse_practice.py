import argparse
import sys

def do_operation(n1, n2, method):
    if method == "add":
        return (n1 + n2)
    
    elif method == "subtract":
        return (n1 - n2)

    elif method == "multiply":
        return (n1 * n2)

    elif method == "divide":
        if n2 == 0:
            raise ValueError("Denomination cannot be 0")
        
        return (n1/ n2)

    elif method == "modulo":
        if n2 == 0:
            raise ValueError("Denomination cannot be 0")
        
        return (n1%n2)
    else:
        raise ValueError(f"Unknown operation: {method}. Valid operations: add, subtract, multiply, divide, modulo")
    
def main():

    parser = argparse.ArgumentParser()

    # this is how we add the arguments
    parser.add_argument("number1", help = "first_number") # positional argumengt
    parser.add_argument("number2", help = "second_number") # positional argument
    parser.add_argument("operation", help = "operation") # positional argument
    parser.add_argument("--message", help = "any message u wanna enter") # optional argument '--' as prefix

    # once we pass the argument we get 'parser.parse_args()' object back which has the value of args which user has pass from the command line 
    try : 
        args = parser.parse_args()

        # printing the arguments
        print("First Number :  ", args.number1 )
        print("Second Number :  ", args.number2)
        print("Operation :  ", args.operation )
        print("message : ", args.message)

    # whenever we pass the argument using command line, it is in the format of string. So we need to convert into the desire data type
        num1 = int(args.number1)
        num2 = int(args.number2)
        op = str.lower(args.operation)  # op = args.operation.lower()
        result = do_operation(num1, num2, op)
        print("Result :", result)

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__" : 
    main()