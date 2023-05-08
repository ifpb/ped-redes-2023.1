
**1 (1 ponto). Explique o conceito de encapsulamento em Orientação a Objetos e como ele pode ser implementado em uma classe.**

    * Qual a diferença entre os modificadores de acesso privado, público e protegido utilizados em propriedades em métodos.
    * Cite um exemplo prático pelo qual o uso de encapsulamento seria benéfico e quais seriam os riscos de não implementá-lo.

Resposta:

* O encapsulamento é um dos princípios fundamentais da Orientação a Objetos que visa proteger a integridade e a consistência dos dados e comportamentos de um objeto. 
* Ele consiste em agrupar os dados e os métodos que operam sobre esses dados em uma única unidade, chamada de classe, e restringir o acesso direto a esses dados por outras partes do programa, permitindo o acesso apenas através de métodos específicos da classe, chamados de métodos acessadores (ou getters e setters).

* Em uma classe, os modificadores de acesso controlam a visibilidade dos membros (atributos e métodos) para outras partes do programa. Os modificadores podem ser do tipo: 
    * **Privado:** restringe o acesso aos membros apenas para a própria classe
    * **Público:**  permite o acesso aos membros de qualquer parte do programa
    * **Protegido:** permite o acesso aos membros apenas para a própria classe e suas subclasses.

* Um exemplo prático de uso do encapsulamento seria uma classe que representa uma conta bancária. Os dados dessa classe, como saldo e número da conta, devem ser protegidos para que não possam ser alterados diretamente por outras partes do programa. Para isso, a classe pode ter métodos que permitem apenas a leitura e a escrita controlada do saldo.

* Se o encapsulamento não for implementado, os dados da conta bancária podem ser alterados diretamente por outras partes do programa, comprometendo a integridade e a segurança da conta. Por exemplo, um hacker poderia acessar diretamente o saldo da conta e transferir dinheiro sem autorização. Também não haveria validação dos tipos de valores que podem ser atribuídos ao saldo, permitindo por exemplo à atribuição do saldo a um objeto ou uma lista. Por isso, o encapsulamento é fundamental para garantir a confiabilidade e a segurança dos sistemas orientados a objetos.

---

**2 (1 ponto). Explique as diferenças entre o uso de herança e composição/associação/agregação em Orientação a Objetos.**

    * Dê um exemplo de uma situação em que o uso de herança seria mais adequado e explique o porquê.
    * Dê um exemplo de uma situação em que o uso de composição/associação/agregação seria mais indicado e explique o porquê.

Resposta:
* A herança é um mecanismo que permite que uma classe (subclasse) herde atributos e métodos de outra classe (superclasse). A subclasse pode adicionar, modificar ou sobrescrever os atributos e métodos herdados, mas também pode ter seus próprios atributos e métodos. A herança é uma relação "é um" entre as classes, ou seja, a subclasse é um tipo de superclasse.
* A composição/associação/agregação é um mecanismo que permite que uma classe contenha uma ou várias instâncias de outras classes. A relação entre as classes é uma relação "tem um", onde a classe que contém outras classes é chamada de classe composta e as classes contidas são chamadas de componentes. A composição/associação/agregação permite que as classes trabalhem juntas para realizar uma tarefa complexa, mas sem a hierarquia de herança.
* Um exemplo de uma situação em que o uso de herança seria mais adequado é na criação de uma classe de animais. Suponha que você precise criar várias classes de animais, como cachorro, gato, pássaro e peixe, que compartilham algumas características comuns, como nome, idade e peso. 
  * Nesse caso, seria apropriado criar uma classe animal como superclasse e, em seguida, criar subclasses para cada tipo de animal que herdam os atributos e métodos comuns da superclasse e adicionam seus próprios atributos e métodos exclusivos. 
  * Dessa forma, é possível reutilizar o código comum e reduzir a redundância.
