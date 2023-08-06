from django.shortcuts import render


# Create your views here.


def calculate(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    m = len(s1)
    n = len(s2)
    x = 0
    for letter in s1:
        if letter in s2:
            s2 = s2.replace(letter, '', 1)
            x = x + 1

    count = m + n - 2 * x

    f = ['F', 'L', 'A', 'M', 'E', 'S']

    ind = 0

    while len(f) > 1:
        remaining_letters_count = len(f)
        steps = count % remaining_letters_count
        steps = remaining_letters_count if steps == 0 else steps
        ind = ind + steps - 1
        ind = ind % remaining_letters_count
        f.pop(ind)

    return f[0]


def home(request):
    return render(request, 'home.html')


def response(request):
    if request.method == 'POST':
        name1 = request.POST['name1']
        name2 = request.POST['name2']

        result = calculate(name1, name2)
        relation = ''
        if result == 'F':
            relation = 'Friendship'
        elif result == 'L':
            relation = 'Love'
        elif result == 'A':
            relation = 'Attraction'
        elif result == 'M':
            relation = 'Marriage'
        elif result == 'E':
            relation = 'Enemy'
        else:
            relation = 'Sister'
        return render(request, 'home.html', {'relation': relation, 'name1': name1, 'name2': name2, 'flag': True})
