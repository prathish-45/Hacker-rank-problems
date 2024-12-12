def timeConservation(s):
    pm = s.endswith("PM")
    am = s.endswith("AM")
    if pm is True:
        if s[:2] == "12":
            return s[:-2]
        else:
            hours = int(s[:2])
            railTime = hours + 12
            pmResult = str(railTime) + s[2:-2]
            return pmResult
    if am is True:
        if s[:2] == "12":
            return "00"+s[2:-2]
        else:
            return s[:-2]
        
if __name__ == '__main__':
    s = input("Enter the time: ")
    result = timeConservation(s)
    print(result)
