import socket
import time

def fuzz(target_ip, target_port, prefix=b"", start_length=100, step=100, max_length=5000):
    buffer = prefix + b"A" * start_length
    
    while len(buffer) <= max_length:
        try:
            print(f"[*] Sending {len(buffer)} bytes...")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((target_ip, target_port))
            s.send(buffer + b"\r\n")
            s.close()
            
            time.sleep(1)
            buffer += b"A" * step
        except Exception as e:
            print(f"[!] Crash bei {len(buffer)} Bytes!")
            print(f"Fehler: {e}")
            break

if __name__ == "__main__":
    target_ip = "192.168.1.100"
    target_port = 9999
    fuzz(target_ip, target_port)
