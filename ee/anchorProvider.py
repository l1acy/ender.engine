# from pygame import Surface

# type crd = tuple[int, int]

# class AnchorProvider:
#     def c(x: int, y: int, screen: Surface) -> crd:
#         cx, cy = screen.get_size()

#         return (cx + x, cy + y)
    
#     def lu(x: int, y: int, screen: Surface) -> crd:
#         return (x, y)
    
#     def lc(x: int, y: int, screen: Surface) -> crd:
#         cy = screen.get_height() / 2

#         return (x, cy + y)
    
#     def ld(x: int, y: int, screen: Surface) -> crd:
#         height = screen.get_height()

#         return (x, height - y)
