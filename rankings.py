from game import *
from settings import *

class Rankings():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = DISPLAY_W/2, DISPLAY_H/2

    def show_rankings(self):
        self.game.draw_text("RANKINGS", 50, self.mid_w, DISPLAY_H / 4 - 40)
        texts = self.read_text(HS_FILE)
        while len(texts) < 10:
            texts.append(" ")
        for i in range(10):
            x = DISPLAY_W*1/3+80 if i%2==0 else DISPLAY_W*2/3+80
            y = DISPLAY_H/3+15+50*i/2  if i%2==0 else DISPLAY_H/3+15+50*(i-1)/2
            s = str(i+1) + ". " + texts[i]
            self.game.draw_text_2(s.ljust(18,' '), 22, x, y)
        self.game.draw_text_2("Press BACKSPACE to return", 22, self.mid_w, DISPLAY_H * 3 / 4 + 60)

    def update_hs_file(self, name, score):
        text = name + ' ' + score
        scores = []
        texts = []
        with open(HS_FILE, 'r') as file_to_read:
            while True:
                line = file_to_read.readline()
                if not line:
                    break
                line = line.strip('\n')
                texts.append(line)
        pos = 0
        for item in texts:
            lst = item.split()
            scores.append(int(lst[1]))
        for s in scores:
            if int(score) >= s:
                break
            else:
                pos += 1
                break
        texts.insert(pos, text)
        with open(HS_FILE, 'a') as file_to_change:
            file_to_change.seek(0)	
            file_to_change.truncate()
            for i in range(9):
                file_to_change.write(texts[i]+'\n')
            file_to_change.write(texts[i])

    def read_text(self,root_dir):
        lines = []
        with open(root_dir, 'r') as file_to_read:
            while True:
                line = file_to_read.readline()
                if not line:
                    break
                line = line.strip('\n')
                lines.append(line)
        #print(lines[0].split())
        return lines
