**Todos los archivos python utilizados en este test técnicos son ejecutados desde app.py, para los codigos especificos de cada uno, porfavor revisar la carpeta scripts.**

P.1:
    Diseñar un modelo de datos. Genere una propuesta sobre cómo guardar los datos. Justifique esa propuesta y explique por qué es la mejor opción.

R.1:
    Para esta base de datos realicé un modelo de estrella, con la fact table que contiene la información de trips, y 2 dimension table para almacenar users y vehicles.
    ![Screenshot](./images/star_scheme.png)
    FIGURA 1.

    Elegí este modelo ya que para el caso presentado al no tener información respecto a requerimientos de
    seguridad o recursos permite una arquitectura más facil de comprender al no estar tan disgregada y sigue poniendo
    enfasís en los viajes realizados que viene a ser complementada por las tablas de dimensiones con el objetivo de no repetir 
    información.

    De todas formas si existieran requisitos especificos de privacidad de los datos o solicitudes del cliente interno especificas dejo también
    una arquitectura con más tablas aun que se trabajara en base al primer esquema señalado.
    
![Screenshot](./images/alt_scheme.png)
FIGURA 2.

P.3
    Crea las tablas del modelo de datos que diseñaste en el paso 1. Puede usar scripts SQL o código en Python.

R.3
    Se realizó a través de modelo_datos.py donde se realiza la conexión a la base de datos en postgres
    creando las tablas necesarias para el modelo si es que estas no existen

P.4
    Genera archivos en Python para cargar los datos del archivo trips.csv en las tablas que creaste en el paso anterior.

R.4
    Se realizó a través de carga_datos.py donde utilizando pandas se proceso el archivo csv entregado creando dataframes
    especificos según la tabla necesaria. Estos posteriormente son cargados utilizando la función de pandas especifica junto con la conexión
    a través de sqlalchemy al postgres.


P.5 
    Cree una nueva tabla en Postgres llamada resumen_diario.
    
    i) Genera con Python un proceso de ETL que cargue en la tabla un resumen por día de:
        la cantidad de viajes
        los suma de ingresos
        el promedio de ingresos
        la suma de metros recorridos. Explique y justifique las decisiones que tomó para generar el resumen. Considere que diariamente no habrá más de 100.000 viajes.
    ii) Señale (sin necesidad de implementar) qué procesos podría desarrollar para asegurar la consistencia de los datos en la tabla resumen_diario.
    iii) Señale (sin necesidad de implementar) cómo podría automatizar este proceso de ETL de manera diaria.

R.5
    i) Se realizó a través de carga_datos.py donde se agruparon de forma diaria los valores y se realizaron los cálculos requeridos. Posteriormente se renombro la columna
    a dia y se creo una columna de id. Después se realizo la carga a las tablas utilizando la función de pandas especifica junto con la la conexión a través de 
    sqlalchemy al postgres.

    Para generar el resumen utilice las funciones de pandas incorporadas optimizando el codigo, donde cantidad de viajes es un 'count' al número de registros para ese día
    especifico, la suma de ingresos sería 'sum' de los montos totales del día y al igual que el promedio sería 'mean' de esta misma columna, y con respecto a la suma de metros
    seria 'sum' de la columna que ve los metros de los trayectos del día.

    Está lógica la implemente según la información disponible en el ejercicio, asumiendo que es la primera vez que se carga toda la información a la tabla resumen_diario, para
    el manejo de día a día de la base de datos se creo un archivo llamado operador_diario.py con el ejemplo de como se realizaría.

    ii) En primer lugar revisar que los datos no se encuentren dúplicados, y haría restricciones para verificar que los 
    datos ingresados tengan el formato correspondiente. Un ejemplo de esto sería tambien revisar que el price_tax se calcula correctamente 
    y corresponde al 19% del price_amount y verificaria que price_total sea correcto.
    Otro punto relevante es que crearia un código para almacenar los valores rechazados en otra tabla para así poder análisis del por que ha ocurrido esto.

    iii) A pesar de no implementarlo agregue un código llamador operador_diario.py donde está el como realizaría el proceso para manejarlo de forma diaria a través de
    aiflow con el scheduler filtrando el csv por la fecha del día con el objetivo de solamente realizar los calculos en los datos del día para optimizar recursos y
    posteriormente cargando esos datos a la tabla existente. Cabé destacar que el código no se ejecutará ya que la fecha de hoy al no existir en la base de datos no retornaría nada, por eso airflow no se encuentra instalado, el código es solamente a modo de ejemplo de como se llevaría a cabo el ETL de forma diaria.



P.6
    La empresa quiere implementar un sistema de descuentos mediante cupones. ¿Cómo modificarías el modelo de datos para agregarlo? Describa su propuesta, justifique y explique por qué es la mejor opción. No es necesario que lo implemente.

R.6
    En caso de implementar el sistema de descuento a través de cupones crearia una nueva tabla de dimensión para los pagos llamada payments, 
    sacando de trips price_amount, price_tax y price_total. En la nueva tabla payments agregaria las columnas price_amount_before_cupon, 
    price_tax_before_cupon, cupon_amount y con eso pondria 3 columnas más las cuales serían price_amount_after_cupon, price_tax_after_cupon y price_total.
    
![Screenshot](./images/cupon_scheme.png)
    FIGURA 3.

    Esta sería la mejor forma ya que al agregar un cupón este se encuentra mayormente relacionando con el pago. 
    Permite crear una nueva tabla más relacionada a la parte financiera del negocio, capturando más datos como 
    el viaje antes y después de los descuentos, además de más información que pudiera ser relevante con respecto a esta área. 
    A su vez permite que, al momento de generar reporteria a un área financiera, consultar solamente esta tabla trayendo la información pertinente. 
    
    Se debe entender que la arquitectura está basada en la información del caso, ya que por ejemplo si
    el área de finanzas requiriera no solo está información del pago si no que también de los vehiculos utilizados 
    por un tema del costo de estos, e incluso la distancia recorrida por temas de vida útil, y varios casos más donde toda información
    disgregada se tenga que volver a unir esto repecutiria en la arquitectura planteada y se podría evaluar. 