### Title
Convolutional Sequence to Sequence Leaarning

### Authors
Jonas Gehring, Michael Auli, David Grangier, Denis Yarats, Yann N. Dauphin

### link
[Arxiv](http://arxiv.org/abs/1003.0146)

### Contents
- A Convolutional Architecture
    1. Position Embeddings
        - input element: **x** = (x_1, x_2, .., x_m)
        - distributional space **w** = (w_1, ..., w_m), w_i is f dimension vector
        - Embedding matrix D (V*f dim)
        - position  **p** = (p_1, ..., p_m), p_i is f dimension vector transformed from its absolute position
        - input **e** = (w_1 + p+1, ..., w_m + p_m)
    1. Convolutional Block Structure 
        - $\frac{n!}{k!(n-k)!} = {n \choose k}$