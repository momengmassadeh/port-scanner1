import socket

def scan_ports(target, port_range=(1, 1024)):
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("❌ خطأ: تعذر الوصول إلى العنوان. تأكد من صحة اسم الموقع أو IP.")
        return

    print(f"\n🔍 الفحص جاري على: {target} ({ip})\n")

    open_ports = []

    for port in range(port_range[0], port_range[1] + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print(f"✅ المنفذ {port} مفتوح")
                open_ports.append(port)
            sock.close()
        except socket.error:
            continue

    if not open_ports:
        print("\n❌ لم يتم العثور على أي منفذ مفتوح.")
    else:
        print(f"\n📊 المنافذ المفتوحة: {open_ports}")

if __name__ == "__main__":
    print("🌐 برنامج فحص المنافذ المفتوحة")
    target_host = input("🖥️ أدخل اسم الموقع أو عنوان IP: ").strip()

    if target_host == "":
        print("⚠️ لم يتم إدخال أي عنوان.")
    else:
        scan_ports(target_host)
