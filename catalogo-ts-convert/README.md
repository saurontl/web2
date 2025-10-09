# 🧠 Atividade: Convertendo Projeto de JavaScript para TypeScript

## 🎯 Objetivo

Você deverá converter um projeto simples de JavaScript para TypeScript, aplicando os conceitos aprendidos em aula, como:

- Tipagem estática
- Interfaces e tipos personalizados
- Enum ou union types
- Tipagem de arrays e funções
- Módulos ES6 (`import/export`)

---

## 📁 Estrutura do Projeto (inicial)

```
catalogo-ts-convert/
├── src/
│   ├── app.js
│   └── produtos.js
└── README.md
```

---

## ✅ Passo a passo

1. **Crie um projeto TypeScript**

   ```bash
   npm init -y
   npm install typescript --save-dev
   npx tsc --init
   ```

2. **Altere a extensão dos arquivos de `.js` para `.ts`**

3. **Crie uma interface `Produto` com as seguintes propriedades:**

   - `nome` (string)
   - `preco` (number)
   - `quantidade` (number)
   - `categoria` (use enum ou union)

4. **Tipar todos os parâmetros e retornos das funções**

5. **Tipar o array de produtos como `Produto[]`**

---

## 📌 O que entregar

- Arquivos `.ts` convertidos (`app.ts`, `produtos.ts`)
- `tsconfig.json` com configuração mínima
- Enum ou `type` de categorias
- Comentários explicando brevemente o que foi feito

---

## 🤝 **Dúvidas?**

Caso tenha dúvidas, entre em contato pelo **Discord** ou pelo e-mail do professor. Boa prática e divirta-se! 🚀
