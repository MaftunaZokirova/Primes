class PrimeNumbers: # class
    def __init__(self) -> None: 
        print( "Program is running")
        self.prime_list = [] 
        self.CountPrimes() 
        print(self.prime_list)
        print("Program is ending") 
        

    def CountPrimes(self) -> None:
        i = 2 
        while len(self.prime_list) < 10:
            print(self.prime_list)
            if len(self.prime_list) == 0:
                self.prime_list.append(i)     
            else:
                is_prime = True
                for k in range(len(self.prime_list)):
                    if i % self.prime_list[k] == 0:
                        is_prime = False
                        break
                if is_prime:
                    self.prime_list.append(i)    
            i += 1
           


if __name__ == '__main__': 
 prime_num = PrimeNumbers()
