# **_Parking Lot_**

Este é um projeto em _Django_, que gerencia um estacionamento de veículos.

> ---
>
> _Existem vagas para carros e para motos._
>
> ---

## _Rotas_

A URL Base para essas solicitações é:

```URL
http://127.0.0.1:8000
```

> ---

### _Contas de Usuários_

Para criar um usuário, faça uma solicitação `POST` para `/api/accounts/`.

```JSON
{
  "username": "admin",
  "password": "1234",
  "is_superuser": true,
  "is_staff": true
}
```

> ---
>
> _Por padrão, todos os usuários que se registrarem serão do grupo de Administradores._
>
> ---

Para Logar e poder acessar os **_Recursos_** das outras rotas, faça um `POST` para `/api/login/`

```JSON
{
  "username": "admin",
  "password": "1234"
}
```

> ---
>
> _Esta rota retorna o Token do usuário, que é necessário para realizar outras requisições._
>
> ---

### _**Níveis**_

> ---

Para criar um novo Nível envie uma solicitação `POST` para a rota `/api/levels/`

```JSON
// Header -> Authorization: Token <token-do-admin>
{
  "name": "floor 1",
  "fill_priority": 2,
  "motorcycle_spaces": 20,
  "car_spaces": 50
}
```

Para listar os Níveis cadastrados envie uma solicitação `GET` para a rota `/api/levels/`

### _**Preços**_

> ---

Para criar um novo Preço Base envie uma solicitação `POST` para a rota `/api/pricings/`

```JSON
// Header -> Authorization: Token <token-do-admin>
{
  "a_coefficient": 100,
  "b_coefficient": 100
}
```

### _**Veículos**_

> ---

Para criar um novo registro de Entrada de Veículo, envie uma solicitação `POST` para a rota `/api/vehicles/`

```JSON
// Header -> Authorization: Token <token-do-admin>
{
  "vehicle_type": "car",
  "license_plate": "AYO1029"
}
```

Para registrar a Saída de um Veículo, envie uma solicitação `PUT` para a rota `/api/vehicles/` e especifique o `id` do veículo na URL, por exemplo:

```URL
// Veículo de ID 2
// PUT
http://127.0.0.1:8000/api/vehicles/2/
```

> ---
>
> O sistema calculará o valor à ser pago de acordo com o tempo que o veículo ficou no estacionamento e o ultimo Preço Base registrado.
>
> ---
