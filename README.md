## 📝 Relatório do Candidato

👤 Identificação: **Nome Completo: Rafael da Silva Sousa**


### 1️⃣ Resumo da Arquitetura do Modelo

No projeto, foi utilizada a arquitetura de uma rede neural convolucional (CNN) para a detecção de padrões em imagens 28x28 que contêm imagens de dígitos manuscritos.
O funcionamento do modelo se concentra no uso de duas camadas Conv2D para a detecção dos padrões, a primeira com 32 filtros e a segunda com 64 filtros. O objetivo da utilização das duas camadas Conv2D foi garantir uma acurácia boa na detecção dos padrões nas imagens. Após cada camada Conv2D são utilizadas camadas MaxPooling2D para que a quantidade de dados seja reduzida aos poucos, garantindo assim uma boa eficiência na quantidade de memória gasta. Além disso, não foram utilizadas camadas densas intermediárias (ocultas), para garantir que o modelo continuasse leve.
A quantidade de épocas escolhida foi 4, de modo a garantir uma boa acurácia, mas sem perder muito em tempo de execução.

### 2️⃣ Bibliotecas Utilizadas

* **TensorFlow / Keras / TFLite**: Utilizado para criação, treinamento e otimização do modelo.
* **NumPy**: Utilização de matrizes e funções matemáticas.

### 3️⃣ Técnica de Otimização do Modelo

A principal abordagem de otimização utilizada foi Dynamic Range Quantization. O princípio utilizado consiste na conversão de pesos de ponto flutuante (que não são suportados bem por muitos dispositivos embarcados) para números inteiros de 8 bits, reduzindo assim o tamanho e a velocidade de execução. Além disso foi também utilizada a técnica float16, com o intuito de realizar uma comparação entre o tamanho do modelo após a utilização de Dynamic Range Quantization e após a utilização de float16.

### 4️⃣ Resultados Obtidos

Como resultados, os testes garantiram uma acurácia de aproximadamente 98,83%, em média, um tamanho final de 72.92KB após otimização com Float16 e um tamanho final de 39.98KB após otimização com Dynamic Range Quantization. Esses resultados comprovam que, a partir da arquitetura utilizada, a detecção de padrões de identificação nas imagens pode ser feita de forma satisfatória, mesmo com uma boa redução no tamanho, garantindo assim uma boa eficiência para a utilização em dispositivos embarcados.
Segue abaixo um comparativo dos resultados obtidos a partir da aplicação de duas técnicas distintas de otimização:

| Técnica de quantização | Tamanho do modelo |
| :--- | :--- |
| Float16 | ~ 72.92KB |
| Dynamic Range Quantization | ~ 39.98KB |

Assim, os testes foram capazes de evidenciar uma redução muito maior do tamanho modelo quando utilizada a técnica de quantização Dynamic Range, em detrimento ao uso de Float16.

### 5️⃣ Comentários Adicionais

* **Testes de parâmetros de treinamento**:
Foram testadas três configurações de treinamento:

| Configuração | `batch_size` | `epochs` | Acurácia Média |
| :--- | :---: | :---: | :---: |
| **α** | 256 | 3 | ~ 98,25% |
| **β** | 128 | 4 | ~ 98,56% |
| **γ** | 64 | 4 | ~ 98,83% |

* **Métrica adotada**:

Para a escolha da melhor configuração de parâmetros, é necessário que se escolha aquela que resulte em uma boa acurácia e em um batch_size tão menor quanto possível, para que não haja um gasto exorbitante de memória, o que não é bom em dispositivos embarcados. Com esse objetivo, foi adotada a seguinte métrica, para a escolha da melhor configuração entre as testadas:

<div align="center" style="margin-bottom: 50px;">
  <b>max( [ (acurácia_média(ϕ) - 98) * 100 ] / batch_size(ϕ) ) para ϕ ∈ {α, β, γ}</b>
</div>
Essa métrica é eficiente na escolha da melhor configuração por utilizar como variáveis a Acurácia Média obtida a partir de cada uma das configurações e o batch_size utilizado em cada uma delas (devido à necessidade de se garantir uma execução rápida e sem grande gasto de memória).

A partir da fórmula da métrica, cada uma das três configurações de parâmetros foi testada:

| Configuração | Valores Aplicados | Resultado da Métrica |
| :---: | :--- | :---: |
| **α** | `(0,25 * 100) / 256` | ~ 0,098 |
| **β** | `(0,56 * 100) / 128` | ~ 0,438 |
| **γ** | `(0,83 * 100) / 64` | ~ 1,297 |

* **Melhor configuração**:

Assim, a partir dos resultados obtidos através dos testes e da métrica utilizada, foi constatado que o melhor equilíbrio entre acurácia e performance se dá através do uso da configuração de parâmetros **γ (batch_size = 64 e acurácia ~ 98,83%)**.