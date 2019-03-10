import numpy as np
import random
import pandas as pd


def LyricsGenerator():


    data_loc = "/home/shivansh/Downloads/songdata.csv"
    songfile = pd.read_csv(data_loc)

    #Initializing variable to lyrics in the dataset

    p=""
    for i in songfile.text:
        p+=i

    data = p


    T = {}

    # define order of the Markov chain
    order = 8

    for ix in range(len(data)-order):
        # get the current context
        ctx = data[ix:ix+order]
        
        # get the future val
        future_val = data[ix+order]
        
        # check if the context exists
        if T.get(ctx) is None:
            T[ctx] = {}
            T[ctx][future_val] = 1
        else:
            # check if the future_val key exists
            if T[ctx].get(future_val) is None:
                T[ctx][future_val] = 1
            else:
                T[ctx][future_val] += 1

    for kx in T.keys():
        s = float(sum(T[kx].values()))
    
        for k in T[kx].keys():
            T[kx][k] = T[kx][k]/s

    
    # defines exponential probabilities
    def temp_sample(probs, temp=1.0):
        probs = np.asarray(probs)
        
        exp_probs = np.exp(np.log(probs) / temp)
        
        return list(exp_probs / exp_probs.sum())

    def generate_next(ctx, diversity=1.0):
        r = np.random.random()
        
        possible = T.get(ctx)
        if possible is None:
            return ' '
        diverse_probs = temp_sample(list(possible.values()),temp=diversity)
            
        return np.random.choice(list(possible.keys()),p = diverse_probs)

    ind = int(np.random.random()*(len(data)-order))
    initial_state = data[ind:ind+order]
    ctx = initial_state

    sentence = '' + ctx

    for ix in range(1000):
        nxt = generate_next(ctx, diversity=1.5)
        sentence += nxt
        ctx = sentence[-order:]

    f = open('/home/shivansh/Downloads/lyrics.txt','w')
    f.write(sentence)
    f.close()

    return sentence
























