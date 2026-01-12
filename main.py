from pyscript import display, document


def fever_check(e):
    temp = float(document.getElementById("input1").value)
    
    celsius = (temp - 32) * 5/9

    if celsius >= 37.8:
        display(f'Your temperature is {celsius:.1f}°C. You have a fever', target='output')
    else:
        display(f'Your temperature is {celsius:.1f}°C. You do not have a fever', target='output')