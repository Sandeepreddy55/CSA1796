person(john,'1990, 5, 12').
person(mary,' 1985, 3, 22').
person(bob, '1995, 8, 8').
person(alice, '1980, 11, 17').

get_person(Name,dob):-
    person(Name,dob).
