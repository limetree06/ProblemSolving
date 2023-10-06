def solution(nums):
    pokemon = dict()
    N = len(nums) // 2
    for i in nums:
        if i in pokemon.keys() :
            pokemon[i] = pokemon[i]+1
        else:
            pokemon[i] = 1
    
    key_len = len(pokemon.keys())
    if key_len > N:
        return N
    else:
        return key_len