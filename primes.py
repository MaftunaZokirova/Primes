class PrimeNumbers: # class
    def __init__(self) -> None: # ALWAYS this is called default constructor.after creating a class this is coming as default thing
        print( "Program is running")
        self.prime_list = [] #when var is part of class in python we write before self
        self.CountPrimes() # function name to maintain neat 
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
            # when u write word pass when u do not know your code to come here where u dont knpw how to write thisfunction





if __name__ == '__main__': # in python how main looks like
 prime_num = PrimeNumbers()