* Um exemplo de uma situação em que o uso de composição/associação/agregação seria mais indicado seria na criação de um sistema de gerenciamento de pedidos. 
  * Suponha a criação de uma classe de pedido que contenha informações sobre o cliente, os itens do pedido e o total do pedido. Nesse caso, seria apropriado criar uma classe de cliente e uma classe de item do pedido como componentes e adicionar esses componentes à classe de pedido por meio de associação ou composição. Dessa forma, é possível reutilizar as classes de cliente e item do pedido em outros lugares do sistema, além de tornar o código mais modular e fácil de manter.
---

**3 (1 ponto). Explique o conceito de classe abstrata em Orientação a Objetos e qual é a sua utilidade.**

    * Dê um exemplo de uma situação em que o uso de classes abstratas seria aplicável e explique o porquê.
    * Qual a relação entre o uso de classes abstratas e o conceito de polimorfismo?

Resposta:
* Uma classe abstrata em Orientação a Objetos é uma classe que não pode ser instanciada diretamente e que contém pelo menos um método abstrato (método que não possui implementação na classe abstrata). 
  * Uma classe abstrata pode conter também métodos concretos (com implementação), bem como atributos, construtores e outras características de uma classe comum.
  * A utilidade das classes abstratas está em fornecer uma estrutura básica e um contrato para as classes derivadas. 
  * Uma classe abstrata define a interface (assinatura dos métodos) que as classes derivadas devem implementar, mas não define como eles serão implementados. Dessa forma, as classes derivadas podem estender a classe abstrata e fornecer sua própria implementação para os métodos abstratos, mas também podem herdar o comportamento dos métodos concretos e atributos da classe abstrata.
* Um exemplo de uma situação em que o uso de classes abstratas seria aplicável é na criação de um sistema de pagamento, em que diferentes formas de pagamento (cartão de crédito, boleto bancário, etc.) compartilham algumas características, mas também têm suas próprias especificidades. 
  * Nesse caso, seria apropriado criar uma classe abstrata de pagamento que contém métodos abstratos como "processar pagamento" e "gerar recibo", e em seguida criar subclasses para cada forma de pagamento que estendem a classe abstrata e fornecem sua própria implementação para os métodos abstratos.
* A relação entre o uso de classes abstratas e o conceito de polimorfismo está no fato de que as classes derivadas podem ser tratadas como objetos da classe abstrata, graças à herança e à sobrescrita de métodos. 
  * Isso significa que um método que recebe um objeto da classe abstrata pode ser usado para processar objetos de qualquer uma das subclasses, sem saber qual classe específica está sendo usada. Isso é conhecido como polimorfismo, e é uma das principais vantagens da Orientação a Objetos.



**(1 ponto). Explique os conceitos de sobreposição e sobrecarga de métodos em Orientação a Objetos e como eles podem ser aplicados em uma classe. Dê exemplos de situações em que o uso de cada um desses conceitos seria benéfico em uma classe.**

Resposta:
* A sobrecarga de métodos ocorre quando uma classe tem dois ou mais métodos com o mesmo nome, mas com parâmetros diferentes. O compilador é capaz de diferenciar esses métodos pela sua lista de parâmetros, e escolhe o método apropriado a ser executado de acordo com os argumentos passados para ele.
* A sobreposição de métodos ocorre quando uma classe herda um método de sua classe pai e redefine esse método com a mesma assinatura na classe filha. 
  * Nesse caso, a implementação do método na classe filha substitui a implementação do método na classe pai. 
  * Isso permite que o comportamento do método seja alterado na classe filha, ou que ele seja adaptado para as necessidades específicas da classe filha.
* O uso da sobrecarga de métodos pode ser benéfico em situações em que há diferentes versões de um mesmo método, que podem ser distinguidas pelos seus parâmetros. Isso permite que o código seja mais flexível e adaptável, e evita a necessidade de criar métodos com nomes diferentes para realizar a mesma tarefa.
* Já a sobreposição de métodos pode ser benéfica em situações em que uma classe filha precisa alterar o comportamento de um método herdado da classe pai, ou fornecer uma implementação específica para as suas necessidades. Isso permite que o código seja mais modular e adaptável, e evita a necessidade de duplicar código ou criar métodos com nomes diferentes.
