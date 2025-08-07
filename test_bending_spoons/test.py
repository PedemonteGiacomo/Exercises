
# Returns the bitwise AND of all elements in X
def and_list(X):
    # Initialize result with the first element
    ris = X[0]
    # Iterate through the rest of the list
    for elem in X[1:]:
        # Apply bitwise AND with the current element
        ris = ris & elem
    # Return the final AND result
    return ris

# Returns the bitwise XOR of all elements in X
def xor_list(X):
    # Initialize result with the first element
    ris = X[0]
    # Iterate through the rest of the list
    for elem in X[1:]:
        # Apply bitwise XOR with the current element
        ris = ris ^ elem
    # Return the final XOR result
    return ris

# find contingous sublists
def contingous_list(X):
    # Helper array to store all contiguous sublists
    support_array = []
    # Loop over all possible sublist lengths
    for length in range(1, len(X)+1):
        # For each length, get all possible starting indices
        for start in range(len(X)-length+1):
            # Slice out the contiguous sublist
            sublist = X[start:start+length]
            support_array.append(sublist)
    print(support_array)  # Debug: print all contiguous sublists
    return support_array

def f(x):
    # Get all contiguous sublists of x
    contigous = contingous_list(x)
    # Compute XOR for each sublist
    xor_results = []
    for elem in contigous:
        xor_result = xor_list(elem)
        xor_results.append(xor_result)
    # Compute AND of all XOR results
    final_result = and_list(xor_results)
    return final_result

def f_eff(X):
    N = len(X)
    # Build prefix XOR array
    prefix_xor = [0] * (N + 1)
    for i in range(N):
        prefix_xor[i + 1] = prefix_xor[i] ^ X[i]
    # Collect XORs of all contiguous sublists
    xor_results = []
    for i in range(N):
        for j in range(i, N):
            xor_val = prefix_xor[j + 1] ^ prefix_xor[i]
            xor_results.append(xor_val)
    # Compute AND of all XOR results
    final_result = and_list(xor_results)
    return final_result

if __name__ == "__main__":
    X = [3, 5, 1]
    print(f"f({X}) = {f_eff(X)}")  # Expected output: 0