from hash_map import hash_m


if __name__ == "__main__":
     number = [
        ('1', 'one'),
        ('2', 'two'),
        ('3', 'three'),
        ('4', 'four')
    ]
hashtable = hash_m(number)
print('\n All numbers \n')
print(hashtable)
print(f"1 {hashtable.give_value('1')}")