def make_sum(hundred, fifty, twenty, ten, five, two, one, quarter, dime):
    sum = hundred * 100 + fifty * 50 + twenty * 20 + ten * 10 + five * 5 + two * 2 + one + quarter * 0.25 + dime * 0.1
    print(sum)
    initial_sum=sum
    currency = {
        "ones": 0,
        "twos":0,
        "fives": 0,
        "tens": 0,
        "twenties":0,
        "fifties": 0,
        "hundreds": 0,
        "quarters": 0,
        "dimes": 0
    }
    
    denominations = {"ones":1, "twos":2, "fives":5, "tens":10, "twenties":20, "fifties":50, "hundreds":100, "quarters":0.25, "dimes":0.1}
    safe_drop_sum = 0
    
    while sum < 190:
        if dime > 0:
            sum += 0.1
            dime -= 1
        elif quarter > 0:
            sum += 0.25
            quarter -= 1
        else:
            break

    while sum > 210:
        if hundred > 0:
            sum -= 100
            hundred -= 1
            currency["hundreds"] += 1
            print("Subtracted 1 hundred")
        if fifty > 0:
            sum -= 50
            fifty -= 1
            currency["fifties"] += 1
            print("Subtracted 1 fifty")
        if twenty > 0:
            sum -= 20
            currency["twenties"] += 1
            twenty -= 1
            print("Subtracted 1 twenty")
        if ten > 0:
            sum -= 10
            ten -= 1
            print("Subtracted 1 ten")
            currency["tens"] += 1
        if five > 0:
            sum -= 5
            five -= 1
            currency["fives"] += 1
            print("Subtracted 1 five")
        if two > 0:
            sum -= 2
            two -= 1
            currency["twos"] += 1
            print("Subtracted 1 two")
        if one > 0:
            sum -= 1
            one -= 1
            currency["ones"] += 1
            print("Subtracted 1 one")
        if quarter > 0:
            sum -= 0.25
            quarter -= 1
            print("Subtracted 1 quarter")
            currency["quarters"] += 1
        if dime > 0:
            sum -= 0.1
            dime -= 1
            currency["dimes"] += 1
            print("Subtracted 1 dime")

    
    for key in currency:
        safe_drop_sum += currency[key]*denominations[key]
    print(safe_drop_sum)
    remaining_counter=initial_sum-safe_drop_sum
    return initial_sum,safe_drop_sum,remaining_counter,currency
