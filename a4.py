import numpy as np
import pandas as pd



def main():
    nar = np.array([[15,22,43],[33,23,44]])
    pdfr = pd.DataFrame(data = nar, index = ["r1","r2"], columns = ["c1","c2","c3"])

    print(pdfr)








if __name__ == '__main__':
    main()
