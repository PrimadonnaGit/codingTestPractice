from datetime import datetime


def solution(m, musicinfos):
    answer_list = []
    ml = {"C#": 0, "D#": 1, "F#": 2, "G#": 3, "A#": 4}
    for l in ml:
        m = m.replace(l, str(ml[l]))

    for i, music in enumerate(musicinfos):
        st, et, name, play = music.split(',')
        for l in ml:
            play = play.replace(l, str(ml[l]))
        music_play_time = len(play)
        play_time = (datetime.strptime(et, '%H:%M') - datetime.strptime(st, '%H:%M')).seconds // 60
        real_play = ''
        for i in range(play_time):
            real_play += play[i % music_play_time]

        if m in real_play:
            answer_list.append((name, play_time, i))

    if answer_list:
        answer_list.sort(key=lambda music: (music[1], -i), reverse=True)
        return answer_list[0][0]
    else:
        return "(None)"


if __name__ == '__main__':
    m = "ABCDEFG"
    musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    assert solution(m, musicinfos) == "HELLO"
    m = "CC#BCC#BCC#BCC#B"
    musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
    assert solution(m, musicinfos) == "FOO"
    m = "ABC"
    musicinfos = ["12:00,14:00,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
    assert solution(m, musicinfos) == "WORLD"
