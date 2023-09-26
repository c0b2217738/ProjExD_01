import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01-20230926/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    tori_img = pg.image.load("ex01-20230926/fig/3.png")
    tori_img = pg.transform.flip(tori_img, True, False)
    tori_img2 = pg.transform.rotozoom(tori_img, -1, 1.0)
    #tori_imgs = [tori_img, tori_img2] 練習問題5
    tmr = 0
    count = 0
    n = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        if count%2 == 0:
            n += 1
        else:
            n -= 1
        if n%20 == 1:
            count += 1
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        #screen.blit(tori_imgs[tmr%5], [300,200]) 練習問題5
        tori_img3 = pg.transform.rotozoom(tori_img, -n, 1.0)
        screen.blit(tori_img3, [300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()