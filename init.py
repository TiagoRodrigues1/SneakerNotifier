import svd_caller
import nike_caller

nike = nike_caller.getSneakers()
svd = svd_caller.getSneakers()

nike.extend(svd)

for sneaker in nike:
    print(sneaker)