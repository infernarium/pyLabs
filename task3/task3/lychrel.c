/**
 * floor.c -- программа для расчета нужного этажа
 *
 * Copyright (c) 2021, Tumanyan Mark <tumanyan@cs.karelia.ru>
 *
 * This code is licensed under a MIT-style license.
 */

#include <stdio.h>
#include <limits.h>

/* Выводит все кандидаты в числа Лишрел из отрезка 1, 2, ..., N */
void show_lychrel_candidates(long last_number);

/* Проверяет, является ли заданное число кандидатом в числа Лишрел */
int is_lychrel_candidate(long number);

/* Вычисляет обращение числа */
long reverse(long n);

/* Выводит все кандидаты в числа Лишрел из отрезка 1, 2, ..., N */
void show_lychrel_candidates(long last_number)
{
    long number;

    /* Проверим каждое число в заданном отрезке: */
    for (number = 1; number <= last_number; number++) {
        /* Если оно является кандидатом в числа Лишрел, напечатаем его */
        if (is_lychrel_candidate(number)) {
            printf("%ld\n", number);
        }
    }
}


/* Проверяет, является ли число кандидатом в числа Лишрел */
int is_lychrel_candidate(long number)
{
    long n = number;
    long r = reverse(n);

    if (r < 0)
        return number;

    /* Повторяем ... */
    do {
        /* Если сумма числа и его обращения переполняет разрядную сетку, */
        if ((r == -1) || (n >= LONG_MAX - r)) {
            /* то считаем число искомым кандидатом и завершаем проверку */
            return 1;
        }
        /* иначе вычисляем новое значение, складывая число с обращением */
        n = n + r;

        /* Вычисляем обращение суммы */
        r = reverse(n);

        /* ... пока число не совпадает с обращением */
    } while (n != r);

    /* Считаем, что проверяемое число - не число Лишрел и завершаем проверку */
    return 0;
}


/* Вычисляет обращение числа */
long reverse(long n)
{
    long r = 0;

    do {
        if (r >= (LONG_MAX - n % 10) / 10)
            return -1;
        r = r * 10 + n % 10;
        n /= 10;
    } while (n > 0);

    return r;
}
