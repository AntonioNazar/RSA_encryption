import random
códigos_para_símbolos = {111: '0', 112: '1', 113: '2', 114: '3', 115: '4',
116: '5', 117: '6', 118: '7', 119: '8', 121: '9', 122: '=', 123: '+',
124: '-', 125: '/', 126: '*', 127: 'a', 128: 'b', 129: 'c', 131: 'd',
132: 'e', 133: 'f', 134: 'g', 135: 'h', 136: 'i', 137: 'j', 138: 'k',
139: 'l', 141: 'm', 142: 'n', 143: 'o', 144: 'p', 145: 'q', 146: 'r',
147: 's', 148: 't', 149: 'u', 151: 'v', 152: 'w', 153: 'x', 154: 'y',
155: 'z', 156: 'á', 157: 'à', 158: 'â', 159: 'ã', 161: 'é', 162: 'ê',
163: 'í', 164: 'ó', 165: 'ô', 166: 'õ', 167: 'ú', 168: 'ç', 169: 'A',
171: 'B', 172: 'C', 173: 'D', 174: 'E', 175: 'F', 176: 'G', 177: 'H',
178: 'I', 179: 'J', 181: 'K', 182: 'L', 183: 'M', 184: 'N', 185: 'O',
186: 'P', 187: 'Q', 188: 'R', 189: 'S', 191: 'T', 192: 'U', 193: 'V',
194: 'W', 195: 'X', 196: 'Y', 197: 'Z', 198: 'Á', 199: 'À', 211: 'Â',
212: 'Ã', 213: 'É', 214: 'Ê', 215: 'Í', 216: 'Ó', 217: 'Ô', 218: 'Õ',
219: 'Ú', 221: 'Ç', 222: ',', 223: '.', 224: '!', 225: '?', 226: ';',
227: ':', 228: '_', 229: '(', 231: ')', 232: '"', 233: '#', 234: '$',
235: '%', 236: '@', 237: ' ', 238: '\n'}

símbolos_para_códigos = {'0': 111, '1': 112, '2': 113, '3': 114, '4': 115,
'5': 116, '6': 117, '7': 118, '8': 119, '9': 121, '=': 122, '+': 123,
'-': 124, '/': 125, '*': 126, 'a': 127, 'b': 128, 'c': 129, 'd': 131,
'e': 132, 'f': 133, 'g': 134, 'h': 135, 'i': 136, 'j': 137, 'k': 138,
'l': 139, 'm': 141, 'n': 142, 'o': 143, 'p': 144, 'q': 145, 'r': 146,
's': 147, 't': 148, 'u': 149, 'v': 151, 'w': 152, 'x': 153, 'y': 154,
'z': 155, 'á': 156, 'à': 157, 'â': 158, 'ã': 159, 'é': 161, 'ê': 162,
'í': 163, 'ó': 164, 'ô': 165, 'õ': 166, 'ú': 167, 'ç': 168, 'A': 169,
'B': 171, 'C': 172, 'D': 173, 'E': 174, 'F': 175, 'G': 176, 'H': 177,
'I': 178, 'J': 179, 'K': 181, 'L': 182, 'M': 183, 'N': 184, 'O': 185,
'P': 186, 'Q': 187, 'R': 188, 'S': 189, 'T': 191, 'U': 192, 'V': 193,
'W': 194, 'X': 195, 'Y': 196, 'Z': 197, 'Á': 198, 'À': 199, 'Â': 211,
'Ã': 212, 'É': 213, 'Ê': 214, 'Í': 215, 'Ó': 216, 'Ô': 217, 'Õ': 218,
'Ú': 219, 'Ç': 221, ',': 222, '.': 223, '!': 224, '?': 225, ';': 226,
':': 227, '_': 228, '(': 229, ')': 231, '"': 232, '#': 233, '$': 234,
'%': 235, '@': 236, ' ': 237, '\n': 238}
def Euclides_estendido(a,b):
  x_antigo,y_antigo=1,0
  x_novo,y_novo=0,1
  Dividendo,divisor=a,b
  while divisor!= 0:
   Quociente,resto=divmod(Dividendo,divisor)
   x_antigo,x_novo=x_novo,(x_antigo-Quociente*x_novo)
   y_antigo,y_novo=y_novo,(y_antigo-Quociente*y_novo)
   Dividendo,divisor=divisor,resto
  return x_antigo
def Euclides(a,b):
  dividendo,divisor=a,b
  while True:
    resto=dividendo%divisor
    if resto==0:
     return divisor
    dividendo,divisor=divisor,resto
def fatorando_2(n):
  k=0
  q=n
  while q%2==0:
    q//=2
    k+=1
  return k,q

def MillerRabin(modulo,base):
  if modulo%2==0 or modulo==1:
    return 'composto'
  base=(base%modulo)
  if base==0 or base==1:
    return 'inconclusivo'
  k,q=fatorando_2(modulo-1)
  r=pow(base,q,modulo)
  if r==1 or r==modulo-1:
    return 'inconclusivo'
  i=0
  while(True):
   r=pow(r,2,modulo)
   i+=1
   if r==1 or i==k:
     return 'composto'
   if r==modulo-1:
     return 'inconclusivo'
def provavelmente_primo(n):
 modulo=random.randrange(10**(n)+1,10**(n+2)-1,2)
 i=0
 while(i<=10):
  base=random.randrange(2,modulo-2)
  x=MillerRabin(modulo,base)
  if(x=='inconclusivo'):
    i+=1
  else:
   i=0
   modulo=random.randrange(10**(n)+1,10**(n+2)-1,2)
 return modulo
def gera_chave():
  p=provavelmente_primo(50)
  q=provavelmente_primo(50)
  n=p*q
  phin=(p-1)*(q-1)
  while(True):
    e=random.randrange(3,phin-1)
    if(Euclides(e,phin)==1):
     break;
  d=Euclides_estendido(phin,e)
  inverso_p_mod_q=Euclides_estendido(p,q)
  inverso_q_mod_p=Euclides_estendido(q,p)
  forma_red_d_mod_p_1=d%(p-1)
  forma_red_d_mod_q_1=d%(q-1)
  return n,e,d,p,q,inverso_p_mod_q,inverso_q_mod_p,forma_red_d_mod_p_1,forma_red_d_mod_q_1
def encriptar(texto,n,e):
  util={}
  lista=[]
  for i in range(len(texto)):
    util[texto[i]]=dict.get(símbolos_para_códigos,texto[i])
    lista.append(list(dict.values(util)))
    dict.clear(util)
  for i in range (len(lista)):
    lista[i]=pow(*lista[i],e)%n
  return lista
def descriptar(blocos,n,d):
  util={}
  lista=[]
  for i in range(len(blocos)):
    blocos[i]=pow(blocos[i], d)%n
  for i in range(len(blocos)):
    util[blocos[i]]=dict.get(códigos_para_símbolos,blocos[i])
    lista.append(list(dict.values(util)))
    dict.clear(util)
  return lista