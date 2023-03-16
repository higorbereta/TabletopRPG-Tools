# **Descrição TabletopRPG-Tools**


Ferramenta para auxiliar no gerenciamento de um RPG de mesa. Abaixo segue uma breve descrição de cada componente existente atualmente.

<br>

## **Ficha de Personagem**
Ficha de personagem jogável no RPG de mesa, está sendo estruturada incialmente para ter os dados apenas na execução, onde cada informação é gravada em um dicionário com um número de index que seria o número do personagem.
Dessa forma, é possível realizar o cadastro de mais de um personagem simultaneamente.

Exemplo ficha de personagem:

========== <> ==========

**DADOS DO PERSONAGEM** <br>
Nome: Nort<br>
Raça: Ent<br>
Classe: Mago<br>
Nível: 1<br>
Exp: 0/10<br>
<br>**ATRIBUTOS**<BR>
Força: 0<br>
Destreza: 2<br>
Inteligência: 10<br>
Constituição: 2<br>
Sabedoria: 5<br>
Carisma: 1<br>
|  Pontos disponíveis: 0<br>
========== <> ==========

<br>

Abaixo uma pequena explicação de algumas informações contidas na ficha de personagem.

### **Nível e Experiência**
Atualmente foi colocado na ferramenta um calculo fixo de multiplicador de nível e experiência. 

- Próximo Nível: Nível atual * 5 + 5
~~~ python
def new_nivel(index):
    next_level.update({index:(nivel_personagem[index] * 5 + 5)})
~~~

Assim que atinge a experiência necessária, o sistema realiza a alteração do nível e 0 a experiência corrente, e em seguida valida novamente a quantidade para o nível seguinte. Caso a experiência atual seja maior do que a do proximo nível, ele mantém o valor de sobra.

A alteração de nível é salva em um dicionário onde o index é o índice de personagens criados.

*VALIDAR POSSIBILIDADE DE CONFIGURAR ESSAS VARIÁVEIS.*

<br>

### **Atributos**
Definido inicialmente para iniciar com 20 pontos de atributos de livre distribuição, e 1 ponto adicional por nível que subir.

VALIDAR POSSIBILIDADE DE CONFIGURAR QNT DE PONTOS INICIAIS E AUMENTADOS POR LEVEL.

<br>

## **Dado**
O dado da ferramenta terá a opção de escolha da quantidade de lados que serão calculados através da função random.
Atualmente, não faz armazenamento do histórico do valor do dado.

<br>

## **Calculadora**
A calculadora será uma ferramenta adicional para calcular os resultados do dado, cruzado com as informações do personagem já criado.

Existem os seguintes tipos de calculadora:
- Calculadora de Dano: (Ainda não criado)
- Calculadora de Acerto: (Ainda não criado) -> Validar se não entraria como teste de Destreza
- Teste de atributos: Essa opção abrangera qualquer testes que deverá utilizar os atributos como base, e retonrará o resultado da fórmula, cabendo ao mestre tomar a decisão.
<br><br>

# Desenvolvimento Futuro

- Tela de configurações: Para alterar os multilpicadores de nível
- Configuração atributos: Pontuação inicial e por nível para distribuir
- Validação de atributos: Validação que impeça a diminuição de algum atributo na opção de distribuir pontos.
- Cadastro de Equipamentos
- Cadastro de Inimigos
- Cadastro de Habilidades do persoangem

# Anotações de código

~~~ python
def new_nivel(index):
    next_level.update({index:(nivel_personagem[
~~~