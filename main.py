import subprocess
import sys
import os

def select_ovpn_file(directory="Path/to/this_dir"):
    files = [f for f in os.listdir(directory) if f.endswith('.ovpn')]
    if not files:
        print(f"No .ovpn files found in directory: {directory}")
        sys.exit(1)
    print("Available .ovpn files:")
    for i, file in enumerate(files):
        print(f"{i + 1}: {file}")
    choice = int(input("Select a file by number: ")) - 1
    if choice < 0 or choice >= len(files):
        print("Invalid selection")
        sys.exit(1)
    return files[choice]

ovpn_config_file = "/Path/to/this_dir/{}".format(select_ovpn_file())
def connect_vpn():
    if not os.path.exists(ovpn_config_file):
        print(f"Error: The OpenVPN config file does not exist: {ovpn_config_file}")
        sys.exit(1)
    try:
        print("Connecting to VPN...")
        with open("/tmp/vpn_credentials.txt", "w") as cred_file:
            cred_file.write("vpnbook\nzm396a4\n")
        subprocess.run(["sudo", "openvpn", "--config", ovpn_config_file, "--auth-user-pass", "/tmp/vpn_credentials.txt"], check=True)
        os.remove("/tmp/vpn_credentials.txt")
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to VPN: {e}")
        sys.exit(1)

if __name__ == "__main__":
    connect_vpn()
