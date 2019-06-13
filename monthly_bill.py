def calculation(heat, electric):

    internet = 25
    jonah_total = electric + internet
    hannah_total = heat

    total_all_together = jonah_total + hannah_total
    total_per_individual = total_all_together / 3

    hannah_owed = hannah_total - total_per_individual 
    jonah_owed = jonah_total - total_per_individual

    if hannah_owed < 0:
        hannah_pays = -1 * hannah_owed
        jonah_is_payed = total_per_individual + hannah_pays
        return 'Jonah is payed ${0}'.format(jonah_is_payed)

    elif jonah_owed < 0:
        jonah_pays = -1 * jonah_owed
        hannah_is_payed = total_per_individual + jonah_pays
        return 'Hannah is payed ${0}'.format(hannah_is_payed)
    
    phillip_pays_hannah = total_per_individual - jonah_owed
    phillip_pays_jonah = total_per_individual - hannah_owed
    return'Phillip pays Hannah ${0} and pays Jonah ${1}'.format(phillip_pays_hannah, phillip_pays_jonah)

def main():

    print(calculation(33,27))

main()
    


    
