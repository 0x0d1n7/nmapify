import subprocess
from datetime import datetime

# ASCII art logo
logo = '''
███╗░░██╗███╗░░░███╗░█████╗░██████╗░██╗███████╗██╗░░░██╗
████╗░██║████╗░████║██╔══██╗██╔══██╗██║██╔════╝╚██╗░██╔╝
██╔██╗██║██╔████╔██║███████║██████╔╝██║█████╗░░░╚████╔╝░
██║╚████║██║╚██╔╝██║██╔══██║██╔═══╝░██║██╔══╝░░░░╚██╔╝░░
██║░╚███║██║░╚═╝░██║██║░░██║██║░░░░░██║██║░░░░░░░░██║░░░
╚═╝░░╚══╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░░░░╚═╝░░░
'''

# Nmap options with explanations
options = [
    ("-sS", "TCP SYN scan (stealthy)"),
    ("-sT", "TCP connect scan"),
    ("-sU", "UDP scan"),
    ("-A", "Enable OS detection, version detection, script scanning, and traceroute"),
    ("-O", "Enable OS detection"),
    ("-v", "Increase verbosity level"),
    ("-T0", "Paranoid timing template"),
    ("-T1", "Sneaky timing template"),
    ("-T2", "Polite timing template"),
    ("-T3", "Normal timing template"),
    ("-T4", "Aggressive timing template"),
    ("-T5", "Insane timing template"),
    ("-p", "Specify port(s) to scan"),
    ("-n", "Disable DNS resolution"),
    ("-oX", "Output results in XML format"),
    ("-oN", "Output results in normal format"),
    ("-oG", "Output results in grepable format"),
    ("-iL", "Read targets from a file"),
    ("--script", "Execute Nmap scripts")
]

# Print the ASCII art logo and credits
print(logo)
print("Made by 0x0d1n7\n")

# Read user input for the target IP address
target_ip = input("Enter the target IP address: ")

# Print the list of available options
print("Select scan options (comma-separated):")
for index, (option, description) in enumerate(options, start=1):
    print(f"{index}. {option} - {description}")

# Read user input for the selected options
selected_options = input("Enter the selected options (comma-separated): ")

# Construct the Nmap command
command = ["nmap"]
command.extend(selected_options.split(","))
command.append(target_ip)

# Generate the output file name
output_file = f"{target_ip}-{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"

try:
    # Run the Nmap command and save the output to a file
    result = subprocess.run(command, check=True, capture_output=True)
    with open(output_file, "wb") as file:
        file.write(result.stdout)
    print(f"Scan completed successfully. Results saved to {output_file}")

except subprocess.CalledProcessError as e:
    print(f"Error: {e}")

