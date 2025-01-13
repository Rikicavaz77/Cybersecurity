from collections import Counter

def hex_to_bytes(text):
    return bytes.fromhex(text)

def hex_to_decimal(text):
    return [int(text[i * 2 : (i + 1) * 2], 16) for i in range(len(text) // 2)]
    
def find_key_length(text, key_length=10):
    best_match = 0
    best_key_length = 0
    
    for key_length in range(key_length - 5, key_length + 5 + 1):
        matches = 0
        
        for i in range(len(text) - key_length):
            if text[i] == text[i + key_length]:
                matches += 1
        
        print(f"Number of matches:{matches}")
        print(f"Key length:{key_length}")
        
        if matches > best_match:
            best_match = matches
            best_key_length = key_length
    
    return best_key_length
    
def key_splitter(text, key_length):
    result = []
    
    for i in range(key_length):
        result.append(text[i::key_length])
    
    return result

def char_freq(block):
    freq = Counter(block)
    sorted_freq = sorted(freq.items(), key=lambda c: c[1], reverse=True)
    return sorted_freq

with open('encrypted.txt', 'r') as f:
    cipher_text = f.read()
    
    cipher_bytes = hex_to_bytes(cipher_text)
    
    print(cipher_bytes)
    
    key_length = find_key_length(cipher_bytes)
    
    print(key_length)
    
    cipher_decimal_list = hex_to_decimal(cipher_text)
    
    print(cipher_decimal_list)
    
    block_list = key_splitter(cipher_decimal_list, key_length)
    
    print(block_list)
    
    freq_block_list = []
    for block in block_list:
        freq_block_list.append(char_freq(block))
        
    print(freq_block_list)
    
    single_freq_list = [block[0][0] for block in freq_block_list]
    
    print(single_freq_list)
    
    key = [c ^ ord(' ') for c in single_freq_list]
    
    print(key)
    
    plain_text = ''
    
    for i, c in enumerate(cipher_decimal_list):
        plain_text += chr(c ^ key[i % key_length])
        
    print(plain_text)