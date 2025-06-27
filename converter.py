import argparse  # Importing argparse for command-line argument handling

# Set up argument parser with description
parser = argparse.ArgumentParser(description="CLI Temperature Converter: Celsius ↔ Fahrenheit")

# Add mutually exclusive arguments so user can provide either -c or -f, not both
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-c", "--celsius", type=float, help="Temperature in Celsius")
group.add_argument("-f", "--fahrenheit", type=float, help="Temperature in Fahrenheit")

# Parse the arguments
args = parser.parse_args()

# If user gave Celsius, convert to Fahrenheit
if args.celsius is not None:
    f = (args.celsius * 9 / 5) + 32
    print(f"{args.celsius}°C = {f:.2f}°F")

# If user gave Fahrenheit, convert to Celsius
else:
    c = (args.fahrenheit - 32) * 5 / 9
    print(f"{args.fahrenheit}°F = {c:.2f}°C")

