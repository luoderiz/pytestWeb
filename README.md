# Pytest Automation

En este proyecto se encuentran desarrolladas las pruebas de frontend de la aplicación CRM SalesForce utilizando un framework basado en Python, Pytest, y Allure Report para los siguientes navegadores: Chrome, Firefox, Edge (Chromium) e Internet Explorer en modo Incognito y/o modo Headless.

## Getting Started

Las siguientes instrucciones premiten obtener una copia del proyecto, setear el entorno y poder correrlo localmente para desarollo de nuevas funcionalidades o testing.

### Prerequisitos

> #### Python 
>
> - Ingresar a la sección Descargas de [Python](https://www.python.org/downloads/).
> - Descargar la última versión o >= to 3.8.0.
> - Instalar Python y setear las variables de entorno.
> - Verificar que se haya instalado correctamenete con *python --version* desde cualquier consola/terminal (PowerShell, CMD, bash).
> ```
> PS C:\Users\you_user> python --version
> Python 3.8.0
> ```

> #### Entorno virtual de Python
>
> Los entornos virtuales de Python son útiles para evitar conflictos entre distintos proyectos que pueden utilizar distintas versiones de librerías.
> - Ubicado desde una consola en la raíz del proyecto, ejecutar el siguiente comando:
> ```
> python -m venv .venv
> ```
> - Al finalizar, se debería haber creado una carpeta con nombre ".venv" la raíz del proyecto.
> - Para acitvar el entorno virtual, ejecutar el siguiente comando:
> -- En Linux bash/zsh -> ``` $ source .venv/bin/activate ```
> -- En Windows cmd.exe -> ``` .\.venv\Scripts\activate.bat ```
> -- En Windows PowerShell -> ``` .\.venv\Scripts\Activate.ps1 ```
> - Para indagar más sobre el tema, ingresar a la siguiente url [venv](https://docs.python.org/3/library/venv.html).

> #### Allure 
>
> Se necesita instalar Allure en el sistema.
> - Ingresar a [allure release](https://github.com/allure-framework/allure2/releases/).
> - Descargar la versión zip: **2.13.3**.
> - Descomprimir en el directorio que prefieras. Por ejemplo, crear una carpeta de nombre *allure* en *C:\\* y descomprimir aquí.
> ```
> C:\allure
> ```
> - Agregar la carpeta *bin* de allure a las Variables de Entorno *PATH*.
> - Para obtener ayuda sobre el paso anterior, ingresar a [how to set a environment variable on Windows 10](https://superuser.com/questions/949560/how-do-i-set-system-environment-variables-in-windows-10).
> - Verificar la instalación de Allure ejecutando el comando *allure --version* desde cualquier consola/terminal.
> ```
> PS C:\Users\you_user> allure --version
> 2.13.3
> ```

> #### WebDriver 
>
> - Se necesitan descargar los WebDrivers para poder ejecutar los test localmente.
> - Para el caso de Google Chrome, se debe verificar qué versión se encuentra instalada:
> -- Ingresar a *Opciones* (3 puntitos a la derecha).
> -- Seleccionar *Ayuda*.
> -- Seleccionar *Información de Google Chrome*
> - Por ejemplo: Google Chrome Version 90.0.4430.93 (Build oficial) (64 bits)
> - Descargar el WebDriver que soporte la versión del browser instalado. (*por ejemplo: If you are using Chrome version 90, please download ChromeDriver 90.0.4430.24*)
> - Para obtener más información y descargar los WebDrivers, ingresar a los siguientes sitios:
>   - [FirefoxDriver (GeckoDriver)](https://github.com/mozilla/geckodriver/releases)
>   - [ChromeDriver](https://chromedriver.chromium.org/downloads)
>   - [EdgeDriver(chromium)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads)
>   - [InternetExplorerDriver(3.9)](https://selenium-release.storage.googleapis.com/index.html)
> - Crear una carpeta llamada *drivers* en la raíz del proyecto, y guardar los ejecutables *.exe* dentro de esta.
> - *For example*:
>```
> PS C:\Users\you_user\you_workspace\drivers> ls
> Name
> ----
> chromedriver.exe
> geckodriver.exe
> IEDriverServer.exe
> msedgedriver.exe
>```

### Instalación

>
> #### Python Libs
> - Es neceasrio instalar en el proyecto los módulos/librerías que se usan como dependencias desde el archivo *requirements.txt*.
> ```
> PS C:\Users\you_user\you_workspace> pip install -r requirements.txt
> ```
> - Finalizada la instalación, se puede verificar la instalación de los módulos con el comando *pip freeze* y se debe observar lo siguente:
> ```
> PS C:\Users\you_user\you_workspace> pip freeze
> ...
> allure-pytest-bdd==2.8.22
> allure-python-commons==2.8.13
> pytest==5.4.2
> selenium==3.141.0
> ...
>```

### Settings

> #### Configuración del framework
> Antes de correr los test es necesario comprender el archivo **config.json**. Este archivo tiene los siguientes atributos:
> - **browser** : *str* (string con el nombre del navegador. Debe ser: "firefox", "chrome", "edge", "ie").
> - **driverPath** : *str* (string con el path donde se guardaron los WebDrivers. Recomendación: "./drivers/your_webdriver.exe").
> - **urlApp** : *str* (string con la url de entrada de la aplicación App a testear. Por ejemplo: "https://www.your-url-app.com").
> - **defaultWait** : *int* (tiempo en segundos a esperar por la carga de los elementos antes de hacer alguna acción. Si un elemento no está presente o visible en este tiempo, el test fallará por *timeout*).
> - **incognito** : *bool* (booleano para indicar si el test se ejecuta en modo Incognito/Private. *true* para ejecutar en este modo, *false* para ejecutar sin este modo).
> - **extensions** : *list* (lista con el nombre de las extensiones a instalar. Por ejemplo: "adblock").
> - **lang** : *str* (string con el nombre del código de localización para setear el navegador. Listado: "http://www.lingoes.net/en/translator/langcode.htm").
> - **headless** : *json* (diccionario que contiene los atributos *enabled* y *window_size*).
> - - **enabled** : *bool* (booleano para indicar si el test se ejecutar sin visualización del browser (headless). *true* para ejecutar en este modo, *false* para ejecutar sin este modo).
> - - **window_size** : *json* (diccionario que contiene los tamaños *x* e *y* de la ventana del browser. Este parámetro es sólo para el modo headless).
> - - - **X** : *int* (ancho de la ventana. Por ejemplo: 800).
> - - - **Y** : *int* (alto de la ventana. Por ejemplo: 600).


> Un ejemplo del archivo *config.json*:
>
>```
>   {
>       "browser": "chrome",
>       "driverPath": "./drivers/chromedriver.exe",
>       "urlApp": "http://demo.automationtesting.in/Index.html",
>       "defaultWait": 15,
>       "incognito": false,
>       "lang": "es-AR",
>       "headless": {
>           "enabled": false,
>           "window_size": {
>               "X": 1920,
>               "Y": 1080
>           }
>       },
>       "extensions": [
>           "adblock"
>       ]
>   }
>```


## Ejecución de tests
> El framework está basado en *pytest*, por lo que las distintas formas de ejecutar los test se pueden revisar en la documenetación: [pytest](https://docs.pytest.org/en/6.2.x/usage.html#calling-pytest-through-python-m-pytest).
> ```bash
> #Ejecucion por tag
> python -m pytest -v -m alias
> ```


### Reporte Allure
> Para acceder al reporte allure se debe utilizar el siguiente comando:
> ```
> allure serve .\report\
> ```
>
> **Advertencia:** el directorio donde se busca el reporte con el comando anterior, debe coincidir con el especificado en el comando con el que se ejecutó el script del test.


## Plugins recomendados
> A continuación se enumeran una serie de plugins recomendados para el entorno de desarrollo Visual Studio Code:
>* [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
>* [**Pylance**](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
>* [**Cucumber (Gherkin) Full Support**](https://marketplace.visualstudio.com/items?itemName=alexkrechik.cucumberautocomplete)



