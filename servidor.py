import socket
import threading

class Server:
  def __init__(self):
    self.host = 'localhost'
    self.port = 5555
    self.currentC = 0
    self.alumnos = {}

  def Inscripcion(self, connection, client):
    if client in self.alumnos:
      connection.sendall("Usted ya está inscrito en el curso".encode('utf-8'))
      return
    
    elif self.currentC >= 15:
      # Enviar mensaje de rechazo
      connection.sendall("Rechazo de inscripción: Limite de almnos alcanzado.".encode('utf-8'))
      return
    
    else:
      self.currentC += 1
      self.alumnos[client] = self.currentC
      print('El cliente ', client,' se ha inscrito en la posición ', self.currentC,'.')
      connection.sendall(f"Inscrito en el curso en la posición {self.currentC}".encode('utf-8'))

  def Fecha(self, connection):
    connection.sendall("El curso empezará a las 9:00hrs del dia 15 de diciembre".encode('utf-8'))

  def Posicion(self, connection, client):
    if client in self.alumnos:
      connection.sendall(f"Usted está inscrito en la posición número {self.alumnos.get(client)}".encode('utf-8'))
    else:
      connection.sendall("Usted no está inscrito en el curso".encode('utf-8'))

  def Cliente(self, connection, client):
    while True:
      data = connection.recv(11)

      if data.decode('utf-8') == 'inscripcion':
        print('\nEl cliente ', client,' ha solicitado inscribirse.')
        self.Inscripcion(connection, client)

      elif data.decode('utf-8') == 'fecha':
        print('\nEl cliente ', client ,' ha solicitado la fecha y hora del curso.')
        self.Fecha(connection)

      elif data.decode('utf-8') == 'posicion':
        print('\nEl cliente ', client,' ha solicitado ver su posicion de inscripción')
        self.Posicion(connection, client)
        
      elif data.decode('utf-8') == 'exit':
        print('\nEl cliente ', client,' se ha desconectado.')
        break
      
      else:
        print('Sin mensaje', client)
        break

  def Inicio(self):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Vincular con el socket al puerto
    sock.bind((self.host, self.port))

    # Escuchando las conexiones entrantes
    sock.listen(5)

    try:
      while True:
        # Esperando por conexion
        print("\nEsperando alguna conexion..")
        connection, client = sock.accept()

        print(client, ' se ha conectado.')
        connection.sendall("Bienvenido al Servidor".encode('utf-8'))

        # Iniciar nuevo hilo para el cliente
        cliente_hilo = threading.Thread(target=self.Cliente, args=(connection, client))
        cliente_hilo.start()

    except KeyboardInterrupt:
      print("Servidor interrumpido por el usuario")

    finally:
      # Cerrar la conexion  
      connection.close()

if __name__ == "__main__":
  serv = Server()
  serv.Inicio()