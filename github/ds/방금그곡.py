def solution(m, musicinfos):
    answer = '(None)'
    max_time = 0
    dict = {}
    
    for music in musicinfos:
        start, end, name, l = music.split(',')
        # 총시간을 구하고 시간 만큼 노래를 만든다
        # 노래를 dict에 넣고 m과 비교
        h1, m1 = start.split(':')
        start = int(h1) * 60 + int(m1)
        h2, m2 = end.split(':')
        end = int(h2) * 60 + int(m2)
        total_time = end - start
        final = end -start 
        song_time = []
        new_song = []
        # #을 구분해서 배열에 넣기
        
        for k in range(len(l)):
            s = ''
            if l[k].isalpha():
                s += l[k]
                if k+1 <= len(l) - 1:
                    if not l[k+1].isalpha():
                        s+= l[k+1]
                song_time.append(s)
            else:
                continue
        
        #악보로 총 음악 만들기
        idx= 0
        while True:
            if idx == len(song_time):
                idx = 0
            if total_time == 0:
                break
            new_song.append(song_time[idx])
            idx += 1
            total_time -= 1
        
        
        new_m = []
        for k in range(len(m)):
            s = ''
            if m[k].isalpha():
                s += m[k]
                if k+1 <= len(m) - 1:
                    if not m[k+1].isalpha():
                        s+= m[k+1]
                new_m.append(s)
            else:
                continue
        index = 0
        for a in range(len(new_song)):
            if new_song[a] == new_m[index]:
                if new_song[a:a+len(new_m)] == new_m:
                    if final > max_time:
                        answer = name
                        max_time = final
                        break
            else:
                continue
        
        
            
        
        
    
    return answer
    
        
    
    
   