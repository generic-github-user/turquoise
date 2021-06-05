def tetration(n, m):
    r = n
#     m must be an integer
    m = int(m)
#     Repeatedly raise initial value to the previously computed power (e.g., 2 -> 2^2 -> 2^(2^2) -> ...)
    for i in range(m):
        r = n ** r
    return r
tetration.info = "This function handles Turquoise's tetration functionality, which uses the ^^ operator; it is generally impractical due to extremely rapid increases in the function's output as n and m grow, but is included for completeness."

tetration(1.6, 6)