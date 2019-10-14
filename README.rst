 FORK Google Ads API Client Library for Python
========================================
this project is not official!!!

Se muestra el proceso para que una cuenta developer de google a traves de oauth2 pueda gestionar cuentas de google ads y las campanias de las mismas. En este flujo la forma de obtener las credenciales para poder gestionar las cuentas de terceros se requiere de un proceso manual(se explica mas adelante cual es). Para conseguir un proceso totalmente automatizado ver mas adelante.

1.- Para obtener acceso a la gestion de una cuenta tercera de google ads se necesita un token y un refresh token para volver a generar nuevos tokens ya que estos caducan. El token lo obtenemos al mostrarle al propietario de la cuenta de google ads una pantalla donde se autentifica con sus credenciales y acepta el consentiento de que un tercero gestione su cuenta.

2.- Al aceptar el consentimiento se redirecciona a una pagina web que muestra un codigo, este codigo es el que tenemos que intercambiar por nuestro token y refresh token. En este punto es donde se lleva la parte manual de copiar ese codigo y utilizarlo para el intercambio.

3.- Una vez obtenido el refresh token lo debemos guardar para que con este podamos manipular la cuenta de google ads de este usuario.

## Nota para crear credenciales:

https://www.evernote.com/shard/s571/sh/38c25b1c-f78c-4192-9ed9-ddbbce04c986/23f9d148619363a9a497bd38630716f9

## Nota para obtener refresh token y consumir la api de gogole ads

https://www.evernote.com/shard/s571/sh/eda0111a-95e8-4dbc-8942-914c824fc3e7/d604153750295f7f4ae82f7e6f403079
