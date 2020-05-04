# ProjectEuler - Problem 700 (Eulercoin)
## Text
> Leonhard Euler was born on 15 April 1707.
>
> Consider the sequence 1504170715041707n mod 4503599627370517.
>
> An element of this sequence is defined to be an Eulercoin if it is strictly smaller than all previously found Eulercoins.
>
> For example, the first term is 1504170715041707 which is the first Eulercoin. The second term is 3008341430083414 which is greater than 1504170715041707 so is not an Eulercoin. However, the third term is 8912517754604 which is small enough to be a new Eulercoin.
>
> The sum of the first 2 Eulercoins is therefore 1513083232796311.
>
> Find the sum of all Eulercoins.

## Solution
Let `N = 1504170715041707`, `M = 4503599627370517` and `Nn = N * n (mod M)`.
With a quick check we can see that `M` is a prime number so there are exactly `M` distinct values `Nn` (one for every `n` in `[0, M-1]`) that are possible Eulercoins. They are way too many to be found with a brute-force attack or, at least, with ONLY a brute-force attack!

The first approach is to find some Eulercoins by brute-force but it is easy to see that from a certain point the search slows down dramatically (around 16-20 Eulercoins). Getting to the 16th Eulercoin (`15806432`) we know that all the other Eulercoins are in the order of at most `10^7` that is significantly less than `M ~ 4.5 * 10^15` so we can stop our brute-force attack on `n` and start analysing only the "tail", from our last Eulercoin down towards 1.

To do so we fix an `Nn` from 1 to the minimum Eulercoin found, `min`, (i.e. `15806432`). Knowing that `Nn = N * n (mod M)`, leads us to `n = Nn / N (mod M)` where the division by `N`, in modular arithmetic, is the product by the modular multiplicative inverse of `N` (found using the Extended Euclidean Algorithm). Every pair `(n, Nn)` found this way will be added to a dictionary. At this point we can order them by ascending `n` values and keep only the `Nn`'s that are smaller than the previous ones.

## Usage
Simply run `eulercoin.py` as a python script:
```
$ python eulercoin.py
```
