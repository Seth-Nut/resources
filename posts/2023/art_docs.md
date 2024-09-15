---
title: "Documentación"
subtitle: "Enteneder los pasos para crear una buena documentación en Python (más algunas recomendaciones)."

author: "Francisco Alfaro"
date: "2023-10-07"
categories: [python, docs]
image: "../images/books.png"
---


# El arte de una buena documentación

<img src="../images/books.png" width="150" align="center" />

<br>


Esperamos que, si estás leyendo este tutorial, ya comprendas la importancia de documentar tu código. Pero, por si acaso, permíteme citar algo que Guido mencionó en la reciente [PyCon 2016](https://www.youtube.com/watch?v=YgtL4S7Hrwo&ab_channel=PyCon2016):

::: {.callout-note appearance="simple"}

## Cita

  "El código se lee más a menudo de lo que se escribe."
    — _[Guido van Rossum](https://gvanrossum.github.io/)_
:::

## Introducción

Cuando escribes código, lo haces para dos audiencias principales: tus usuarios
y tus desarrolladores (incluyéndote a ti mismo). Ambas audiencias son
igualmente cruciales. Si eres como yo, es posible que hayas abierto
antiguas bases de código y te hayas preguntado: "¿En qué estaba pensando?". 
Si tienes dificultades para entender tu propio código, imagina lo que tus 
usuarios u otros desarrolladores sienten cuando intentan utilizarlo o **contribuir** a tu código.

Por otro lado, es probable que hayas pasado por situaciones en las que deseabas realizar
algo en Python y encontraste lo que parecía ser una excelente biblioteca que podría hacer 
el trabajo. Sin embargo, al comenzar a usar la biblioteca, buscaste ejemplos, descripciones
o incluso documentación oficial sobre cómo realizar una tarea específica y no pudiste encontrar una solución de inmediato.

Después de buscar durante un tiempo, te das cuenta de que la documentación es insuficiente o,
peor aún, está completamente ausente. Esta es una experiencia frustrante que te impide utilizar 
la biblioteca, sin importar cuán bueno o eficiente sea el código. Daniele Procida resumió esta situación de manera acertada:

::: {.callout-note appearance="simple"}

## Cita

  "No importa cuán bueno sea tu software, porque **si la documentación no es lo suficientemente buena, la gente no lo usará.**"
    — _[Daniele Procida](https://www.divio.com/en/blog/documentation/)_
:::


En esta guía, aprenderás desde cero cómo documentar adecuadamente tu código 
en Python, desde los scripts más pequeños hasta los proyectos más grandes de
Python, para evitar que tus usuarios se sientan frustrados al usar o contribuir a tu proyecto.


## Comentarios vs Documentación

<img src="https://i.stechies.com/userfiles/images/python-docstrings.webp" width="500" align="center" />


Antes de sumergirnos en el arte de documentar tu código en Python, es crucial establecer una distinción fundamental: los comentarios y la documentación desempeñan roles distintos y están dirigidos a audiencias diferentes.

**Comentarios**:

En términos generales, los comentarios están diseñados 
para proporcionar información sobre tu código a los desarrolladores. 

La audiencia principal a la que se dirigen son aquellos que mantienen y 
trabajan en el código Python. Cuando se combinan con un código bien escrito, 
los comentarios actúan como guías que ayudan a los lectores a comprender mejor el código, 
su propósito y su estructura. Esto se alinea perfectamente con la sabia observación de Jeff Atwood,

::: {.callout-note appearance="simple"}

## Cita

   "El código te dice cómo; los comentarios te dicen por qué."
    — [Jeff Atwood](https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/)
:::

**Documentación del Código**:

Por otro lado, la documentación del código se enfoca en describir el uso y la funcionalidad 
del código a los usuarios. Aunque puede ser útil durante el proceso de desarrollo, su audiencia 
principal son los usuarios finales del software. La siguiente sección de este artículo se adentrará 
en cuándo y cómo debes abordar la tarea de comentar tu código en Python.

## Comentarios 

<img src="https://www.stechies.com/userfiles/images/Comments-in-python.webp" width="500" align="center" />


En Python, los comentarios son esenciales para 
proporcionar información adicional sobre tu código. 

Se crean utilizando el símbolo de número (`#`) y deben 
ser declaraciones breves, no más largas que unas pocas frases. Aquí tienes un ejemplo simple:

```python
def hello_world():    
    # Un comentario simple antes de una simple declaración de impresión
    print("Hola Mundo")
```

De acuerdo con las [pautas de estilo de código de Python (PEP 8)](http://pep8.org/#maximum-line-length), 
los comentarios deben tener una longitud máxima de 72 caracteres.
Esto es válido incluso si tu proyecto cambia la longitud máxima de línea recomendada para que sea mayor que los 80 caracteres. 
Si un comentario va a superar el límite de caracteres recomendado, es apropiado usar múltiples líneas para el comentario:

```python
def hello_long_world():     
    # Una declaración muy larga que sigue y sigue y sigue y sigue y sigue 
    # sin terminar hasta que alcance el límite de 80 caracteres
    print("¡Hola Mundoooooooooooooooooooooooooooooooooooooooooooooooooooooo!")
```

Comentar tu código sirve para varios propósitos, incluyendo:

*   **Planificación y Revisión:** Durante el desarrollo de nuevas partes de tu código, los comentarios pueden servir como una forma de planificar o esquematizar esa sección. Es importante recordar eliminar estos comentarios una vez que se haya implementado y revisado/testeado el código real:

    ```python
    # Primer paso
    # Segundo paso
    # Tercer paso
    ```

*   **Descripción del Código:** Los comentarios se utilizan para explicar la intención de secciones específicas del código:

    ```python
    # Intentar una conexión basada en configuraciones anteriores. Si no tiene éxito,
    # solicitar al usuario nuevas configuraciones.
    ```

*   **Descripción Algorítmica:** Al usar algoritmos, especialmente los complicados, es útil explicar cómo funcionan o cómo se implementan en tu código. También es apropiado describir por qué seleccionaste un algoritmo específico en lugar de otro:

    ```python
    # Usar el ordenamiento rápido para obtener ganancias de rendimiento.
    ```

*   **Etiquetado:** Puedes utilizar etiquetas para señalar secciones específicas de código donde se encuentran problemas conocidos o áreas de mejora. Algunos ejemplos son `BUG`, `FIXME` y `TODO`:

    ```python
    # TODO: Agregar condición para cuando 'val' sea None
    ```

Los comentarios en tu código deben ser breves y centrados. Evita comentarios largos cuando sea posible. Además, sigue las siguientes cuatro reglas esenciales sugeridas por Jeff Atwood:

1.  **Mantén los Comentarios Cerca del Código:** Los comentarios deben estar lo más cerca posible del código que describen. Los comentarios distantes del código descriptivo son frustrantes y pueden pasarse por alto fácilmente al realizar actualizaciones.

2.  **Evita el Formato Complejo:** No uses formatos complejos como tablas o figuras ASCII. Estos formatos pueden distraer y ser difíciles de mantener con el tiempo.

3.  **Evita Información Redundante:** Supón que el lector del código tiene un entendimiento básico de los principios de programación y la sintaxis del lenguaje. No incluyas información redundante.

4.  **Diseña Tu Código para que se Comente por Sí Mismo:** La forma más fácil de entender el código es leyéndolo. Cuando diseñes tu código utilizando conceptos claros y fáciles de entender, ayudarás al lector a comprender tu intención de manera rápida y sencilla.

Recuerda que los comentarios están diseñados para los lectores, incluyéndote a ti mismo,
para ayudarlos a comprender el propósito y diseño del software.

### Type Hinting en Python

<img src="https://cdn-images-1.medium.com/v2/resize:fit:764/1*ki1NgX07eTLUWtafhqmiWQ.gif" width="400" align="center" />


El [Type Hinting](https://docs.python.org/3/library/typing.html) es una característica que te permite
indicar explícitamente los tipos de datos que esperas 
en las funciones y métodos. Aunque Python es un lenguaje de programación de tipado dinámico,
el Type Hinting no cambia esa naturaleza, pero proporciona información adicional a los desarrolladores y a
las herramientas de análisis estático sobre cómo debería funcionar el código.

El Type Hinting no afecta el comportamiento en tiempo de ejecución,
por lo que no impide que el código funcione si los tipos no coinciden.

En cambio, es una herramienta para ayudar a los desarrolladores a comprender y depurar el
código de manera más eficiente y prevenir posibles errores.

Considera la siguiente función `hello_name`:

```python
def hello_name(name: str) -> str:
    return f"Hello {name}"
```

En este ejemplo, hemos utilizado Type Hinting para especificar 
que el parámetro `name` debe ser una cadena (`str`) y que la función 
`hello_name` debe devolver una cadena (`str`). Esta información es
útil para otros desarrolladores que utilicen esta función porque 
ahora saben qué tipo de dato esperar como entrada y qué tipo de dato obtendrán
como resultado.


## Docstrings

<img src="https://t3h.edu.vn/sites/default/files/docstring-trong-python-01.png" width="500" align="center" />


Una parte fundamental de
la documentación en Python son las **docstrings**, que son cadenas de texto utilizadas 
para describir funciones, clases, módulos y más.

### Introudcción
Las docstrings son cadenas de documentación 
que se encuentran dentro del código fuente Python. 
Estas cadenas proporcionan información sobre el propósito y el
funcionamiento de funciones, clases y otros elementos del código.

Las docstrings son especialmente valiosas para ayudar a los usuarios y desarrolladores
a comprender cómo utilizar y trabajar con tu código.

**¿Cómo Funcionan las Docstrings?**

Cuando definimos una función, clase o módulo en Python, podemos incluir una docstring justo debajo de la definición. Por ejemplo:

```python
def saludar(nombre):
    """Esta función imprime un saludo personalizado."""
    print(f"Hola, {nombre}!")
```

Las docstrings se pueden acceder a través del atributo `__doc__` del objeto. Por ejemplo:

```python
print(saludar.__doc__)
```

La salida sería: "Esta función imprime un saludo personalizado." 
Las docstrings también se utilizan en entornos de desarrollo 
interactivo y se muestran al utilizar la función `help()`.

**Manipulación de Docstrings**

Es importante destacar que puedes manipular
directamente las docstrings. Sin embargo, existen restricciones
para los objetos incorporados en Python. Por ejemplo, no puedes cambiar la docstring de un objeto `str` incorporado:

```python
str.__doc__ = "¡Esto no funcionará para objetos incorporados!"
```

Pero para funciones y objetos personalizados,
puedes establecer o modificar sus docstrings de la siguiente manera:

```python
def decir_hola(nombre):
    """Una función simple que saluda a la manera de Richie."""
    print(f"Hola {nombre}, ¿soy yo a quien estás buscando?")

decir_hola.__doc__ = "Una función que saluda estilo Richie Rich."
```

**Ubicación Estratégica de las Docstrings**

Una forma más sencilla de definir docstrings es colocar una cadena literal justo debajo de la definición de la función o clase. Python automáticamente interpreta esta cadena como la docstring. Por ejemplo:

```python
def decir_hola(nombre):
    """Una función simple que saluda a la manera de Richie."""
    print(f"Hola {nombre}, ¿soy yo a quien estás buscando?")
```

### Tipos de Docstrings

Las docstrings son elementos esenciales para documentar 
tu código Python de manera clara y coherente. Siguen convenciones y
pautas que se describen en [PEP 257](https://www.python.org/dev/peps/pep-0257/). 

El propósito de las docstrings es proporcionar a los usuarios de tu código un resumen conciso 
y útil del objeto, como una función, clase, módulo o script. Deben ser lo suficientemente 
concisas como para ser fáciles de mantener, pero lo suficientemente detalladas como para
que los nuevos usuarios comprendan su propósito y cómo utilizar el objeto documentado.

#### Formato de las Docstrings

Todas las docstrings deben utilizar el formato de triple comilla doble (`"""`) y 
deben colocarse justo debajo de la definición del objeto, ya sea en una sola línea o en varias líneas:

**Una línea:**

```python
"""Esta es una línea de resumen rápida utilizada como descripción del objeto."""
```

**Varias líneas:**

```python
"""
Esta es la línea de resumen
Esta es la elaboración adicional de la docstring. Dentro de esta sección, puedes proporcionar más detalles según sea apropiado para la situación. Observa que el resumen y la elaboración están separados por una nueva línea en blanco.
"""
```

Es importante destacar que todas las docstrings de varias líneas deben seguir un patrón específico:

1. Una línea de resumen de una sola línea.
2. Una línea en blanco después del resumen.
3. Cualquier elaboración adicional de la docstring.
4. Otra línea en blanco.

Además, todas las docstrings deben tener una longitud máxima de caracteres que sigue las mismas pautas que los comentarios, que es de 72 caracteres.


#### Docstrings de Clase

Las docstrings de clase se crean para la clase en sí, así como para cualquier método de clase. Las docstrings se colocan inmediatamente después de la clase o el método de clase, con un nivel de sangría:

```python
class ClaseSimple:
    """Aquí van las docstrings de clase."""
    def decir_hola(self, nombre: str):
        """Aquí van las docstrings de método de clase."""
        print(f'Hola {nombre}')
```

Las docstrings de clase deben contener la siguiente información:

* Un breve resumen de su propósito y comportamiento.
* Cualquier método público, junto con una breve descripción.
* Cualquier propiedad de clase (atributos).
* Cualquier cosa relacionada con la [interfaz](https://realpython.com/python-interface/) para los subclases, si la clase está destinada a ser subclaseada.

Los parámetros del [constructor de clase](https://realpython.com/python-class-constructor/) deben documentarse dentro de la docstring del método `__init__` de la clase. Los métodos individuales deben documentarse utilizando sus propias docstrings individuales. Las docstrings de método de clase deben contener lo siguiente:

* Una breve descripción de lo que hace el método y para qué se utiliza.
* Cualquier argumento (tanto requerido como opcional) que se pase, incluidos los argumentos de palabras clave.
* Etiqueta para cualquier argumento que se considere opcional o tenga un valor predeterminado.
* Cualquier efecto secundario que ocurra al ejecutar el método.
* Cualquier excepción que se genere.
* Cualquier restricción sobre cuándo se puede llamar al método.

Echemos un vistazo a un ejemplo simple de una clase 
de datos que representa un Animal. Esta clase contendrá algunas propiedades de clase, propiedades de instancia, un `__init__` y un único [método de instancia](https://realpython.com/instance-class-and-static-methods-demystified/):

```python
class Animal:
    """Una clase utilizada para representar un Animal
    
    Attributes:
        dice_str (str): una cadena formateada para imprimir lo que dice el animal
        nombre (str): el nombre del animal
        sonido (str): el sonido que hace el animal
        num_patas (int): el número de patas del animal (predeterminado 4)
    """
    
    dice_str = "Un {nombre} dice {sonido}"
    
    def __init__(self, nombre, sonido, num_patas=4):
        """Inicializa una nueva instancia de Animal
        
        Parameters:
            nombre (str): El nombre del animal
            sonido (str): El sonido que hace el animal
            num_patas (int, opcional): El número de patas del animal (predeterminado es 4)
        """
        self.nombre = nombre
        self.sonido = sonido
        self.num_patas = num_patas
        
    def dice(self, sonido=None):
        """Imprime el nombre del animal y el sonido que hace.
        
        Si no se pasa el argumento `sonido`, se utiliza el sonido predeterminado del Animal.
        
        Parameters:
            sonido (str, opcional): El sonido que hace el animal (predeterminado es None)
        
        Raises:
            NotImplementedError: Si no se establece ningún sonido para el animal o se pasa como parámetro.
        """
        if self.sonido is None and sonido is None:
            raise NotImplementedError("¡No se admiten animales silenciosos!")
        sonido_salida = self.sonido if sonido is None else sonido
        print(self.dice_str.format(nombre=self.nombre, sonido=sonido_salida))
```

### Estilos de Docstrings

<img src="https://cdn-icons-png.flaticon.com/512/2620/2620243.png" width="150" align="center" />


 Existen formatos específicos de docstrings que pueden 
 ser utilizados para ayudar a los analizadores de docstrings y 
 a los usuarios a tener un formato familiar y reconocido.

Algunos de los formatos más comunes son los siguientes:

| Tipo de Formato                                                                                               | Descripción                                                                    | Compatible con Sphinx | Especificación Formal |
|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|:---------------------:|:--------------------:|
| [Google docstrings](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings) | Forma de documentación recomendada por Google                                    |         Sí            |          No          |
| [reStructuredText](http://docutils.sourceforge.net/rst.html)                                                  | Estándar oficial de documentación de Python; no es amigable para principiantes pero rico en características |         Sí            |          Sí          |
| [NumPy/SciPy docstrings](https://numpydoc.readthedocs.io/en/latest/format.html)                               | Combinación de reStructuredText y Docstrings de Google utilizada por NumPy      |         Sí            |          Sí          |
| [Epytext](http://epydoc.sourceforge.net/epytext.html)                                                         | Una adaptación de Epydoc para Python; ideal para desarrolladores de Java            |    No oficialmente    |          Sí          |

La elección del formato de docstring depende de ti, pero debes mantener el mismo formato en todo tu documento o proyecto. A continuación, se presentan ejemplos de cada tipo para darte una idea de cómo se ve cada formato de documentación.

#### Google docstrings

```python
"""Obtiene e imprime las columnas de encabezado de la hoja de cálculo

Args:
    file_loc (str): La ubicación del archivo de la hoja de cálculo.
    print_cols (bool): Una bandera utilizada para imprimir las columnas en la consola
        (el valor predeterminado es Falso)

Returns:
    list: una lista de cadenas que representan las columnas de encabezado
"""
```

#### reStructuredText

```python
"""Obtiene e imprime las columnas de encabezado de la hoja de cálculo

:param file_loc: La ubicación del archivo de la hoja de cálculo
:type file_loc: str
:param print_cols: Una bandera utilizada para imprimir las columnas en la consola
    (el valor predeterminado es Falso)
:type print_cols: bool

:returns: una lista de cadenas que representan las columnas de encabezado
:rtype: list
"""
```

#### NumPy/SciPy docstrings

```python
"""Obtiene e imprime las columnas de encabezado de la hoja de cálculo

Parameters
----------
file_loc : str
    La ubicación del archivo de la hoja de cálculo
print_cols : bool, opcional
    Una bandera utilizada para imprimir las columnas en la consola (el valor predeterminado es Falso)

Returns
-------
list
    una lista de cadenas que representan las columnas de encabezado
"""
```

#### Epytext

```python
"""Obtiene e imprime las columnas de encabezado de la hoja de cálculo

@type file_loc: str
@param file_loc: La ubicación del archivo de la hoja de cálculo
@type print_cols: bool
@param print_cols: Una bandera utilizada para imprimir las columnas en la consola
    (el valor predeterminado es Falso)
@rtype: list
@returns: una lista de cadenas que representan las columnas de encabezado
"""
```

Estos ejemplos te proporcionan una idea de cómo se estructuran y formatean las docstrings 
en diferentes estilos de documentación. 

Puedes elegir el que mejor se adapte a tus preferencias 
y necesidades de documentación, pero asegúrate de mantener la coherencia en todo tu proyecto.

## Documentar tus Proyectos de Python

Los proyectos de Python vienen en todo tipo de formas,
tamaños y propósitos. La forma en que documentas tu proyecto
debe adaptarse a tu situación específica. Ten en cuenta quiénes serán 
los usuarios de tu proyecto y adáptate a sus necesidades. Dependiendo 
del tipo de proyecto, se recomiendan ciertos aspectos de la documentación. La estructura general del proyecto y su documentación debe ser la siguiente:

```
project_root/
│
├── project/  # Project source code
├── docs/
├── README
├── HOW_TO_CONTRIBUTE
├── CODE_OF_CONDUCT
├── examples.py
```

Esta estructura de directorios es un diseño común para organizar un proyecto de software en Python. A continuación, se explica en detalle cada elemento de esta estructura:

1. **project_root (Directorio Raíz del Proyecto):**
   Este es el directorio principal que contiene todos los archivos y carpetas relacionados con tu proyecto. Es el punto de partida para tu proyecto.

2. **project/ (Carpeta "project"):**
   Esta carpeta suele contener el código fuente principal de tu proyecto. Aquí se almacenan todos los archivos de Python que forman parte de tu proyecto. Puedes organizar estos archivos en subdirectorios según la estructura de tu proyecto. Por ejemplo, puedes tener subdirectorios para módulos específicos o componentes del proyecto.

3. **docs/ (Carpeta "docs"):**
   La carpeta "docs" se utiliza para almacenar la documentación de tu proyecto. Aquí puedes incluir documentos explicativos, manuales de usuario, instrucciones de instalación y cualquier otra documentación relevante. Mantener una documentación clara y organizada es esencial para que los usuarios comprendan y utilicen tu proyecto de manera efectiva.

4. **README:**
   El archivo "README" es un documento importante que proporciona una breve descripción de tu proyecto y su propósito. Suele incluir información sobre cómo instalar y utilizar el proyecto, así como otros detalles importantes. Los usuarios suelen consultar este archivo primero cuando exploran un proyecto.

5. **HOW_TO_CONTRIBUTE:**
   Este archivo contiene instrucciones para las personas que deseen contribuir al desarrollo de tu proyecto. Incluye detalles sobre cómo pueden colaborar, enviar correcciones, agregar nuevas funciones y seguir las pautas de contribución.

6. **CODE_OF_CONDUCT:**
   El archivo "CODE_OF_CONDUCT" establece las reglas y pautas de comportamiento que deben seguir los colaboradores y usuarios del proyecto. Define cómo deben interactuar entre sí de manera respetuosa y profesional. También puede indicar las consecuencias en caso de violación del código de conducta.

7. **examples.py:**
   Este archivo es un script de Python que contiene ejemplos simples de cómo utilizar las funcionalidades de tu proyecto. Estos ejemplos pueden ayudar a los usuarios a comprender cómo utilizar tu código en situaciones reales y proporcionar ejemplos de uso práctico.

##  Principales librerías 

La documentación es una parte fundamental de cualquier proyecto de desarrollo de software.
Proporciona información crucial sobre cómo utilizar, mantener y contribuir al código. 
En el ecosistema de Python, existen varias bibliotecas y herramientas que facilitan la 
tarea de documentar el código de manera efectiva. En este artículo, exploraremos algunas de
las principales bibliotecas de Python utilizadas para documentar código.

### Sphinx

<img src="https://quintagroup.com/cms/python/images/sphinx-logo.png/sphinx-logo.png" width="400" align="center" />


[Sphinx](https://www.sphinx-doc.org/) es una de las herramientas de documentación más populares en el mundo de Python. Fue originalmente desarrollada para documentar la propia documentación de Python y se ha convertido en una elección común para proyectos de código abierto y proyectos internos. Algunas de sus características clave incluyen:

- Generación de documentación en varios formatos, incluyendo HTML, PDF, ePub y más.
- Utiliza [reStructuredText](https://docutils.sourceforge.io/rst.html) como su formato de marcado predeterminado, que es altamente estructurado y permite documentar de manera eficiente los aspectos técnicos.
- Amplia gama de extensiones y complementos que permiten personalizar y mejorar la documentación.
- Admite la generación automática de documentación a partir de docstrings en el código Python.
- Es especialmente adecuado para documentar bibliotecas, API y proyectos técnicos.

Sphinx es altamente configurable y puede generar documentación de alta calidad y profesional. Sin embargo, puede requerir un tiempo de configuración inicial y tiene una curva de aprendizaje empinada para los principiantes.

### MkDocs

<img src="https://images.g2crowd.com/uploads/product/image/social_landscape/social_landscape_778a7d232b5f8a1b643eae6a2a19150f/mkdocs.png" width="300" align="center" />


[MkDocs](https://www.mkdocs.org/) es una herramienta de generación de documentación que se centra en la simplicidad y la facilidad de uso. Está diseñada para crear documentación de proyectos de una manera simple y rápida, principalmente enfocada en la generación de sitios web de documentación. Algunas de sus características clave incluyen:

- Utiliza [Markdown](https://www.markdownguide.org/getting-started/) como formato de marcado predeterminado, que es fácil de aprender y escribir.
- Ofrece una interfaz de línea de comandos simple para iniciar y generar sitios de documentación.
- Proporciona temas y extensiones para personalizar el aspecto y la funcionalidad de la documentación generada.
- Ideal para proyectos de código abierto y documentación de proyectos pequeños a medianos.

MkDocs es especialmente adecuado para proyectos con necesidades de documentación simples. Es fácil de aprender y usar, lo que lo convierte en una excelente opción para principiantes. Sin embargo, puede ser limitado en funcionalidad en comparación con Sphinx para proyectos técnicos y complejos.

#### MkDocs-Material

<img src="https://embeddedcomputing.weebly.com/uploads/1/1/6/2/11624344/mkdocsmaterial_orig.png" width="300" align="center" />


[MkDocs-Material](https://squidfunk.github.io/mkdocs-material/) es un tema personalizado para MkDocs, una popular herramienta de generación de sitios web estáticos diseñada para crear documentación de proyectos de manera sencilla y efectiva. Este tema, conocido como "Material for MkDocs", se inspira en el elegante diseño de Material Design de Google y está diseñado para ofrecer una experiencia de documentación moderna y atractiva.

Una de las principales características de MkDocs-Material es su enfoque en la legibilidad y la facilidad de navegación. Esto se logra mediante un diseño limpio y organizado que hace que la documentación sea más accesible para los usuarios. Además, el tema proporciona herramientas útiles para mejorar la experiencia de los lectores, como una función de búsqueda integrada que permite a los usuarios encontrar rápidamente la información que necesitan.

Otra ventaja de MkDocs-Material es su navegación intuitiva, que facilita a los usuarios la exploración de la documentación y la navegación entre secciones y páginas. Esto es fundamental para garantizar que los usuarios puedan acceder fácilmente a la información que están buscando sin esfuerzo.







## ¿Por Dónde Empiezo?

La documentación de proyectos sigue una progresión simple:

1. Sin Documentación
2. Alguna Documentación
3. Documentación Completa
4. Buena Documentación
5. Excelente Documentación

Si te sientes perdido acerca de por dónde continuar con tu documentación, observa en qué punto se encuentra tu proyecto en relación con la progresión mencionada anteriormente. ¿Tienes alguna documentación? Si no la tienes, comienza por ahí. Si ya tienes algo de documentación pero te faltan algunos de los archivos clave del proyecto, comienza agregándolos.

Al final, no te desanimes ni te sientas abrumado por la cantidad de trabajo necesario para documentar el código. 

Una vez que comiences a documentar tu código, te resultará más fácil seguir adelante. 

## Referencias

* [Documenting Python Code: A Complete Guide](https://realpython.com/documenting-python-code/)
* [Document Your Python Code and Projects With ChatGPT](https://realpython.com/document-python-code-with-chatgpt/)