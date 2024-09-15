---
title: "Gitlab PDF"
subtitle: "Cómo aprovechar GitLab CI/CD para generar archivos PDF utilizando los artefactos de un Pipeline."

author: "Francisco Alfaro"
date: "2023-10-01"
categories: [ci-cd,software-development]
image: "../images/gitlab-ci.png"
---

# Generando Archivos PDF con GitLab CI/CD

<img src="../images/gitlab-ci.png" alt="" align="center" width="150"/>

<br>

[GitLab CI/CD](https://docs.gitlab.com/ee/ci/) es una potente herramienta que permite automatizar y gestionar el ciclo de vida de las aplicaciones de software. 

CI (Integración Continua) y CD (Entrega Continua) 
son prácticas esenciales en el desarrollo de software
moderno que buscan mejorar la calidad del código, aumentar 
la eficiencia y reducir los errores. GitLab CI/CD se integra 
de manera nativa en el flujo de trabajo de GitLab, lo que lo 
convierte en una opción atractiva para equipos de desarrollo.

- **CI (Integración Continua)**: Es el proceso de integrar cambios de código frecuentes en un repositorio compartido. Esto implica la ejecución automática de pruebas y análisis de calidad cada vez que se envía código. El objetivo es identificar y corregir problemas de manera temprana en el ciclo de desarrollo.


- **CD (Entrega Continua)**: Una vez que las pruebas de CI se han superado con éxito, el código se considera apto para su implementación en entornos de producción o de pruebas. El objetivo es entregar de manera eficiente y confiable el software a los usuarios finales.


## Artefactos en GitLab CI/CD

<img src="https://cdn4.iconfinder.com/data/icons/folders-23/140/_Code-512.png" alt="" align="center" width="150"/>


Antes de profundizar en la generación de archivos PDF,
es importante comprender el concepto de "artefactos" 
en GitLab CI/CD. Los artefactos son archivos o conjuntos
de archivos generados como resultado de una ejecución exitosa 
de un pipeline.

Estos artefactos se almacenan en GitLab y se pueden
utilizar posteriormente en otros trabajos o pipelines. 

En el contexto de la generación de archivos PDF, 
los artefactos son esenciales porque permiten
que los archivos PDF generados en un trabajo 
se conserven y utilicen en otros trabajos o etapas del pipeline.

## Generación de Archivos PDF con GitLab CI/CD

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/PDF_file_icon.svg/1667px-PDF_file_icon.svg.png" alt="" align="center" width="150"/>


La generación de archivos PDF como parte de su proceso 
de CI/CD puede ser útil en varios escenarios, como 
la creación de informes automatizados, la generación
de documentación técnica o la producción de facturas en
línea.

A continuación, detallaremos cómo lograrlo utilizando GitLab CI/CD:

> **Nota**: Tomaremos como referencia el siguiente [repositorio](https://gitlab.com/fralfaro/cv).

### Paso 1: Preparación del Proyecto

Antes de comenzar, asegúrese de que su proyecto
de GitLab esté configurado correctamente y tenga 
acceso a GitLab CI/CD. También debe tener un 
archivo de código fuente que desee convertir en un archivo PDF.

Asegúrese de que cualquier dependencia necesaria esté especificada
en su archivo de configuración de CI/CD.

<img src="https://raw.githubusercontent.com/fralfaro/blog/main/posts/2023/img/step_01.png" alt="" align="center" width="750"/>


### Paso 2: Creación de un Script de Generación de PDF

Cree un script que sea capaz de generar el archivo PDF a 
partir de sus datos de entrada. 

Este script debería tomar los datos relevantes y 
formatearlos en un archivo PDF.

<img src="https://raw.githubusercontent.com/fralfaro/blog/main/posts/2023/img/step_02.png" alt="" align="center" width="750"/>


### Paso 3: Configuración de GitLab CI/CD

En su repositorio de GitLab, cree un archivo llamado 
`.gitlab-ci.yml` si aún no lo ha hecho.

Este archivo contiene la configuración de su pipeline. 

Aquí hay un ejemplo de cómo podría verse:

```yaml
stages:
  - pdf

generate_pdf:
  stage: pdf
  image: aergus/latex
  script:
    - latexmk -pdf **/*.tex

  artifacts:
    paths:
      - ./*.pdf
```

En este ejemplo:

```yaml
stages:
  - pdf
```

1. `stages`: Esta sección define las etapas (stages). En este caso, solo se define una etapa llamada "pdf". Las etapas son divisiones lógicas en el pipeline que agrupan trabajos relacionados. En este caso, el pipeline tiene una sola etapa llamada "pdf".

```yaml
generate_pdf:
  stage: pdf
  image: aergus/latex
  script:
    - latexmk -pdf **/*.tex
```

2. `generate_pdf`: Esta sección define un trabajo (job) llamado "generate_pdf". Un trabajo es una unidad de ejecución en el pipeline. Aquí está el desglose de esta sección:

   - `stage: pdf`: Esta línea especifica que este trabajo pertenece a la etapa "pdf" definida previamente. En otras palabras, este trabajo se ejecutará en la etapa "pdf" del pipeline.

   - `image: aergus/latex`: Esta línea especifica la imagen Docker que se utilizará para ejecutar este trabajo. En este caso, se utiliza la imagen "aergus/latex", que contiene un entorno LaTeX para compilar documentos PDF. Esta imagen es esencial para compilar archivos LaTeX en archivos PDF.

   - `script`: Aquí se definen los comandos que se ejecutarán en el trabajo. En este caso, se utiliza el comando "latexmk -pdf **/*.tex". Este comando utiliza "latexmk" para compilar todos los archivos ".tex" en el proyecto en archivos PDF. El uso de `**/*.tex` significa que buscará archivos ".tex" en todos los subdirectorios del proyecto.

```yaml
artifacts:
  paths:
    - ./*.pdf
```

3. `artifacts`: Esta sección especifica qué archivos deben considerarse artefactos y, por lo tanto, se conservarán después de una ejecución exitosa del trabajo. Aquí está el desglose de esta sección:

   - `paths: ./*.pdf`: Esta línea especifica que todos los archivos con extensión ".pdf" en el directorio actual deben considerarse artefactos. Esto significa que los archivos PDF generados como resultado de la ejecución de este trabajo se conservarán y estarán disponibles para su descarga después de el pipeline se haya ejecutado con éxito.

### Paso 4: Ejecución del pipeline

Cada vez que realice un envío de código (push) o active manualmente el pipeline, 
GitLab ejecutará el trabajo de generación de PDF. 
El script generará el archivo PDF y lo almacenará como un artefacto.

<img src="https://raw.githubusercontent.com/fralfaro/blog/main/posts/2023/img/step_03.png" alt="" align="center" width="750"/>



### Paso 5: Acceso a los Archivos PDF Generados

Una vez que el pipeline se haya ejecutado con éxito, 
puede acceder a los archivos PDF generados en GitLab.

Vaya a la página de su proyecto en GitLab, seleccione "CI/CD" y 
luego "Artefactos". 

[Aquí](https://gitlab.com/fralfaro/cv/-/jobs/artifacts/main/browse?job=generate_pdf) encontrará el archivo PDF generado que puede descargar.

## Conclusiones

GitLab CI/CD es una herramienta
poderosa que puede ayudar en la automatización 
de una amplia variedad de tareas, incluida 
la generación de archivos PDF. 

Al comprender cómo utilizar artefactos en
GitLab CI/CD y seguir los pasos mencionados anteriormente,
puede integrar fácilmente la generación de PDF en su flujo
de trabajo de desarrollo, lo que ahorra tiempo y esfuerzo, 
y garantiza la consistencia y la calidad en la creación de
documentos PDF automatizados.

## Referencias

* [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/)
* [Job artifacts](https://docs.gitlab.com/ee/ci/jobs/job_artifacts.html)