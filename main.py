# Mutables - Aniadir - Quitar o modificar elementos
# Regla de indice(0)
        #   -4        -3        -2      -1
        #    0         1         2       3
courses = ['Python', 'Numpy', 'Pandas', 'Dash', ]

courses[0] = 'Python v3'

courses.append('Rails')
courses.append('Livewire')

courses[-1] = 'Curso profesional de livewire'

courses.remove('Numpy')

print(courses)


# Strings, Enteros, Flotantes, Booleanos & Tuplas

settings = (3306, 'localhost', 'user', 'password')

user = { 
        'name' : 'Cody', 
        'age': 10, 
        'password' : 'password123'
}

contact = { 
        'email': 'info@codigofacilito.com',
        'phonenumber' : '123456789',

}

numbers =  ['a', 'adrian', 'cody', 'a', 'cody']

uniques = set(numbers)
uniques = list(uniques)

uniques.sort(reverse=True)
print(uniques)