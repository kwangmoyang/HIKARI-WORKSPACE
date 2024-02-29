import random
import pygame
###########################################################
###########################################################

# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() #초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("HIKARI Game") #게임이름

# 화면배경 이미지 설정
background = pygame.image.load("C:/Users/User/Desktop/개인/pythonWorkspace/pygame_basic/game_background.png")

# FPS
clock = pygame.time.Clock()

# 폰트 정의 (폰트, 크기)
game_font = pygame.font.Font(None, 40)

# 게임 점수 설정
character_score = 0

###########################################################
###########################################################

# 1. 사용자 게임 초기화 (게임 이미지, 좌표,속도, 폰트 등)


# 캐릭터 1 설정
character = pygame.image.load("C:/Users/User/Desktop/개인/pythonWorkspace/pygame_basic/sinnoske.png")
character_size = character.get_rect().size  # 이미지 크기 구해오기
character_width = character_size[0]         # 캐릭터  가로
character_height = character_size[1]        # 캐릭터  세로

# 위치조정 
character_x_pos = (screen_width / 2) - (character_width / 2) # 화면 가로의 절반 크기
character_y_pos = screen_height - character_height           # 화면 세로 크기 가장 아래에 

# 이동속도
character_speed = 0.6

# 이동할 좌표
to_x = 0
to_y = 0
############################################################################################################
############################################################################################################
# 떨어지는 물체 설정
enemy = pygame.image.load("C:/Users/User/Desktop/개인/pythonWorkspace/pygame_basic/attacker.png")
enemy_size   = enemy.get_rect().size  # 물체 이미지 사이즈 가져오기
enemy_width  = enemy_size[0]         # 가로 크기
enemy_height = enemy_size[1]        # 세로 크기

# 위치조정 
enemy_x_pos = random.randint(0, screen_width - enemy_width) #랜덤 값
enemy_y_pos = 0

# 이동속도
enemy_speed = 10

###########################################################################################################
# 이벤트 루프
running = True # 게임이 진행중인가?

while running:
    dt = clock.tick(30) #게임 화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 아무스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False # X버튼 클릭시 게임이 종료됨
        
        # 우측 좌측 무빙 키 
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT :
                to_x += character_speed
        # 방향키를 떼면 멈춤
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                to_x = 0
            
    character_x_pos += to_x * dt
    # 3. 떨어지는 물체 위치 정의
    enemy_y_pos += enemy_speed

    ##### 경계값 처리

    # 캐릭터 이동 범위 제한 설정 
    if character_x_pos < 0 : character_x_pos = 0
    elif character_x_pos > screen_width - character_width : character_x_pos = screen_width - character_width

    # 번개 위치 범위 제한 설정 
    if enemy_y_pos > screen_height :
        character_score += 1 # 점수 1점 추가 
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    ###### 4. 충돌 처리
    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top  = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크의 경우
    if character_rect.colliderect(enemy_rect):
        print("충돌이 감지 됨")
        running = False 


    # 5. 화면에 그리기
    screen.blit(background, (0,0)) # 백그라운드 이미지 추가
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 떨어지는 물체 그리기 

    # 점수 표출 하기 
    score = game_font.render("SCORE : "+str(int(character_score)), True, (0, 0, 0))
    screen.blit(score, (10, 10))

    pygame.display.update() #게임화면을 다시 그리기

# 잠시 대기
pygame.time.delay(2000) # 2초정도 대기 (ms)

# pygame 종료
pygame.quit()
 
