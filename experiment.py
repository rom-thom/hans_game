

def print_palyndroms(ranges):

    
    for i in range(ranges):
        i_str = str(i)

        pal_length = len(str(ranges-1))
        if len(i_str) != pal_length:
            i_str = i_str.zfill(pal_length)
        i_reversed = i_str[::-1]

        if i_reversed == i_str:
            print(i)


        
        


