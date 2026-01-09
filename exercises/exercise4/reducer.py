# -*- coding: utf-8 -*-
import sys

most_used_payment = None
max_count = 0

current_payment = None
current_count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    this_payment, count = data_mapped

    if current_payment and current_payment == this_payment:
        current_count += int(count)
    else:
        if current_payment:
            if current_count > max_count:
                max_count = current_count
                most_used_payment = current_payment

        current_payment = this_payment
        current_count = int(count)

if current_payment:
    if current_count > max_count:
        max_count = current_count
        most_used_payment = current_payment

if most_used_payment:
    print("El tipo de pago más utilizado es: {0}\tcon {1} usos".format(most_used_payment, max_count))

