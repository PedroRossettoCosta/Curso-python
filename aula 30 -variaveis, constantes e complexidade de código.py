velocidade = 61
local_carro = 101

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1
#fazendo exercicio sozinha
if velocidade > RADAR_1:
    multa = True
    print('vc está acima da velcodiade permitida!')
else:
    multa = False
    print('Vc está dentro do limite de velocidade')

detectar = local_carro - LOCAL_1

if detectar == RADAR_RANGE or detectar == RADAR_RANGE * -1:
    distancia = True
    print('O radar te detectou!')
else:
    distancia =False
    print('O radar nao te detectou')

if distancia and multa:
    print('Vc levou uma multa')
else: 
    print('Vc não levou uma multa') 

#gabarito
'''vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('carro multado em radar 1')'''