for i in range(100, 1000):
    for j in range(100, 1000):
        r = i * j
        ri = str(r)[::-1]
        ri = int(ri)
        if r == ri:
            print(f"Achei:{i}*{j}={r}")
