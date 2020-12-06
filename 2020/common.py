def read_lines( filename ):
    """
    """
    with open( filename ) as file_handle:
        lines = [ line.strip() for line in file_handle.readlines() ]
    return lines

def read_chunks( filename ):
    """
    """
    lines = read_lines( filename )

    chunks = [ [] ]
    for line in lines + []:
        if len( line ) == 0:
            chunks.append( [] )
        else:
            chunks[ -1 ].append( line )
    
    return [ chunk for chunk in chunks if len( chunk ) > 0 ]

def flatten( list_of_lists ):
    """
    """
    return [ item for sublist in list_of_lists for item in sublist ]