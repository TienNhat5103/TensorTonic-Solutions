def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    n = len(tokens)
    chunks = []
    i = 0
    while i<n:
        if i + chunk_size < n:
            chunks.append(tokens[i:i+chunk_size])
            i = i + chunk_size - overlap
        else: 
            chunks.append(tokens[i:n])
            break
    
    return chunks
        