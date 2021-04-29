#
# Clase que representa un Alumno.
#
class Alumno(object):
  id = 1
  nombre = '' 
  apellidos = ''

  #  
  # Constructor.
  #
  def __init__(self):
    # Id auto_increment
    self.id = Alumno.id
    Alumno.id += 1

  #
  # Función para formatear los datos del alumno.
  # Devuelve: 
  #   String: cadena formateada.
  #
  def formato(self):
    forma = 'Alumno(id={0},nombre={1},apellidos={2})'
    return forma.format( str(self.id), self.nombre, self.apellidos )
  
#
# Clase que representa el Sistema.
#
class Sistema(object):
  alumnos = [] # array de alumnos.
  opcion = 0 # opcion que selecciono el usurio.
  
  #
  # Menu de navegacion para el usuario.
  #
  def menu(self):
    while self.opcion != 4:
      print('+------------------+')
      print('|   M   E   N  U   |')
      print('+------------------+')
      print('| 1.- Agregar      |')
      print('| 2.- Listar       |')
      print('| 3.- Eliminar     |')
      print('| 4.- Salir        |')
      print('+------------------+')
      
      opcion = input(" Opción: ")
      if (opcion.isdigit()): 
        self.opcion = int(opcion)
      else:
        self.opcion = 0
        
      print()
      self.accion()
      print()

  #
  # Valida la opcion que escogio el usuario.
  #
  def accion(self):
    if self.opcion == 1:
      self.agregar()
    elif self.opcion == 2:
      self.listar()
    elif self.opcion == 3:
      self.eliminar()
    elif self.opcion == 4:
      pass
    else:
      print('Opción incorrecta')

  #
  # Agrega un nuevo alumno a la lista.
  #
  def agregar(self):
    a = Alumno()
    a.nombre = input(" Nombre: ").strip().capitalize()
    a.apellidos = input(" Apellidos: ").strip().capitalize()
    # Agregamos el objeto a la lista.
    self.alumnos.append(a) 
    print(' ¡Ok Datos Guardados!')

  #
  # Enlista todos los alumnos.
  #
  def listar(self):
    for a in self.alumnos:
      print(a.formato())

  #
  # Elimina un alumno por su id.
  #
  def eliminar(self):
    id = int( input(" Id a eliminar: ") )
    # Recorremos toda la lista.
    for i in range( len(self.alumnos) ):
      # Obtenemos el alumno en la posicion actual del for.
      a = self.alumnos[i]
      if a.id == id: # Comparamos que los Ids sean iguales.
        opcion = input(' Desea eliminar a: "' + a.formato() + '" S/N: ')
        if opcion.upper() == 'S':
          # Removemos el item de la lista.
          self.alumnos.remove(a)
          print(' ¡Ok Datos Borrados!')
        # endif
        break
      # endif
    # endfor

#
# Metodo principal
#
if __name__ == "__main__":
  s = Sistema()
  s.menu()

