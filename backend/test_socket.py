import socket

def test_port(host, port):
    print(f"Checking {host}:{port}...")
    try:
        sock = socket.create_connection((host, port), timeout=10)
        print(f"SUCCESS: Reached {host}:{port}")
        sock.close()
    except Exception as e:
        print(f"FAILED: {host}:{port} - {e}")

test_port('smtp.gmail.com', 587)
test_port('smtp.gmail.com', 465)
test_port('smtp.gmail.com', 25)
test_port('google.com', 80)
test_port('google.com', 443)
