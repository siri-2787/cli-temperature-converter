import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🌡️ CLI Temperature Converter")
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-c", "--celsius", type=float, help="Convert Celsius to Fahrenheit")
    group.add_argument("-f", "--fahrenheit", type=float, help="Convert Fahrenheit to Celsius")

    args = parser.parse_args()

    if args.celsius is not None:
        result = celsius_to_fahrenheit(args.celsius)
        print(f"{args.celsius}°C = {result:.2f}°F")

    elif args.fahrenheit is not None:
        result = fahrenheit_to_celsius(args.fahrenheit)
        print(f"{args.fahrenheit}°F = {result:.2f}°C")
