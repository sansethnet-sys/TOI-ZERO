st = "capricorn,aquarius,pisces,aries,taurus,gemini".split(',')
st += ["cancer","leo","virgo","libra","scorpio","sagittarius"]
pt = [22,20,19,21,20,21,22,23,23,23,24,22]
D , M = int(input()) , int(input())-1
print(st[(D//pt[M]+M)%12])