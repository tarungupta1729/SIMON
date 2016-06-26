import pygame
import random
import time
pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("simon")
crash_sound = pygame.mixer.music.load("Crash.mp3")

white = (0,0,202)
#white = (255,255,255)
black = (8,8,8)
RED = (255,0,0)
new = (250,31,86)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
bright_yellow = (150,150,0)
bright_blue = (0,0,150)
bright_green = (0,150,0)
bright_red = (150,0,0)
#bgcolor = (0,128,255)
bgcolor= (37,72,153)
pause = False
def quitgame():
	pygame.quit()
	quit()
def drawbutton():
	pygame.draw.rect(gameDisplay,bright_yellow,(150,100,175,175))
	pygame.draw.rect(gameDisplay,bright_blue,(345,100,175,175))
	pygame.draw.rect(gameDisplay,bright_red,(150,295,175,175))
	pygame.draw.rect(gameDisplay,bright_green,(345,295,175,175))
def drawsibutton(color):
	#print(1)
	if color == YELLOW:
		pygame.draw.rect(gameDisplay,color,(150,100,175,175))
	elif color == BLUE:
		pygame.draw.rect(gameDisplay,color,(345,100,175,175))
	elif color == RED:
		pygame.draw.rect(gameDisplay,color,(150,295,175,175))
	elif color == GREEN:
		pygame.draw.rect(gameDisplay,color,(345,295,175,175))
		
def text_objects(text,font):
	textsurface = font.render(text,True,black)
	return textsurface,textsurface.get_rect()
def button(text,x,y,w,h,ic,ac,action=None):
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	if x+w>mouse[0]>x-w and y+w>mouse[1]>y-w:
		pygame.draw.circle(gameDisplay,ic,(x+h,y),w,0)
		pygame.draw.circle(gameDisplay,black,(x+h,y),w+2,3)
		if click[0]==1 and action!=None:
			action()
	else:
		pygame.draw.circle(gameDisplay,ac,(x+h,y),w,0)
		pygame.draw.circle(gameDisplay,black,(x+h,y),w+2,3)
	smallText = pygame.font.SysFont("broadway",25)
	textSurf,textRect = text_objects(text,smallText)
	textRect.center  = (x+h,y)
	gameDisplay.blit(textSurf,textRect)
def control():
	cont = True
	clock = pygame.time.Clock()
	while cont:
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				quitgame()
		gameDisplay.fill(bgcolor)
		lt = pygame.font.SysFont('cooperblack',45)
		ttSurf,ttRect = text_objects("Controls: Play with Q,W,A,S",lt)
		ttRect.center = (400,300)
		gameDisplay.blit(ttSurf,ttRect)
		pygame.display.update()
		pygame.time.wait(1000)
		cont = False
		game_loop()
def game_intro():
	intro = True
	clock = pygame.time.Clock()
	while intro:
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				quitgame()
		gameDisplay.fill(bgcolor)
		largetext=pygame.font.SysFont('cooperblack',65)
		TextSurf,TextRect = text_objects("SIMON",largetext)
		TextRect.center = (400,100)
		gameDisplay.blit(TextSurf,TextRect)
		
		
		button("PLAY",150,450,100,50,GREEN,bright_green,control)
		button("QUIT",550,450,100,50,RED,bright_red,quitgame)
		
		
		pygame.display.update()
		clock.tick(15)
def unpause():
	global pause 
	pause = False
def yourscore(score):
	temp = pygame.font.SysFont("comicsansms",25)
	t1 = temp.render("Your Score is " + str(score),True,black)
	gameDisplay.blit(t1,(300,400))
def crash(score):
	pygame.mixer.music.play()
	time.sleep(2)
	pygame.mixer.music.stop()
	#pygame.mixer.music.play(crash_sound)
	gameDisplay.fill(bgcolor)
	te = pygame.font.SysFont("comicsansms",75)
	teSurf,teRect = text_objects("YOU LOOSE!",te)
	teRect.center = (400,300)
	gameDisplay.blit(teSurf,teRect)
	yourscore(score)
	pygame.display.update()
	time.sleep(2)
	game_intro()
def displayscore(score):
	font = pygame.font.SysFont("comicsansms",25)
	text = font.render("Score is : " + str(score),True,BLUE)
	gameDisplay.blit(text,(650,0))
def paused():
	clock = pygame.time.Clock()
	while pause:
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				quitgame()
		
		gameDisplay.fill(bgcolor)
		largeText = pygame.font.SysFont("cooperblack",100)
		TextSurf,TextRect = text_objects("Game Paused",largeText)
		TextRect.center = (400,100)
		gameDisplay.blit(TextSurf,TextRect)
		
		button("CONTINUE",150,450,100,30,GREEN,bright_green,unpause)
		button("QUIT",550,450,100,30,RED,bright_red,quitgame)
		
		pygame.display.update()
		clock.tick(15)
	
def game_loop():
	global pause,pattern,index,waitinginput,play
	clock = pygame.time.Clock()
	play = True
	index = 0
	pattern = []
	waitinginput = False
	score = 0
	while play:
		clicked = None
		gameDisplay.fill(black)
		drawbutton()
		displayscore(score)
		pygame.display.update()
		clock.tick(60)
		
		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				quitgame()
			if(event.type == pygame.KEYDOWN):
				if(event.key == pygame.K_q):
					clicked = YELLOW
				elif(event.key == pygame.K_w):
					clicked = BLUE
				elif(event.key == pygame.K_a):
					clicked = RED
				elif(event.key == pygame.K_s):
					clicked = GREEN
				if(event.key == pygame.K_p):
					pause = True	
					paused()
				
		if not waitinginput:
			#pygame.display.update()
			pygame.time.wait(1000)
			pattern.append(random.choice((YELLOW,BLUE,RED,GREEN)))
			#origsurf = gameDisplay.copy()
			for button in pattern:
				#print (button)
				drawsibutton(button)
				pygame.display.update()
				pygame.time.wait(500)
				drawbutton()
				pygame.display.update()
				pygame.time.wait(500)
				#gameDisplay.blit(origsurf,(0,0))
			
			waitinginput = True
		else:
			if clicked and clicked == pattern[index]:
				drawsibutton(clicked)
				pygame.display.update()
				pygame.time.wait(200)
				index+=1
				if index == len(pattern):
					score+=1
					waitinginput = False
					index =0 
			elif clicked and clicked!= pattern[index]:
				crash(score)
				
game_intro()
game_loop();
quitgame()