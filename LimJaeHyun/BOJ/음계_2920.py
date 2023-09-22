def sound_of_music(melody):
    answer = ''
    if melody == [1, 2, 3, 4, 5, 6, 7, 8]:
        answer = 'ascending'
    elif melody == [8, 7, 6, 5, 4, 3, 2, 1]:
        answer = 'descending'
    else:
        answer = 'mixed'
    return answer


music = list(map(int, input().split()))
print(sound_of_music(music))
