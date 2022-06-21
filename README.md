# CouponsAPI V1.0
READ requirments.txt

  La API lo que crea es un microservicio el cual se le pueden agregar cupones de descuento, gracias a REST-FRAMEWORK a los objetos se los puede visualizar a traves de un GET y se pueden llamar individualmente.
  Este fue creado para luego poder conectarlo al primer microservicio de planes.
  Lo primero que se creo fue un entorno virtual(VirtualEnv) en donde se le instalo propiamente django y posteriormente fue configurado, en el modifcamos el archivo models.py donde agregamos una sola tabla para los cupones con sus respectivos atributos. Luego de eso se instalo DjangoRestFramework para poder trabajar con los metodos GET y Post de manera mas comoda. Fueron configurados los archivos necesarios para que el funcionamiento sea correcto(urls.py, serializers.py, views.py, admin.py). Ya todo confirgurado se fue a probar la API para corroborar algun error que existiera, para los errores que existieron fueron solucionados y se probaba nuevamente el funcionamiento. Al final de esta version no se encuentra con ningun bug y simplemente esta preparada para la conexion con el otro el microservicio
  El estado del proyecto es finalizado en su version 1.0 y esperando a proximas actualizaciones para la conexion.
   
  
