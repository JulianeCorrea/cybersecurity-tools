import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    """Verifica se uma porta específica está aberta"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Porta {port} aberta ✅")
    except:
        pass

if __name__ == "__main__":
    print("=== Scanner de Portas ===")
    host = input("Digite o IP ou hostname: ")
    ports = [21, 22, 80, 443, 3389, 8080]  # Portas comuns
    
    print(f"\nScanning {host}...")
    with ThreadPoolExecutor(max_workers=50) as executor:  # Scanner paralelo
        executor.map(lambda port: scan_port(host, port), ports)