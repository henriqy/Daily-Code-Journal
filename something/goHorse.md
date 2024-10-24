# Go Horse Programming

> é uma expressão usada na área de programação para descrever um estilo de desenvolvimento de software desorganizado e pouco estruturado.

## principais características do Go Horse incluem:

1. Falta de planejamento
2. Ausência de padrões e melhores práticas
3. Código pouco estruturado
4. Falta de revisão de código
5. Atrasos e retrabalho

## Exemplo de Codigo Go Horse:

---

// Variáveis globais (evitar uso excessivo)
let x = 0;
let y = 100;

// Função sem nenhuma modularização ou clareza
function a() {
  console.log('Função a chamada');

  // Muitas linhas de código que não estão organizadas
  x = 10;
  y += 20;

  // ...

  // Muitas mais linhas de código

  // ...

  console.log('x:', x, 'y:', y);
}

// Função b que chama a função a
function b() {
  console.log('Função b chamada');
  a(); // Chamada de função não estruturada
}

// Chamada inicial
b(); // Início do caos!

---