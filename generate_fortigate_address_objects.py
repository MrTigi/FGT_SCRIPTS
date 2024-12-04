import os

def generate_fortigate_objects(input_file, output_file=None):
    """
    Reads a file of IP addresses and generates FortiGate address objects configuration.

    Args:
        input_file (str): Path to the file containing IP addresses.
        output_file (str, optional): Path to save the generated configuration.
    """
    try:
        with open(input_file, 'r') as infile:
            ip_addresses = [line.strip() for line in infile if line.strip()]
        
        config_lines = []
        for i, ip in enumerate(ip_addresses):
            obj_name = f"h_{ip}"  # Unique name for each object
            config_lines.append(
                f"config firewall address\n"
                f"    edit \"{obj_name}\"\n"
                f"        set subnet {ip} 255.255.255.255\n"
                f"    next\n"
                f"end\n"
            )
        
        config_output = "\n".join(config_lines)
        
        if output_file:
            with open(output_file, 'w') as outfile:
                outfile.write(config_output)
            print(f"Configuration saved to {output_file}")
        else:
            print("Generated FortiGate Configuration:")
            print(config_output)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Change these paths as needed
    input_file_path = "/Users/*****/Desktop/Scripts/input.txt"  # Replace with your input file name
    output_file_path = "/Users/*****/Desktop/Scripts/fortigate_address_config.txt"  # Replace with desired output file name
    
    # Run the script
    generate_fortigate_objects(input_file_path, output_file_path)
