# Comedouros-para-ovinos
Backend do sistema de comedouros para ovinos

---

## API - Endpoints de Usuário

### POST /registrar_usuario
Registra e realiza login de um novo usuário.

**Campos obrigatórios (JSON):**
- `nome`: string
- `senha`: string
- `confirmacaoSenha`: string
- `email`: string

**Retorno:**
- `mensagem`: string - mensagem de sucesso
- `erro`: string - mensagem de erro

---

### POST /login_usuario
Realiza login de um usuário existente.

**Campos obrigatórios (JSON):**
- `nome`: string
- `senha`: string

**Retorno:**
- `mensagem`: string - mensagem de sucesso
- `erro`: string - mensagem de erro

---

### GET /logout_usuario
Realiza logout do usuário autenticado.

**Autenticação:** Requer sessão ativa (login prévio)

**Retorno:**
- `mensagem`: string - mensagem de sucesso

---

### PATCH /editar_usuario
Edita os dados de cadastro do usuário autenticado.

**Autenticação:** Requer sessão ativa (login prévio)

**Campos opcionais (JSON):**
- `novoNome`: string
- `novaSenha`: string
- `novoEmail`: string

**Retorno:**
- `mensagem`: string - mensagem de sucesso
- `usuario`: objeto JSON com dados atualizados

---

### DELETE /deletar_usuario
Deleta o usuário autenticado.

**Autenticação:** Requer sessão ativa (login prévio)

**Retorno:**
- `mensagem`: string - mensagem de sucesso

---

### GET /perfil_usuario
Retorna os dados do usuário autenticado.

**Autenticação:** Requer sessão ativa (login prévio)

**Retorno:**
- Objeto JSON com os dados do usuário logado

---

