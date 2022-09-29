
def soma(n1: int,n2: int) -> int:
    try:
        n1=int(n1)
        n2=int(n2)
        assert isinstance(n1,int)
        assert isinstance(n2,int)
    except ValueError:
        print("Não foi possível converter")
        
    return(n1+n2)
