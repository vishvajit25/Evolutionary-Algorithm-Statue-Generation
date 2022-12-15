def generate_rgbaRo(seed):
    random.seed(seed)
    
    # Randomly generate R,G,B,A and Roughness Factor
    R=random.randint(0,255) #Red
    G=random.randint(0,255) #Green
    B=random.randint(0,255) #Blue
    A=random.uniform(0,1)   #Alpha (Opacity)
    RoughnessFactor=random.uniform(0,1)
    
    return R,G,B,A,RoughnessFactor
