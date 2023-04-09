# python3

def read_input():
    input_type = input().rstrip()

    if input_type == "I":
        pattern = input().rstrip()
        text = input().rstrip()

    elif input_type == "F":
        with open('./tests/06', 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    else:
        print("input-error")

    return (pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    m, n = len(pattern), len(text)

    if n < m:
        return []

    pattern_hash, text_hash, h = 0, 0, 1
    b = 13
    q = 256
    result = []

    for i in range(m-1):
        h = (h*q) % b

    for i in range(m):
        pattern_hash = (q*pattern_hash + ord(pattern[i])) % b
        text_hash = (q*text_hash + ord(text[i])) % b
    
    for i in range(n-m+1):
        if pattern_hash == text_hash and pattern == text[i:i+m]:
            result.append(i)
        if i < n-m:
            text_hash = (q*(text_hash - ord(text[i])*h) + ord(text[i+m])) % b
            text_hash = (text_hash + b) % b

    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))