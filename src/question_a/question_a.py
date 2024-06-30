#write functions here, don't add input('') statements here!
def test_config():
    return True

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num**0.5)+ 1):
        if num % i == 0:
            return False
        
    return True

